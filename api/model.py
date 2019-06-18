import os
import time

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.python import keras
from tensorflow.python.keras import layers

from api import dataset
from api.configuration import GEN_NOISE_INPUT_SHAPE, DEBUG_LOG, N_CHANNELS, IMG_SHAPE, LC_GEN_SAMPLE_SAVE_INTERVAL, \
    CKPT_SAVE_INTERVAL, BATCH_SIZE, TB_GEN_SAMPLE_SAVE_INTERVAL


def generator():
    """
    Purpose of the Generator model is to images that looks real. During training,
    the Generator progressively becomes better at creating images that look real.

    The Generator model does up-sampling to produces images from random noise. It
    takes random noise as an input, then up-samples several times until reach
    desired image size (in this case 224x224x3).

    Returns:
         The Generator model.
    """
    start = time.time()

    model = keras.Sequential([
        layers.Dense(units=7 * 7 * 256, use_bias=False, input_shape=(GEN_NOISE_INPUT_SHAPE,)),
        layers.BatchNormalization(),
        layers.LeakyReLU(),
        layers.Reshape((7, 7, 256)),

        layers.Conv2DTranspose(filters=128, kernel_size=(5, 5), strides=(1, 1), padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),

        layers.Conv2DTranspose(filters=64, kernel_size=(5, 5), strides=(2, 2), padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),

        layers.Conv2DTranspose(filters=32, kernel_size=(5, 5), strides=(2, 2), padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),

        layers.Conv2DTranspose(filters=3, kernel_size=(5, 5), strides=(2, 2), padding="same", use_bias=False,
                               activation="tanh"),
    ])

    end = time.time()
    if DEBUG_LOG:
        print("Execution time: {:.9f}s (generator)".format(end - start))

    return model


def generator_loss(fake_output):
    """
    The generator's loss quantifies how well it was able to
    trick the discriminator. Intuitively, if the generator
    is performing well, the discriminator will classify the
    fake images as real (or 1).

    Arguments:
        fake_output: Fake image produced by Generator model.

    Returns:
        Loss of the Generator.
    """
    cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

    return cross_entropy(tf.ones_like(fake_output), fake_output)


def generator_optimizer():
    """
    The Generator model and the Discriminator model uses different
    optimizers because tow different networks are trained.

    Returns:
        Generator optimizer.
    """
    return tf.optimizers.Adam(1e-4)


def discriminator():
    """
    Purpose of the Discriminator model is to learn to tell real images
    apart from fakes. During training, the Discriminator progressively
    becomes better at telling fake images from real ones. The process
    reaches equilibrium when the Discriminator can no longer distinguish
    real images from fakes.

    The Discriminator is a simple CNN-based image classifier. It outputs
    positive values for real images, and negative values for fake images.

    Returns:
        The Discriminator model.
    """
    start = time.time()

    model = keras.Sequential([
        layers.Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same',
                      input_shape=[IMG_SHAPE[0], IMG_SHAPE[1], N_CHANNELS]),
        layers.LeakyReLU(),
        layers.Dropout(rate=0.3),

        layers.Conv2D(filters=128, kernel_size=(5, 5), strides=(2, 2), padding='same'),
        layers.LeakyReLU(),
        layers.Dropout(rate=0.3),

        layers.Flatten(),
        layers.Dense(units=1),
    ])

    end = time.time()
    if DEBUG_LOG:
        print("Execution time: {:.9f}s (discriminator)".format(end - start))

    return model


def discriminator_loss(real_output,
                       fake_output):
    """
    This method quantifies how well the discriminator is able to distinguish
    real images from fakes. It compares the discriminator's predictions
    on real images to an array of 1s, and the discriminator's predictions
    on fake (generated) images to an array of 0s.

    Arguments:
        real_output: Real image from dataset.
        fake_output: Fake image produced by Generator model.

    Returns:
        Total loss of the Discriminator.
    """
    cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss

    return total_loss


def discriminator_optimizer():
    """
    The Generator model and the Discriminator model uses different
    optimizers because tow different networks are trained.

    Returns:
        Discriminator optimizer.
    """
    return tf.optimizers.Adam(1e-4)


def define_checkpoint(gen_model,
                      gen_optimizer,
                      dis_model,
                      dis_optimizer):
    """
    Saves and restores (if needed) checkpoints.

    Arguments:
        gen_model: Generator model.
        gen_optimizer: Generator optimizer.
        dis_model: Discriminator model.
        dis_optimizer: Discriminator optimizer.

    Returns:
        Checkpoint object, Checkpoint name prefix.
    """
    start = time.time()

    checkpoint_dir = 'res/training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=gen_optimizer,
                                     discriminator_optimizer=dis_optimizer,
                                     generator=gen_model,
                                     discriminator=dis_model)
    checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

    end = time.time()
    if DEBUG_LOG:
        print("Execution time: {:.9f}s (define_checkpoint)".format(end - start))

    return checkpoint, checkpoint_prefix


def train(real_image_dataset,
          last_epoch,
          epochs,
          gen_model,
          gen_optimizer,
          dis_model,
          dis_optimizer,
          checkpoint,
          checkpoint_prefix):
    """
    Train the Generator and Discriminator simultaneously. At the
    beginning of the training, the generated images look like
    random noise. As training progresses, the generated digits
    will look increasingly real. During training process, generated
    images and checkpoints have stored on disk.

    Arguments:
        real_image_dataset: Dataset that contains real images.
        last_epoch: If checkpoint is used, what was the
        last proceed epoch.
        epochs: How many epochs should model run.
        gen_model: Generator model.
        gen_optimizer: Generator optimizer.
        dis_model: Discriminator model.
        dis_optimizer: Discriminator optimizer.
        checkpoint: Checkpoint object.
        checkpoint_prefix: Checkpoint name prefix.
    """
    sum_execution_time = 0

    # Define TensorBoard loss metrics
    gen_loss_metric = keras.metrics.Mean('train_loss', dtype=tf.float32)
    dis_loss_metric = keras.metrics.Mean('train_loss', dtype=tf.float32)

    # Define TensorBoard metrics save path
    train_log_dir = 'logs/gradient_tape/' + 'train'
    train_summary_writer = tf.summary.create_file_writer(train_log_dir)

    # Random input for the generator model
    seed = tf.random.normal([16, GEN_NOISE_INPUT_SHAPE])

    for epoch in range(last_epoch, epochs):
        start_epoch = time.time()

        for image_batch in real_image_dataset:
            # Train step
            start_train = time.time()
            train_step(
                image_batch,
                gen_model,
                gen_optimizer,
                dis_model,
                dis_optimizer,
                gen_loss_metric,
                dis_loss_metric
            )
            end_train = time.time()
            if DEBUG_LOG:
                print("\tExecution time: {:.9f}s (train_step)".format(end_train - start_train))

            # Test step
            start_test = time.time()
            real_dis_acc, fake_dis_acc, combined_dis_acc = test_step(
                image_batch,
                gen_model,
                dis_model
            )
            end_test = time.time()
            if DEBUG_LOG:
                print("\tExecution time: {:.9f}s (test_step)".format(end_test - start_test))

            # Record TensorBoard scalar metrics
            start_metrics = time.time()
            with train_summary_writer.as_default():
                with tf.name_scope('Loss'):
                    tf.summary.scalar('Generator', gen_loss_metric.result(), step=epoch)
                    tf.summary.scalar('Discriminator', dis_loss_metric.result(), step=epoch)

                with tf.name_scope('Accuracy'):
                    tf.summary.scalar('Real Discriminator', real_dis_acc, step=epoch)
                    tf.summary.scalar('Fake Discriminator', fake_dis_acc, step=epoch)
                    tf.summary.scalar('Combined Discriminator', combined_dis_acc, step=epoch)

            gen_loss_metric.reset_states()
            dis_loss_metric.reset_states()

            # TensorBoard Weights and Biases metric
            with train_summary_writer.as_default():
                with tf.name_scope('Generator'):
                    with tf.name_scope('Weights'):
                        for gen_layer in gen_model.layers:
                            try:
                                tf.summary.histogram(gen_layer.name, gen_layer.get_weights()[0], step=epoch)
                            except Exception:
                                pass

                with tf.name_scope('Discriminator'):
                    for dis_layer in dis_model.layers:
                        try:
                            with tf.name_scope('Weights'):
                                tf.summary.histogram(dis_layer.name, dis_layer.get_weights()[0], step=epoch)
                            with tf.name_scope('Biases'):
                                tf.summary.histogram(dis_layer.name, dis_layer.get_weights()[1], step=epoch)
                        except Exception:
                            pass

            end_metrics = time.time()
            if DEBUG_LOG:
                print("\tExecution time: {:.9f}s (summary/metrics)".format(end_metrics - start_metrics))

        # Save generator sample image
        save_image(gen_model,
                   epoch + 1,
                   seed,
                   train_summary_writer)

        # Save model checkpoint
        if (epoch + 1) % CKPT_SAVE_INTERVAL == 0:
            start_ckpt = time.time()
            checkpoint.save(file_prefix=checkpoint_prefix)
            end_ckpt = time.time()
            if DEBUG_LOG:
                print("\tExecution time: {:.9f}s (checkpoint.save)".format(end_ckpt - start_ckpt))

        epoch_execution_time = time.time() - start_epoch
        sum_execution_time += epoch_execution_time
        print('Time for the epoch {} is {} sec'.format(epoch + 1, epoch_execution_time))

        # Track execution time of each epoch in TensorBoard
        with train_summary_writer.as_default():
            with tf.name_scope('Execution time'):
                tf.summary.scalar('Train epoch', epoch_execution_time, step=epoch)
                tf.summary.scalar('Average epoch', (sum_execution_time / (epoch + 1)), step=epoch)
                tf.summary.scalar('Sum epoch', sum_execution_time, step=epoch)

    print("Execution time: {:.9f}s (train)".format(sum_execution_time))


@tf.function
def train_step(images,
               gen_model,
               gen_optimizer,
               dis_model,
               dis_optimizer,
               gen_loss_metric,
               dis_loss_metric):
    """
    The training loop begins with generator receiving a random seed as input.
    That seed is used to produce an image. The discriminator is then used
    to classify real images (drawn from the training set) and fakes
    images (produced by the generator). The loss is calculated for each
    of these models, and the gradients are used to update the generator
    and discriminator.

    The tf.function annotation causes this function to be compiled. This
    allows the TensorFlow runtime to apply optimizations and exploit
    parallelism during the computation. Some reasons not to use this
    annotation:
      - Variables need to be created each time the function is called.
      - You want dynamic Python control flow inside of the function
      (ie, that should change each time you call the function based
      on criteria not passed to the function as args/kwargs).

    Arguments:
        images: Real image batch.
        gen_model: Generator model.
        gen_optimizer: Generator optimizer.
        dis_model: Discriminator model.
        dis_optimizer: Discriminator optimizer.
        dis_loss_metric: TensorBoards discriminator loss metrics.
        gen_loss_metric: TensorBoards generator loss metrics.
    """
    noise = tf.random.normal([dataset.BATCH_SIZE, GEN_NOISE_INPUT_SHAPE])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = gen_model(noise, training=True)

        real_output = dis_model(images, training=True)
        fake_output = dis_model(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, gen_model.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, dis_model.trainable_variables)

    gen_optimizer.apply_gradients(zip(gradients_of_generator, gen_model.trainable_variables))
    dis_optimizer.apply_gradients(zip(gradients_of_discriminator, dis_model.trainable_variables))

    gen_loss_metric(gen_loss)
    dis_loss_metric(disc_loss)


@tf.function
def test_step(real_images,
              gen_model,
              dis_model):
    """
    Calculates Discriminator accuracy on real and
    fake (generated) images.

    Arguments:
        real_images: Images from the real dataset.
        gen_model: A generator model.
        dis_model: A discriminator model.

    Returns:
       Discriminator accuracy on the fake and real images
       as well as combined accuracy of them.
    """
    # Generate fake images
    random_seed = tf.random.normal([BATCH_SIZE, GEN_NOISE_INPUT_SHAPE])

    fake_images = gen_model(random_seed, training=False)

    # Give predictions
    real_dis_prediction = dis_model(real_images)
    fake_dis_prediction = dis_model(fake_images)

    # Actual accuracy
    correct = len(real_dis_prediction[real_dis_prediction >= 0.0])
    wrong = len(real_dis_prediction[real_dis_prediction < 0.0])
    real_dis_acc = float(correct) / float(correct + wrong)

    # Fake accuracy
    correct = len(fake_dis_prediction[fake_dis_prediction < 0.0])
    wrong = len(fake_dis_prediction[fake_dis_prediction >= 0.0])
    fake_dis_acc = float(correct) / float(correct + wrong)

    # # Combined accuracy
    combined_dis_acc = (real_dis_acc + fake_dis_acc) / 2

    return real_dis_acc, fake_dis_acc, combined_dis_acc


def save_image(gen_model,
               epoch,
               test_input,
               train_summary_writer):
    """
    Stores generated image examples during the training
    process.

    Arguments:
        gen_model: Generator model.
        epoch: A Current epoch.
        test_input: A Generated image.
    """
    start = time.time()

    predictions = None
    if (epoch % LC_GEN_SAMPLE_SAVE_INTERVAL == 0) or (epoch % TB_GEN_SAMPLE_SAVE_INTERVAL == 0):
        predictions = gen_model(test_input, training=False)

    # Record image to local storage.
    if epoch % LC_GEN_SAMPLE_SAVE_INTERVAL == 0:
        for i in range(predictions.shape[0]):
            img = np.array(predictions[i]) * 127.5 + 127.5
            img = img.astype(np.int, copy=False)
            plt.imsave('res/image_at_epoch_{:05d}_{:05d}.png'.format(epoch, i), img)

    # Record TensorBoard image metrics
    if epoch % TB_GEN_SAMPLE_SAVE_INTERVAL == 0:
        with tf.name_scope("Samples"):
            with train_summary_writer.as_default():
                for i in range(predictions.shape[0]):
                    img = np.array(np.array(predictions[i]) * 0.5 + 0.5).astype(np.float)
                    img = np.reshape(img, (1, IMG_SHAPE[0], IMG_SHAPE[1], N_CHANNELS))
                    tf.summary.image('image_{:03d}.png'.format(i), img, step=epoch)

    end = time.time()
    if DEBUG_LOG:
        print("\tExecution time: {:.9f}s (save_image)".format(end - start))

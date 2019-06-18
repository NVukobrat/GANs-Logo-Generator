import time

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from api.configuration import GEN_NOISE_INPUT_SHAPE, TB_GEN_SAMPLE_SAVE_INTERVAL, LC_GEN_SAMPLE_SAVE_INTERVAL, \
    IMG_SHAPE, N_CHANNELS, DEBUG_LOG


def loss_and_accuracy(train_summary_writer,
                      gen_loss_metric,
                      epoch,
                      dis_loss_metric,
                      real_dis_acc,
                      fake_dis_acc,
                      combined_dis_acc):
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


def weights_and_biases(train_summary_writer,
                       gen_model,
                       epoch,
                       dis_model):
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


def execution_time(train_summary_writer,
                   epoch_execution_time,
                   epoch,
                   sum_execution_time):
    with train_summary_writer.as_default():
        with tf.name_scope('Execution time'):
            tf.summary.scalar('Train epoch', epoch_execution_time, step=epoch)
            tf.summary.scalar('Average epoch', (sum_execution_time / (epoch + 1)), step=epoch)
            tf.summary.scalar('Sum epoch', sum_execution_time, step=epoch)


def save_image(gen_model,
               epoch,
               train_summary_writer):
    """
    Stores generated image examples during the training
    process.

    Arguments:
        gen_model: Generator model.
        epoch: A Current epoch.
    """
    start = time.time()
    test_input = tf.random.normal([16, GEN_NOISE_INPUT_SHAPE])

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

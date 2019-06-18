import os
import random
import time

import tensorflow as tf

from api.configuration import DEBUG_LOG, MAX_SAMPLES_PER_CLASS, MAX_CLASSES, BATCH_SIZE, N_CHANNELS, IMG_SHAPE


# TODO: Try to make this function compatible with tf.function.
def load_normalized_dataset(path):
    """
    Loads dataset in form of Dataset object used for batch
    training.

    When requested paths have been collected, images located
    on the paths are read into the tensors and transformed
    to the Dataset object used for batch training.

    The dataset path should be in the form:
    dataset_root/class_name/image_name.

    Arguments:
        path: A relative path to the dataset root.

    Returns:
        A normalized dataset.
    """
    start = time.time()

    image_samples_path = list()
    class_count = 1
    for class_dir in os.listdir(path):
        img_sample_count = 1
        full_class_dir = os.path.join(path, class_dir)
        for image_name in os.listdir(full_class_dir):

            full_image_name = os.path.join(full_class_dir, image_name)
            image_samples_path.append(full_image_name)

            if img_sample_count == MAX_SAMPLES_PER_CLASS:
                break

            img_sample_count += 1

        if class_count == MAX_CLASSES:
            break

        class_count += 1

    random.shuffle(image_samples_path)

    with open('image_list.txt', 'w') as f:
        for item in image_samples_path:
            f.write("%s\n" % item)

    scene_dataset = tf.data.Dataset.from_tensor_slices(
        image_samples_path
    )

    scene_dataset = scene_dataset.map(load_and_preprocess_image)

    scene_dataset = scene_dataset.batch(
        BATCH_SIZE
    )

    end = time.time()
    if DEBUG_LOG:
        print("Execution time: {:.9f}s (load_normalized_dataset)".format(end - start))

    return scene_dataset


@tf.function
def load_and_preprocess_image(path):
    """
    Reads image from the path and returns preprocessed image.

    Arguments:
        path: Path to the image.

    Returns:
        Preprocessed image.
    """
    image = tf.io.read_file(path)
    return preprocess_image(image)


@tf.function
def preprocess_image(image):
    """
    Preprocess the given image. It decodes JPEG/PNG image and
    normalizes it to the [-1, 1] range.

    Arguments:
        image: A tensor of file content.

    Returns:
        Decoded and normalized image.
        """
    image = tf.cond(
        tf.image.is_jpeg(image),
        lambda: tf.image.decode_jpeg(image, channels=N_CHANNELS),
        lambda: tf.image.decode_png(image, channels=N_CHANNELS))
    image = tf.image.resize(image, IMG_SHAPE)
    image = (image - 127.5) / 127.5  # [-1, 1]

    return image

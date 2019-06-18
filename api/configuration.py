###########################
# ### General constants ###
###########################

# Shape of the dataset and generator output images.
IMG_SHAPE = (56, 56)

# Number of channels of the dataset and generator output images.
N_CHANNELS = 3

# Dataset batch size
BATCH_SIZE = 256

# Last epoch during previous training (in case training
# has continued from the checkpoint).
LAST_EPOCH = 0

# How many epochs should train last.
EPOCHS = 500000

# Debug logging
DEBUG_LOG = False

###################################
# ### Dataset related constants ###
###################################

# Root path to the dataset
DATASET_PATH = "dataset"

# How many classes will be used for training.
MAX_CLASSES = -1

# How many samples should be used from each class.
MAX_SAMPLES_PER_CLASS = -1

#################################
# ### Model related constants ###
#################################

# Noise size for the input of the Generator model.
GEN_NOISE_INPUT_SHAPE = 100

#######################################################
# ### Metrics/Logging and Caching related constants ###
#######################################################

# Defines an interval for saving checkpoints based on epochs.
CKPT_SAVE_INTERVAL = 100

# Defines an interval for saving generator image samples based on epochs to the local disk.
LC_GEN_SAMPLE_SAVE_INTERVAL = 100

# Defines an interval for saving generator image samples based on epochs to the TensorBoard.
TB_GEN_SAMPLE_SAVE_INTERVAL = 100

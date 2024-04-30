#%%
import os
import warnings

import numpy as np
import PIL
import tensorflow as tf
tf.random.set_seed(73)
# from IPython.display import Image, display
# from keras.utils.vis_utils import plot_model
from PIL import ImageOps
from skimage.io import imsave
from tensorflow import keras
from tensorflow.keras import layers
from metrics import f1_m
from utils1 import read_dataset, reshape_target, collapse_dim, write_imgs
from losses import weighted_cce
weights = np.array([1, 15])


# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"      # To disable using GPU
tf.get_logger().setLevel('INFO')
tf.autograph.set_verbosity(1)
warnings.filterwarnings('ignore')

def get_model_unet(img_size, num_classes):
    inputs = keras.Input(shape=img_size + (1,))

    prev_layers = {}
    ### [First half of the network: downsampling inputs] ###

    # Entry block
    x = layers.Conv2D(32, 3, padding="same")(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)
    prev_layers[32] = x

    x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

  
    for filters in [64, 128, 256]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        prev_layers[filters] = x

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

    ### [Second half of the network: upsampling inputs] ###

    for filters in [256, 128, 64, 32]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.UpSampling2D(2)(x)
        residual = prev_layers[filters]
        x = layers.concatenate([residual, x])  # Add back residual

    # Add a per-pixel classification layer
    outputs = layers.Conv2D(num_classes, 1, activation="softmax", padding="same")(x)

    # Define the model
    model = keras.Model(inputs, outputs)
    return model



# Free up RAM in case the model definition cells were run multiple times
keras.backend.clear_session()

x_train, x_test, y_train, y_test, names_train, names_test = read_dataset()
y_train_r, y_test_r = reshape_target(y_train), reshape_target(y_test)

# write_imgs(x_test, names_test, '/home/mt0/22CS60R40/UNet-Skeletonization/my_version/test_shapes')
# write_imgs(y_test, names_test, '/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Y_target')
#%%
img_size = (256,256)
num_classes = 2
batch_size = 32
# Build model
model1 = get_model_unet(img_size, num_classes)
model2 = get_model_unet(img_size, num_classes)

# model1.compile(optimizer="adam", loss=weighted_cce(weights), metrics=[f1_m])
# model2.compile(optimizer="adam", loss=weighted_cce(weights), metrics=[f1_m])


# callbacks1 = [
#     keras.callbacks.ModelCheckpoint("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/best_model/unet_skel_init.h5", save_best_only=True)
# ]

# callbacks2 = [
#     keras.callbacks.ModelCheckpoint("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/best_model/unet_skel_next.h5", save_best_only=True)
# ]

# # Train the model, doing validation at the end of each epoch.
# epochs = 3

# #%%


# model1.fit(x_train, y_train_r, epochs=epochs, validation_data=(x_test,y_test_r), callbacks=callbacks1, batch_size=32)
model1 = keras.models.load_model('/home/mt0/22CS60R40/UNet-Skeletonization/my_version/best_model/unet_skel_init.h5', custom_objects={"f1_m": f1_m, "loss": weighted_cce(weights)})

#%%

x_train_new = model1.predict(x_train)
x_test_new = model1.predict(x_test)

x_train_new = collapse_dim(x_train_new)
x_test_new = collapse_dim(x_test_new)


# model2.fit(x_train_new, y_train_r, epochs=epochs, validation_data=(x_test_new, y_test_r), callbacks=callbacks2, batch_size=32)


model2 = keras.models.load_model('/home/mt0/22CS60R40/UNet-Skeletonization/my_version/best_model/unet_skel_next.h5', custom_objects={"f1_m": f1_m, "loss": weighted_cce(weights)})

Y = model2.predict(x_test_new)

write_imgs(Y, names_test, '/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Y_pred_new', collapse=True)


# %%

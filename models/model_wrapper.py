import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import time

import tensorflow as tf
from tensorflow import keras
from keras._tf_keras.keras.preprocessing import image_dataset_from_directory
from keras._tf_keras.keras.callbacks import Callback, CSVLogger

from . import model

def process(image, label):
    image = tf.image.rgb_to_grayscale(image)
    image = tf.cast(image, tf.float32) / 255.0
    label = tf.one_hot(label, depth=9)
    return image, label

def model_wrapper(train=False, model_path=None, use_mnist = False):
    if model_path:
        return tf.keras.models.load_model(model_path)

    my_model = model.get_model()

    # if wts_path:
    #     my_model.load_weights(wts_path)

    if train:
        # gpus = tf.config.experimental.list_physical_devices('GPU')
        # for gpu in gpus:
        #     tf.config.experimental.set_memory_growth(gpu,True)

        
        # defining the callbacks
        class myCallback(Callback):
            def on_epoch_end(self, epoch, logs={}):
                logs['val_loss'], logs['val_accuracy'] = my_model.evaluate(val_ds)
                if logs.get('accuracy') > 0.995 and logs.get('val_accuracy') > 0.995:
                    print('Stopping training')
                    my_model.stop_training = True

        callbacks = [myCallback(),CSVLogger('training.log')]


        # defining the datasets
        if use_mnist:
            mnist = tf.keras.datasets.mnist

            (x_train, y_train), (x_test, y_test) = mnist.load_data()

            # normalize the data
            x_train = x_train / 255.0
            x_test = x_test / 255.0
        else:
            batch_size = 16
            img_height = 32
            img_width = 32
            data_dir = "D:\Sudoku_Solver\dataset"

            train_ds, val_ds = image_dataset_from_directory(
                                data_dir,
                                validation_split=0.2,
                                subset="both",
                                seed=123,
                                image_size=(img_height, img_width),
                                batch_size=batch_size
                            )
            
            train_ds = train_ds.map(process)
            val_ds = val_ds.map(process)

            # x_train = train_ds.map(lambda image, label: image)
            # y_train = train_ds.map(lambda image, label: label)

            # x_val = val_ds.map(lambda image, label: image)
            # y_val = val_ds.map(lambda image, label: label)
            


        my_model.fit(train_ds, epochs=11, callbacks=[callbacks])
        print(my_model.evaluate(val_ds))

        # if wts_path:
        # my_model.save_weights('{}-{}'.format(wts_path, round(time.time())))
        my_model.save('new_model.hdf5')
        # else:
        #     my_model.save_weights(to_save_as)
        return 1 
    return 0
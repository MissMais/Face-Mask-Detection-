import tensorflow as tf
from tensorflow.keras.models import load_model

def load_and_preprocess_image(path, value):
    if value == 'button1':
        img = tf.keras.preprocessing.image.load_img(path, target_size=(128, 128))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)
        img = img / 255.0
        return img
    elif value == 'button2':
        resized_img = tf.image.resize(path, (128, 128))
        img = tf.expand_dims(resized_img, axis=0)
        img = img / 255.0
        return img

def prediction(image, value):
    processed_img = load_and_preprocess_image(image, value)
    model = load_model("my_model.h5")
    Class = model.predict(processed_img)  
    return Class
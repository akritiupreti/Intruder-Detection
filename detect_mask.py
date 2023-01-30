import numpy as np
import tensorflow as tf
import cv2


def detect(frame):

    model = tf.keras.models.load_model("Model/mainModel.h5")

    frame = tf.image.resize(frame, (180,180))
    img_array = tf.keras.utils.img_to_array(frame)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    confidence = np.max(score)*100
    if confidence > 70:
        return True

    return False


if __name__ == '__main__':
    pass


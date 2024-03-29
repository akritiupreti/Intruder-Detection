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


    #labels = [['with_helmet', 'with_mask', 'without_mask']]
    #y_classes = predictions.argmax(axis=-1)
    #label = sorted(labels)[y_classes]
    confidence = np.max(score)*100
    #print(confidence, label)
    if confidence >= 95:
        return True

    return False


if __name__ == '__main__':
    pass
    #img = cv2.imread('face images/without_mask/maksssksksss51.png')
    #print(detect(img))


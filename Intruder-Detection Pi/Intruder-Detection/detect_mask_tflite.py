import tflite_runtime.interpreter as tflite
import cv2
import numpy as np


def detect(frame):
    model = tflite.Interpreter(model_path="Model/tfliteModel.tflite")
    model.allocate_tensors()

    input_details = model.get_input_details()
    output_details = model.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    input_mean = 127.5
    input_std = 127.5

    frame = cv2.resize(frame,(width,height))
    input_data = np.expand_dims(frame, axis=0)
    input_data = (np.float32(input_data) - input_mean) / input_std

    model.set_tensor(input_details[0]['index'], input_data)
    model.invoke()

    outname = output_details[0]['name']
    if ('StatefulPartitionedCall' in outname): # This is a TF2 model
        scores_idx = 0
    else:
        scores_idx = 2
        
    score = model.get_tensor(output_details[scores_idx]['index'])[0]
    confidence = np.max(score)*100

    if confidence >= 99:
        return True

    return False

if __name__ == '__main__':
    pass
    #frame = cv2.imread('2.jpg')
    #print(detect(frame))

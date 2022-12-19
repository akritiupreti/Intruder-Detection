import face_recognition
import cv2
import os

files = os.listdir('faces')
print(files)
'''
img = cv2.imread('faces/cum.jpg')
cum = face_recognition.face_encodings(img)[0]

rec = cv2.VideoCapture(0)
ret, frame = rec.read()

unknown = face_recognition.face_encodings(frame)[0]
#print(unknown[0])
result = face_recognition.compare_faces([cum],unknown)
print(result)
'''

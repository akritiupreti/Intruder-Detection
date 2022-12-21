import face_recognition
import cv2

img = cv2.VideoCapture(0)
ret, frame = img.read()

landmarks = face_recognition.face_landmarks(frame)[0]

points = landmarks['chin'] + landmarks['top_lip'] + landmarks['bottom_lip']

for point in points:
    cv2.circle(frame,point,1,(0,255,0))

cv2.imshow('Camera', frame)
cv2.waitKey(0)


print(landmarks)


import cv2
import face_recognition

rec = cv2.VideoCapture(0)

while True:
    ret, frame = rec.read()
    face = face_recognition.face_landmarks(frame)
    points = face[0]['chin'] + face[0]['left_eye'] + face[0]['nose_tip'] + face[0]['nose_bridge'] + face[0]['right_eye']
    #points2 = face[0]['left_eye']

    for point in points:
        cv2.circle(frame,point,1,(0,255,0))

    #for point in points2:
    #    cv2.circle(frame,point,1,(0,0,255))

    cv2.imshow('akriti', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

rec.release()
cv2.destroyAllWindows()
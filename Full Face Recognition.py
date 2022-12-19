import cv2
import face_recognition
import os

rec = cv2.VideoCapture(0)
photos = os.listdir('faces')

result = False
name = ""
unknown = []
frame = []

# when motion is detected, camera opens
while len(unknown) == 0:
    ret, frame = rec.read()

    cv2.imshow('Camera', frame)
    try:    # if no face is detected after camera opens, keep camera ON
        unknown = face_recognition.face_encodings(frame)[0] # when face is detected, unknown is not empty, so loop ends
    except:
        pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.imshow('Face', frame) # Display face of intruder
cv2.waitKey(0)

# now, compare the unknown face with the registered known faces
for photo in photos:
    img = cv2.imread('faces/'+photo)
    known = face_recognition.face_encodings(img)[0]

    result = face_recognition.compare_faces([known], unknown)[0]

    if result:
        name = photo[:-4]
        break


if result:
    print('Hello ' + name + '!')
else:
    print('ALARM BAJAIDIYO')

rec.release()
cv2.destroyAllWindows()
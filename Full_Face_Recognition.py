import cv2
import face_recognition
import os
import sendEmail
import detect_mask
import time


rec = cv2.VideoCapture(0, cv2.CAP_DSHOW)
photos = os.listdir('faces')

result = False
name = ""
unknown = []
frame = []
isHome = True


# when motion is detected, camera opens
while len(unknown) == 0:
    ret, frame = rec.read()

    try:    # if no face is detected after camera opens, keep camera ON
        unknown = face_recognition.face_encodings(frame)[0] # when face is detected, unknown is not empty, so loop ends
        print("face detected")
    except:
        if detect_mask.detect(frame):
            for x in range(5,0,-1):
                print("Please remove your mask/helmet in", x)
                time.sleep(1)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


cv2.imshow('Face', frame) # Display face of intruder
time.sleep(5)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
    print("Open gate")
else:
    cv2.imwrite('intruder/intruder.jpg', frame) #saves image in intruder folder to send via email
    sendEmail.run()
    if isHome:
        friendly = input('Do you know this person? (Y/N): ')
        if friendly.upper() == 'Y':
            answer = input('Do you want to register this person? (Y/N): ')
            if answer.upper() == 'Y':
                new_name = input("Enter the person's name: ")
                new_name = 'faces/' + new_name + '.jpg'
                cv2.imwrite(new_name, frame)

            print('Open gate')
        else:
            print('Gate is still closed')
    else:
        print('Alarm bajaidiyo')

rec.release()
cv2.destroyAllWindows()
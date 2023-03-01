import cv2
import face_recognition
import os
import sendEmail
import detect_mask
import time


rec = cv2.VideoCapture(0)
photos = os.listdir('faces')

result = False
name = ""
unknown = []
isHome = False

# when motion is detected, camera opens
ret, frame = rec.read()
detected = detect_mask.detect(frame)
if detected:
    for sec in range(5, 0, -1):
        print("Please remove your mask/helmet in", sec)
        time.sleep(1)

    ret, frame = rec.read()
    time.sleep(3)
    detected = detect_mask.detect(frame)

    if detected:
        print("Alarm bajaidyo")  # after making the code into a function so that main.py can import, add 'return 1' here to sound the alarm
        quit()  # remove this after adding return 1

while len(unknown) == 0:
    ret, frame = rec.read()
    try:    # if no face is detected after camera opens, keep camera ON
        unknown = face_recognition.face_encodings(frame)[0] # when face is detected, unknown is not empty, so loop ends
        print("face detected")
    except:
        time.sleep(3)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break


cv2.imshow('Face', frame)  # Display face of person in camera
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
    print("Open gate")  # add return 0
else:
    cv2.imwrite('intruder/intruder.jpg', frame)  # saves image in intruder folder for later use/to send via email
    if isHome:  # if owner is home
        friendly = input('Do you know this person? (Y/N): ')
        if friendly.upper() == 'Y':
            answer = input('Do you want to register this person? (Y/N): ')
            if answer.upper() == 'Y':
                new_name = input("Enter the person's name: ")
                new_name = 'faces/' + new_name + '.jpg'
                cv2.imwrite(new_name, frame)

            print('Open gate')  # add return 0
        else:
            print('Gate is still closed')  # add return -1 because gate is closed yet alarm is not sounded
    else:  # if owner is not home
        sendEmail.run()
        print("Owner is not home.")
        rec.release()

        rec = cv2.VideoCapture(0)
        for x in range(10,0,-1):
            print("Please leave in", x)
            time.sleep(1)

        ret, frame = rec.read()  # check if the person has left
        try:
            repeat = face_recognition.face_encodings(frame)
            if face_recognition.compare_faces([repeat], unknown):
                print("Alarm bajaidiyo")  # add return 1
        except:
             pass


rec.release()
cv2.destroyAllWindows()

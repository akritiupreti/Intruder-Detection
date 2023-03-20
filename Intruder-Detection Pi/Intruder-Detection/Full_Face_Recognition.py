import cv2
import face_recognition
import os
import sendEmail
#import detect_mask
import time
#from host import Host


def run(isHome, credentials):
    rec = cv2.VideoCapture(0)
    photos = os.listdir('faces')

    result = False
    name = ""
    unknown = []
    frame = []

    # when motion is detected, camera opens
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
        rec.release()
        cv2.destroyAllWindows()
        return 0
    else:
        cv2.imwrite('intruder/intruder.jpg', frame)  # saves image in intruder folder for later use/to send via email
        flag, name = sendEmail.run(isHome, credentials)
        if isHome:  # if owner is home
            if flag == "00":
                print("Gate is still closed")
                return -1
            elif flag == "10":
                print("Open gate")
                return 0
            else:
                new_name = "faces/" + name + ".jpg"
                cv2.imwrite(new_name, frame)
                print("Face registered! Open gate")
                return 0

        else:  # if owner is not home
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
                    rec.release()
                    cv2.destroyAllWindows()
                    return 1
            except:
                 pass


    rec.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    #isHome = Host()
    #isHome = isHome.getStatus()
    #print("Done!")
    #run(isHome)
    
    pass

import os
import xml.etree.ElementTree as ET
import cv2
import random


def cropandstore(filename, status, box):
    xmin,xmax,ymin,ymax = box
    os.chdir("Face Mask Detection/images")
    img = cv2.imread(filename)
    crop = img[ymin:ymax, xmin:xmax]
    cv2.imshow("img",crop)

    os.chdir("..")
    os.chdir("..")
    if status == "with_mask" or status == "mask_weared_incorrect":
        os.chdir("face images/with_mask")
        if filename in os.listdir():
            filename = filename[:-4] + str(random.randint(1000,10000)) + ".png"
        cv2.imwrite(filename, crop)
    else:
        os.chdir("face images/without_mask")
        cv2.imwrite(filename, crop)

    os.chdir("..")
    os.chdir("..")


def segregate():
    count = 1
    for file in os.listdir("Face Mask Detection/annotations"):
        with open("Face Mask Detection/annotations/" + file, 'r') as f:
            data = f.read()
        tree = ET.parse("Face Mask Detection/annotations/"+file)
        root = tree.getroot()

        for object in root.findall('object'):
            status = object.find('name')
            if status is not None:
                status = status.text
                filename = root.find('filename').text
                bndbox = object.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                xmax = int(bndbox.find('xmax').text)
                ymin = int(bndbox.find('ymin').text)
                ymax = int(bndbox.find('ymax').text)
                cropandstore(filename, status, (xmin,xmax,ymin,ymax))

        print(count, "image done")
        count += 1


segregate()
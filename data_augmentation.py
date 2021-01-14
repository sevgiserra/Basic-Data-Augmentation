from cv2 import cv2
import numpy as np
import os

def crop_image(image, width, height):

    max_x = image.shape[0] - width
    max_y = image.shape[1] - height

    x = np.random.randint(0,max_x)
    y = np.random.randint(0,max_y)

    crop = image[x:x+width , y:y+height]
    cropped_image = cv2.resize(crop, (500,500))
    return cropped_image

#change path
path = '/home/sevgi/Desktop/images2/'

mylist = os.listdir(path)
len = len(mylist)
for i in range (len):

    img = cv2.imread(path+mylist[i])
    os.rename(path+mylist[i],path+'image'+str(i)+'.jpg')

    for y in range (-3,0): #started from -3 so it wont get mixed up from the 0 1 2.. numbers from the i variable when labelling the image

        flipped_image = cv2.flip(img,y+2)
        flipped_name = path + 'flipped'+ str(i) + str(y) + '.jpg'
        cv2.imwrite(flipped_name,flipped_image)

        cropped_image = crop_image(img,100,100)
        cropped_name = path + 'cropped' + str(i) + str(y) + '.jpg'
        cv2.imwrite(cropped_name,cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
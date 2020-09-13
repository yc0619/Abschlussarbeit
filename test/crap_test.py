import cv2

img = cv2.imread('/home/chao/MA_Dataset/Test_1.png')
print(img.shape)
cropped_1 = img[0:2048,0:2048]
cv2.imwrite("/home/chao/MA_Dataset/1_1.png",cropped_1)


import cv2
import os

input_dir = '/home/chao/MA_Dataset/1_Messung/'
output_dir = '/home/chao/MA_Dataset/2_Verarbeitet/'

size = 2048
step = int(0.8 * size)


for filename in os.listdir(input_dir):
    filename_old = str(filename).split('.')[0]
    file = input_dir + filename

    img = cv2.imread(file)
    h_img, w_img = img.shape[0], img.shape[1]

    counter = 1
    i, j = 0, 0
    counter_i, counter_j = 1, 1  #counter_i: column counter_j: line

    # cut the image with defined size and step
    while j + size < w_img:
        while i + size < h_img:
            cropped = img[i:i+size, j:j+size]
            filename_new = filename_old + '_' + str(counter_j) + '_' + str(counter_i) + '.png'
            cv2.imwrite(output_dir + filename_new, cropped)
            i = i + step
            counter_i = counter_i + 1
        i = 0
        counter_i = 1
        j = j + step
        counter_j = counter_j + 1
    print(filename, 'COMPLETE')
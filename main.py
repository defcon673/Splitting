import numpy as np
import numpy as numpy
import cv2
import sys

windowsize_r = 32
windowsize_c = 32

#format for running
#python main [name of image]
#!!! I don't made any checks of missing argument
path = sys.argv[1]
print(path)
img = cv2.imread(path, 1)
img_split = str(sys.argv[1]).split('.')
gray = img
i = 0
for r in range(0, gray.shape[0] - windowsize_r, windowsize_r):
    for c in range(0, gray.shape[0] - windowsize_c, windowsize_c):
        window = gray[r:r+windowsize_r, c:c+windowsize_c]
        cv2.imwrite(img_split[0] + "_negative" + str(i) + "." + img_split[1], window);
        i += 1

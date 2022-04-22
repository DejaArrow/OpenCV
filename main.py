import cv2 as cv
from cv2 import rectangle
import numpy as np
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

haystack_img =  cv.imread('haystack.png', cv.IMREAD_UNCHANGED)
needle_img =  cv.imread('needle.png', cv.IMREAD_UNCHANGED)

needle_w = needle_img.shape[1]
needle_h = needle_img.shape[0]

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
print(result)

threshold = 0.5
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))
#print(locations)

rectangles = []

for loc in locations:
    rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
    rectangles.append(rect)
    rectangles.append(rect)

rectangles, weights = cv.groupRectangles(rectangles, 1, 0.3)
print(rectangles)

if len(rectangles):
    
    counting = 0
    for rectangle in rectangles:
        print (rectangle)
        counting+=1
    print ("The number of stitches found: " , counting)
    
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:
        top_left =  (x, y)
        bottom_right = (x + w, y + h)

        cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

    
    cv.imshow('Matches', haystack_img)
    cv.waitKey()

else:
    print('Stitches not found')








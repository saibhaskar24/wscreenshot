import cv2 as cv
from wscreenshot import Screenshot
import wscreenshot
k = Screenshot()
wscreenshot.list_window_names()
x = k.screenshot()
cv.imshow('My Screenshot', x)
cv.waitKey(0)
cv.destroyAllWindows()
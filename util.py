import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)[0][0]
    hue = hsv_color[0]

    lower_limit = np.array(
        [max(hue - 10, 0), 100, 100],
        dtype=np.uint8
    )

    upper_limit = np.array(
        [min(hue + 10, 179), 255, 255],
        dtype=np.uint8
    )

    return lower_limit, upper_limit

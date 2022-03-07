import cv2
import numpy as np

from . import selenium_info as driver_info

def greenscreen(image_dir):
    image = cv2.imread(image_dir)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    # defining range to excloude the green color from the image 
    # the list contain -> [ value of the Red, value of the Green, value of the Blue
    lower_range = np.array([0, 12, 0, 255])
    upper_range = np.array([180, 255, 10, 255])
    
    # form [ (0 ->110) for Red, (100 -> 255) for Green, ...] 
    mask = cv2.inRange(image, lower_range, upper_range)
    # set all other areas to zero except where mask area 
    image[mask != 0] = [0, 0, 0, 0]

    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
    cv2.imwrite(image_dir, image)

def screenshot(path):
    driver_info.driver.save_screenshot(path)
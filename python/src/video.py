import cv2
import os
def init_video():
    global image_folder
    image_folder = os.path.join("output", "cache")

    global video_name
    video_name = os.path.join("output",'video.mov')

def getAmountOfImages():
    images = 0
    for img in os.listdir(image_folder):
        if img.endswith(".png"): images += 1
    return images - 1

def generateVideo():
    frame = cv2.imread(os.path.join(image_folder, '0.png'))
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'MPEG')
    video = cv2.VideoWriter(video_name, fourcc, 1, (width,height))

    for i in range(0, getAmountOfImages()):
        video.write(cv2.imread(os.path.join(image_folder, str(i) + '.png')))

    cv2.destroyAllWindows()
    video.release()


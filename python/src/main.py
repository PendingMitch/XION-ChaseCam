from utils.selenium_info import init as selenium_init
from utils.file_management import clearCache
from frames import getScreenshots
from video import init_video, generateVideo

if __name__ == "__main__":
    selenium_init()
    clearCache()
    getScreenshots()

    init_video()
    generateVideo()
    clearCache()

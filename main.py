import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import pyautogui as pg
import numpy as np
video = VideoWriter('recordered.mp4', VideoWriter_fourcc(*'MP42'), 7, (1366, 768))
while True:
    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    video.write(screenshot)
    if cv2.waitKey(1) & 0xFF == 27: break
cv2.destroyAllWindows()
video.release()
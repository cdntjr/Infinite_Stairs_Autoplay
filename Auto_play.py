import pyautogui as pag 
import cv2, mss
import numpy as np 
import time


# 특정 부분의 픽셀을 추출해서 RGB값을 비교
left_stairs_pos = {'left': 1311, 'top': 1129, 'width': 1, 'height': 1}
right_stairs_pos = {'left': 1620, 'top': 1129, 'width': 1, 'height': 1}

turn_button = [1098, 1537]
up_button = [1761, 1537]


direction = 0  # 0: left  1: right
pag.PAUSE = 0.06


def screenshot_stair(pos):
    with mss.mss() as sct:
        stairs = np.array(sct.grab(pos))[:, :, :3]
    return stairs


# 최초 실행 
time.sleep(2)
pag.click(up_button[0], up_button[1])
pag.moveTo(x=1430, y=1537, duration=0.0)
time.sleep(0.5)
basic_stairs = screenshot_stair(left_stairs_pos)

while True:

    if direction == 0:
        stairs = screenshot_stair(left_stairs_pos)
    elif direction == 1:
        stairs = screenshot_stair(right_stairs_pos)
    

    if np.all(basic_stairs == stairs):
        #time.sleep(0.01)
        pag.click(up_button[0], up_button[1], duration=0.0)
        pag.moveTo(x=1430, y=1537, duration=0.0)
    else:
        if direction == 0: # 현재 방향이 왼쪽일 때
            stairs = screenshot_stair(right_stairs_pos)
            if np.array_equal(basic_stairs, stairs): # 오른쪽에 계단이 있는가?
                direction = 1 # 방향 오른쪽으로 변경
                pag.click(turn_button[0], turn_button[1], duration=0.0)
                pag.moveTo(x=1430, y=1537, duration=0.0)

        if direction == 1: # 현재 방향이 오른쪽일 때
            stairs = screenshot_stair(left_stairs_pos)
            if np.array_equal(basic_stairs, stairs): # 왼쪽에 계단이 있는가?
                direction = 0 # 방향 왼쪽으로 변경
                pag.click(turn_button[0], turn_button[1], duration=0.0)
                pag.moveTo(x=1430, y=1537, duration=0.0)

    
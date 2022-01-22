import time
import pyautogui


while(True):
  result = pyautogui.position()
  x,y = result

  print('X :',x,'Y : ',y)
  time.sleep(1)


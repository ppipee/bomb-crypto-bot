import pyautogui
import time
import json
import keyboard

MIN = 60 
SEC = 1

class BombCryptoAutoClick:
  def __init__(self,config):
    self.config = config
    self.ttl = config['ttl']
    self.sleep_timer = config['sleep']
    pass

  def is_stop(self):
    try:
      if(keyboard.is_pressed('q')):
        return True
      return False
    except:
      return False
      

  def click_button(self,position):
    try:
      pyautogui.moveTo(position['x'],position['y'])
      pyautogui.click() 
      pyautogui.click() 

      return True

    except:
      return False

  def active_hero(self):
    state = {
      'arrow' : False,
      'hero' : False,
      'all' : False,
      'close' : False,
      'coin' : False,
    }

    ttl = self.ttl

    while(ttl>0):
      should_continue = False
      ttl_displayed = self.ttl - ttl +1
      print('## active hero (', ttl_displayed,')')

      for key in state:
        passed = self.click_button(self.config[key])

        if(not state[key] and passed):
          state[key] = True
          time.sleep(self.config[key]['delay'])
        else:
          ttl -=1
          should_continue = True
          break

      if(should_continue):
        continue

      if(state['coin'] == True):
        break

    return ttl == 0

  def sleep(self):
    print('## sleep')
    off_set = 10

    for timer in range(self.sleep_timer * off_set):
      time.sleep(MIN/off_set)

      time_counter = self.sleep_timer * off_set - timer

      print('## - timer:',time_counter / off_set,'( ',time_counter * 6,' sec )')
      
      # if(self.is_stop()):
      #   return True

    return False

  def start(self):
    while(True):
      self.active_hero()
      should_stop = self.sleep()

      if(should_stop):
        break



if __name__ == '__main__':
  print('## start!')

  file_config = open('./config.json')
  config = json.load(file_config)
  file_config.close()

  autoClick = BombCryptoAutoClick(config)
  autoClick.start()

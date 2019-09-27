from pynput.mouse import Button, Controller
import time, datetime

mouse = Controller()
#print("The current mouse position is {0}".format(mouse.position))

def get_time_now():
  now = datetime.datetime.now()
  return now.strftime("%H:%M:%S")

main_menu = [1195, 1055]
logout = [952, 609]
enter_world = [962, 994]
select_mjolnir = [1683, 150]
select_dropbox = [1665, 394]

select_mograine = [679, 300]
choose_realm = [1121, 858]

def single_click():
  mouse.press(Button.left)
  mouse.release(Button.left)

def double_click():
  single_click()
  single_click()

def open_main_menu():
  print("{0} - Opening Main Menu...".format(get_time_now()))
  #place mouse over main menu button and press
  mouse.position = (main_menu[0], main_menu[1])
  single_click()


def press_logout():
  print("{0} - Logging out of character...".format(get_time_now()))
  #place mouse over logout and press
  mouse.position = (logout[0], logout[1])
  single_click()
  time.sleep(5)

def press_dropbox():
  print("{0} - Selecting character Dropbox...".format(get_time_now()))
  mouse.position = (select_dropbox[0], select_dropbox[1])
  double_click()

def press_mjolnir():
  print("{0} - Selecting character Mjolnir...".format(get_time_now()))
  mouse.position = (select_mjolnir[0], select_mjolnir[1])
  double_click()

def press_enter_world():
  print("{0} - Entering world...".format(get_time_now()))
  #place mouse over enter world and press
  mouse.position = (enter_world[0], enter_world[1])
  double_click()

def reset_afk():
  open_main_menu()
  time.sleep(2)
  press_logout()
  time.sleep(10)
  press_enter_world()

#reset_afk()
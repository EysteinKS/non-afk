from pywinauto import application, findwindows
from PIL import Image, ImageGrab
from config import app_path
import datetime

def get_time_now():
  now = datetime.datetime.now()
  return now.strftime("%H:%M:%S")


class WindowManager:
  def __init__(self):
    self.app = application.Application()
    self.window = None

  def connect(self):
    try:
      self.app.connect(path=r"X:\Spill\World of Warcraft\_classic_\Wow.exe")
      self.window = self.app["World of Warcraft"]
    except:
      print("{0} - Unable to connect to app!".format(get_time_now()))
    finally:
      print("{0} - App connected!".format(get_time_now()))


  def focus(self):
    self.window.set_focus()  

  def capture_screen(self):
    print("{0} - Capturing screen...".format(get_time_now()))
    self.focus()
    box = (0, 0, 1920, 1080)
    ImageGrab.grab(box).save("screen.png")

  def get_color_at_pixel(self, x, y):
    img = Image.open("screen.png")
    img_as_rgb = img.convert("RGB")
    pixel = img_as_rgb.getpixel((x, y))
    return pixel


"""
window = WindowManager()
process_id = input("Process id?: ")
window.connect(process_id, "World of Warcraft")
window.focus()
window.capture_screen()
"""
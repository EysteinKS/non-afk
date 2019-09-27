from application import WindowManager
from mouse import enter_world

enter_world_pixel = (962, 994)
enter_world_color = (255, 199, 0)

def check_if_logged_in(window):
  window.capture_screen()
  pixel_color = window.get_color_at_pixel(962, 994)

  if sorted(pixel_color) == sorted(enter_world_color):
    return True
  else:
    return False

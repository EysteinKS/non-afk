from application import WindowManager
from login_after_queue import check_if_logged_in
import sched, time, random, datetime
from mouse import press_enter_world, press_dropbox, reset_afk, press_mjolnir


#TODO
#CHECK FOR COLORS WHEN PRESSING BUTTONS
#LEARN BUTTON LOCATIONS FOR EACH CHARACTER
#CHECK IF DISCONNECTED
#LEARN TO RESTART GAME IF DISCONNECTED (!!)

window = WindowManager()
scheduler = sched.scheduler(time.time, time.sleep)

def get_time_now():
  now = datetime.datetime.now()
  return now.strftime("%H:%M:%S")

min_time = 900
#min_time = 10
max_time = 1200
#max_time = 20

def initialize():
  print("--NON-AFK: Queued--")
  print("{0} - Initializing...".format(get_time_now()))
  window.connect()

def check_task(sc):
  is_logged_in = check_if_logged_in(window)
  if is_logged_in:
    print("{0} - You're logged in! Starting task".format(get_time_now()))
    window.focus()
    press_dropbox()
    press_enter_world()
    task_time = random.randint(min_time, max_time)
    print("Next task running in {0} seconds".format(task_time))
    scheduler.enter(task_time, 1, non_afk_task, (sc,))
  else:
    print("{0} - Still in queue...".format(get_time_now()))
    scheduler.enter(min_time, 1, check_task, (sc,))

def non_afk_task(sc):
  print("{0} - Running task...".format(get_time_now()))
  window.focus()
  press_dropbox()
  time.sleep(1)
  reset_afk()
  task_time = random.randint(min_time, max_time)
  print("Next task running in {0} seconds".format(task_time))
  scheduler.enter(task_time, 1, non_afk_task, (sc,))

initialize()
scheduler.enter(1, 1, check_task, (scheduler,))
scheduler.run()
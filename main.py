from pynput.keyboard import Key, Controller
from apscheduler.schedulers.blocking import BlockingScheduler
from pywinauto import application, findwindows

import os
import random


scheduler = BlockingScheduler()

#Saves the process_id of World of Warcraft
class Process:
  def __init__(self):
    self.process_id = ""
  
  def set_id(self, process_id):
    self.process_id = process_id

  def get_id(self):
    return self.process_id

#Saves the id of the current job
class Job:
  def __init__(self):
    self.job_id = ""

  def set_id(self, job_id):
    self.job_id = job_id
  
  def get_id(self):
    return self.job_id

process = Process()
job = Job()

def get_random_key():
  keys = ["w", "s", Key.space]
  key = random.randint(0, 2)
  return keys[key]


def press_key(key):
  keyboard = Controller()
  print("Pressing key ", key)
  keyboard.press(key)
  keyboard.release(key)

def focus_window():
  app = application.Application()
  id = process.get_id()
  print("process id: ", id)
  print(application.process_module(id))
  app.connect(process=id)
  app["World of Warcraft"].set_focus()


def focus_window_and_press_key():
  focus_window()
  keyToPress = get_random_key()
  press_key(keyToPress)
  start_new_job()


def get_interval_time():
  time = random.randint(60, 290)
  print("Job interval is {0} seconds".format(time))
  return time

def add_scheduler_job():
  jobid = scheduler.add_job(focus_window_and_press_key, "interval", seconds=get_interval_time())
  id = jobid.id
  job.set_id(id)

def start_new_job():
  old_job = job.get_id()
  scheduler.remove_job(old_job)
  add_scheduler_job()
  print("Starting new job")

def run_scheduler():
  add_scheduler_job()
  print("Press CTRL+{0} to exit".format("Break" if os.name == "nt" else "C"))

  try:
    scheduler.start()
  except(KeyboardInterrupt, SystemExit):
    pass


if __name__ == "__main__":
  process_id = input("World of Warcraft Process ID? ")
  process.set_id(process_id)
  run_scheduler()

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
COMPLETED_POMODOROS = 1
TIMER = None

MESSAGES = {
  'WELCOME': 'Welcome to the pomodoro timer!',
  'SHORT_BREAK': 'You earned a 5 minute break!',
  'WORK': 'Lets get back to work!',
  'LONG_BREAK': 'You earned a 20 minutes break!',
  'START': 'Press start!'
}

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  window.after_cancel(TIMER)
  global REPS
  REPS = 1
  canvas.itemconfig(timer_text, text='00:00')
  title_label['text'] = 'Timer'
  checkmark_label['text'] = ''
  message_label['text'] = MESSAGES['START']

  

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  work_seconds = WORK_MIN * 60
  short_break_seconds = SHORT_BREAK_MIN * 60
  long_break_seconds = LONG_BREAK_MIN * 60

  if REPS % 2 == 1:
    title_label['text'] = 'Timer'
    title_label['fg'] = GREEN
    countdown(work_seconds)
  
  if REPS % 2 == 0 and REPS < 8:
    title_label['text'] = 'Break'
    title_label['fg'] = PINK
    countdown(short_break_seconds)

  if REPS == 8:
    title_label['text'] = 'Break'
    title_label['fg'] = PINK
    countdown(long_break_seconds)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  minutes = math.floor(count/60)
  seconds = count % 60
  if minutes == 0:
    minutes = f'0{minutes}'
  if seconds <10:
    seconds = f'0{seconds}'
  canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
  if count > 0:
    global TIMER
    TIMER = window.after(1000, countdown, count-1)
  else:
    global COMPLETED_POMODOROS
    COMPLETED_POMODOROS += 1
    mark = ''
    for _ in range(math.floor(COMPLETED_POMODOROS/2)):
      mark += '✔'
    checkmark_label.config(text=mark)
    show_message()

# ---------------------------- SHOW MESSAGE ------------------------------- #

def show_message(): 
  global REPS
  REPS += 1
  if REPS % 2 == 1:
    message_label.config(text=MESSAGES['WORK'], fg=GREEN)
  
  if REPS % 2 == 0 and REPS < 8:
    message_label.config(text=MESSAGES['SHORT_BREAK'], fg=PINK)

  if REPS == 8:
    message_label.config(text=MESSAGES['LONG_BREAK'], fg=PINK)
    REPS = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.minsize(width=600, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
subtitle_label = Label(text=MESSAGES['WELCOME'], font=(FONT_NAME), fg=GREEN, bg=YELLOW)
subtitle_label.grid(column=1, row=1)

message_label = Label(text=MESSAGES['START'], font=(FONT_NAME), fg=GREEN, bg=YELLOW)
message_label.grid(column=1, row=5)

checkmark_label = Label(text='', fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

start_button = Button(text='Start', borderwidth=0, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', borderwidth=0, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

window.mainloop()
# import tkinter as tk
# from tkinter import Button
# import recorder
# def stop():
#     self.running = False

# def record():
#     running = True
#     if running:
#         with rec.open('nonblocking.wav', 'wb') as file:
#             file.start_recording()
#             if running == False:
#                 file.stop_recording()
# running = False

# button_rec = Button( text='Aufnehmen', command=record())
# button_rec.pack()

# button_stop = Button( text='Stop', command=stop())
# button_stop.pack()

# rec = recorder.Recorder(channels=2)



# root = tk.Tk()
# root.mainloop()

import tkinter as tk
import recorder

# --- functions ---

def start():
    global running

    if running is not None:
        print('already running')
    else:
        running = rec.open('nonblocking.wav', 'wb')
        running.start_recording()

def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running = None
    else:
        print('not running')

# --- main ---

rec = recorder.Recorder(channels=2)
running = None

root = tk.Tk()

button_rec = tk.Button(root, text='Start', command=start)
button_rec.pack()

button_stop = tk.Button(root, text='Stop', command=stop)
button_stop.pack()

root.mainloop() 
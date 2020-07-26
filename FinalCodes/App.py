from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
import os 
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time, threading

class Main(Screen,BoxLayout):
    pass

class Record(Screen,BoxLayout):
    def __init__(self, **kwargs):
        super(Record, self).__init__(**kwargs)
       
        
        #self.zero = 1 #or  this to be here! moved to the recording clock function tut3
        #self.display_counter = '' #No need for this! tut3
        #self.duration = 5
   
    def check_numeric(self):
        self.user_input = self.ids['user_input']
        if self.user_input.text.isdigit() == False:
            d_list = [num for num in self.user_input.text if num.isdigit()]
            self.user_input.text = "".join(d_list)

   
    def startRecording_clock(self):
        self.start_button = self.ids['start_button']
        self.stop_button = self.ids['stop_button']
        self.display_label = self.ids['display_label']
        self.switch = self.ids['duration_switch'] # Tutorial 3
        self.user_input = self.ids['user_input']
        self.mins = 0 #Reset the minutes
        self.zero = 1 # Reset if the function gets called more than once
        self.duration = int(self.user_input.text) #Take the input from the user and convert to a number
        Clock.schedule_interval(self.updateDisplay, 1)
        self.start_button.disabled = True # Prevents the user from clicking start again which may crash the program
        self.stop_button.disabled = False
        self.switch.disabled = True #TUT Switch disabled when start is pressed
       
    def stopRecording(self):
   
        Clock.unschedule(self.updateDisplay)
        self.display_label.text = 'Finished Recording!'
        self.start_button.disabled = False
        self.stop_button.disabled = True #TUT 3
        self.switch.disabled = False #TUT 3 re enable the switch
         
    def updateDisplay(self,dt):  
        if self.switch.active == False:
            if self.zero < 60 and len(str(self.zero)) == 1:
                self.display_label.text = '0' + str(self.mins) + ':0' + str(self.zero)
                self.zero += 1
               
            elif self.zero < 60 and len(str(self.zero)) == 2:
                    self.display_label.text = '0' + str(self.mins) + ':' + str(self.zero)
                    self.zero += 1
            
            elif self.zero == 60:
                self.mins +=1
                self.display_label.text = '0' + str(self.mins) + ':00'
                self.zero = 1
       
        elif self.switch.active == True:
            if self.duration == 0: # 0
                self.display_label.text = 'Recording Finished!'
                self.start_button.disabled = False # Re enable start
                self.stop_button.disabled = True # Re disable stop
                Clock.unschedule(self.updateDisplay)
                self.switch.disabled = False # Re enable the switch
               
            elif self.duration > 0 and len(str(self.duration)) == 1: # 0-9
                self.display_label.text = '00' + ':0' + str(self.duration)
                self.duration -= 1
 
            elif self.duration > 0 and self.duration < 60 and len(str(self.duration)) == 2: # 0-59
                self.display_label.text = '00' + ':' + str(self.duration)
                self.duration -= 1
 
            elif self.duration >= 60 and len(str(self.duration % 60)) == 1: # EG 01:07
                self.mins = self.duration / 60
                self.display_label.text = '0' + str(self.mins) + ':0' + str(self.duration % 60)
                self.duration -= 1
 
            elif self.duration >= 60 and len(str(self.duration % 60)) == 2: # EG 01:17
                self.mins = self.duration / 60
                self.display_label.text = '0' + str(self.mins) + ':' + str(self.duration % 60)
                self.duration -= 1

class WindowManager(ScreenManager):
    pass

class ShowDialog(Screen,BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(None, None),size=(400,400))
        self._popup.open()

    def load_list(self):
        pass

    def loaded_file(self,filename):
        self.file = filename
        print(type(self.file))
        print("loaded completed")

    def start_converting(self):
        self.pop_up = Popup(title="Loading",content=Image(source='C:/Users/p3pra/Desktop/Dproject/Final/loading.png'),size_hint=(None, None),size=(400,400))
        self.pop_up.open()
        time.sleep(2)
        self.converted_text = self.convert_real(self.file)
        self.pop_up.dismiss()



    def convert_real(self,path):
        print("Went to sleep")
        time.sleep(5)
        # r = sr.Recognizer()
        # # open the audio file using pydub
        # sound = AudioSegment.from_wav(path)  
        # # split audio sound where silence is 700 miliseconds or more and get chunks
        # chunks = split_on_silence(sound,
        #     # experiment with this value for your target audio file
        #     min_silence_len = 500,
        #     # adjust this per requirement
        #     silence_thresh = sound.dBFS-14,
        #     # keep the silence for 1 second, adjustable as well
        #     keep_silence=500,
        # )
        # folder_name = "audio-chunks"
        # # create a directory to store the audio chunks
        # if not os.path.isdir(folder_name):
        #     os.mkdir(folder_name)
        # whole_text = ""
        # # process each chunk 
        # for i, audio_chunk in enumerate(chunks, start=1):
        #     # export audio chunk and save it in
        #     # the `folder_name` directory.
        #     chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        #     audio_chunk.export(chunk_filename, format="wav")
        #     # recognize the chunk
        #     with sr.AudioFile(chunk_filename) as source:
        #         audio_listened = r.record(source)
        #         # try converting it to text
        #         try:
        #             text = r.recognize_google(audio_listened)
        #         except sr.UnknownValueError as e:
        #             #print("Error:", str(e))
        #             pass
        #         else:
        #             text = f"{text.capitalize()}. "
        #             #print(chunk_filename, ":", text)
        #             whole_text += text
        # # return the text for all chunks detected
        # return whole_text

    def update_label(self):    
        self.file = self.ids['file_label']
        self.file.text = filename
        #Clock.unschedule(self.update_label(filename))
        
    def dismiss_popup(self):
        self._popup.dismiss()

class show_converted(Screen):
    pass



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    def load_list(self, path, filename):
        a = ShowDialog()
        a.loaded_file(filename[0])

class Selection(Screen,BoxLayout):
    pass

class Summarize(Screen,BoxLayout):
    pass

class KeyPhrases(Screen,BoxLayout):
    pass

class MeetReport(Screen,BoxLayout):
    pass

kv = Builder.load_file("temp.kv")

class Mymainapp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    Mymainapp().run()
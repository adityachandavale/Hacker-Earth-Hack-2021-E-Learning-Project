import moviepy.editor as mp
import speech_recognition as sr
        
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os 

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
#root.deiconify()
root.lift()
root.focus_force()

import shutil

class main:
         
    path = filedialog.askopenfilename(parent=root)
   

    def __init__(self):
        self.video_audio()
        self.get_large_audio_transcription()
    
    def video_audio(self):
        my_clip = mp.VideoFileClip(self.path)
        my_clip.audio.write_audiofile('regression.wav')
        
    def get_large_audio_transcription(self):
            r = sr.Recognizer()
            sound = AudioSegment.from_wav("regression.wav")  

            chunks = split_on_silence(sound,min_silence_len = 500,silence_thresh = sound.dBFS-14,keep_silence=5000)
            folder_name = "audio-chunks"

            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
            whole_text = ""

            for i, audio_chunk in enumerate(chunks, start=1):

                chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
                audio_chunk.export(chunk_filename, format="wav")

                with sr.AudioFile(chunk_filename) as source:
                    audio_listened = r.record(source)

                    try:
                        text = r.recognize_google(audio_listened)
                    except sr.UnknownValueError as e:
                        print(str(e))
                    except HTTPError as er:
                        print('Recognize function error')
                    else:
                        text = f"{text.capitalize()}. "
                        #print(text)
                        whole_text += text
            txtfile=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
            txtfile.write(whole_text)
            txtfile.close()
            shutil.rmtree(folder_name)


class exec:
    a=main()
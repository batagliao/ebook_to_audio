import pyttsx3

def text_to_audio(string, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(string, output_file)
    engine.runAndWait()
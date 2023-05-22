import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = 3
speak.Volume = 100
text = "Активирую бота"

def speek_text(text):
    speak.Speak(text)
speek_text(text)

import pyttsx3, PyPDF2
from googletrans import Translator
def setVoice(speaker):
    voice=speaker.getProperty('voice')
    speaker.setProperty('voice', voice[1].id)

def setVolume(speaker):
    volume=speaker.getProperty('volume')
    speaker.setProperty('volume', 1.0)

def speechRate(speaker):
    rate=speaker.getProperty('rate')
    speaker.setProperty('rate', 150)

def savingFile(speaker):
    speaker.save_to_file('/Users/Anish/Desktop/pygame/small projects/audiobooks', 'test.mp3')

book=open('/Users/Anish/Desktop/STPH.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
speaker=pyttsx3.init()
speechRate(speaker)
#for num in range(66):
page=pdfreader.getPage(66)
text=page.extractText()
#translate_text=Translator().translate(text, dest='hi')
#print(translate_text.text)#"Im here for you"
speaker.say(text)
speaker.runAndWait()

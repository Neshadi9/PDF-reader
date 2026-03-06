import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
import PyPDF2
import pyttsx3

book = open("Pythoninterview_quns.pdf",'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfreader.getPage(5 )
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
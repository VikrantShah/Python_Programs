"""
Progrm to convert PDF file to an Audio Book.


Installing the Dependencies :

pip3 install gtts
pip install PyPDF2
"""

# Importing the libraries
from gtts import gTTS
import PyPDF2

# Getting the location fo the PDF file
pdf_file_location = input("Please enter the path of the PDF file : ").replace("\\", "/")
print(pdf_file_location)

# Getting the filename
fname = (pdf_file_location.split("/")[-1][0:-4] + ".mp3").replace(" ", "_")
print(fname)


# Creating a PDF file object
pdf_file_obj = open(pdf_file_location, "rb")

# Creating a PDF File Reader Object
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

# Getting the number of pages
pages = pdf_reader.numPages
print(pages)

# Reading the text from PDF file
text =  ""
for page in range(pages) :
	page_obj = pdf_reader.getPage(page)
	
	text += page_obj.extractText()
print(text)

# Converting the text to audio and saving it 
tts = gTTS(text = text, lang = "en")
tts.save(fname)
# Web Scraping
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to translate
url = 'https://en.wikipedia.org/wiki/Stephen_Devassy'

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text content from the webpage
text_content = ' '.join([p.get_text() for p in soup.find_all('p')])

print(text_content)

#Translation
import tkinter as tk
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Translate the content to Malayalam
desired_language = 'ml'  # Malayalam language code
translated_text = translator.translate(text_content, dest=desired_language).text

# Create a Tkinter window
root = tk.Tk()
root.title("Noto Sans Malayalam Text")

# Create a text widget and set the Noto Sans Malayalam font
text_widget = tk.Text(root, font=("Noto Sans Malayalam", 12))
text_widget.pack()

# Insert the translated text into the text widget
text_widget.insert(tk.END, translated_text)

# Start the Tkinter main loop
root.mainloop()

#Converting the extracted text to pdf
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Translate the content to your desired language
desired_language = 'ml'  # Change this to your target language code
translated_text = translator.translate(text_content, dest=desired_language).text

# Register the Noto Sans Malayalam font (you might have already done this)
pdfmetrics.registerFont(TTFont('NotoSansMalayalam', r'C:\Users\SREERAJ\Downloads\Noto_Sans_Malayalam\NotoSansMalayalam-VariableFont_wdth,wght.ttf'))  # Replace with the actual path

# Create a PDF document
doc = SimpleDocTemplate("translated_document_web.pdf", pagesize=letter)

# Define a paragraph style using the NotoSansMalayalam font
malayalam_style = getSampleStyleSheet()['Normal']
malayalam_style.fontName = 'NotoSansMalayalam'
malayalam_style.fontSize = 12
malayalam_style.leading = 14
malayalam_style.textColor = colors.black

# Create a Paragraph with the translated text and the Malayalam style
translated_paragraph = Paragraph(translated_text, style=malayalam_style)

# Build the PDF document
doc.build([translated_paragraph])


import PyPDF2
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Provide the path to your English PDF file
pdf_path = r'C:\Users\SREERAJ\OneDrive\Desktop\Languify\LinguaCraft\Subhas Chandra Bose.pdf'

# Extract English text from the PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)  # Change PdfFileReader to PdfReader
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

english_text = extract_text_from_pdf(pdf_path)

# Translate English text to Malayalam
def translate_to_malayalam(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ml')
    return translated_text.text

malayalam_text = translate_to_malayalam(english_text)

# Create a buffer for the PDF
buffer = BytesIO()

# Create a PDF document
doc = SimpleDocTemplate(buffer, pagesize=letter)

# Create a list to hold the content
story = []

# Define a Malayalam paragraph style using Noto Sans
pdfmetrics.registerFont(TTFont('NotoSansMalayalam', r'C:\Users\SREERAJ\Downloads\Noto_Sans_Malayalam\NotoSansMalayalam-VariableFont_wdth,wght.ttf'))  # Replace with the actual path
malayalam_style = ParagraphStyle(
    name='MalayalamStyle',
    fontName='NotoSansMalayalam',
    fontSize=12,
    leading=14,
    textColor=colors.black,
)

# Add the Malayalam text to the story
story.append(Paragraph(malayalam_text, malayalam_style))

# Build the PDF document
doc.build(story)

# Save the Malayalam PDF to a file
malayalam_pdf_path = 'malayalam_text.pdf'
with open(malayalam_pdf_path, 'wb') as f:
    f.write(buffer.getvalue())

print(f"Malayalam PDF saved to {malayalam_pdf_path}")
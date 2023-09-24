from flask import Flask, render_template, request, jsonify
from PIL import Image
import PyPDF2
import pytesseract
import os
import cv2
import numpy as np
from PIL import ImageEnhance
import re
import easyocr
from spellchecker import SpellChecker
from markupsafe import Markup
import html
import string
from autocorrect import Speller


app = Flask(__name__)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

spell = SpellChecker()

@app.route("/", methods=['GET', 'POST'])
def index():

    # print(0)
    if request.method == 'POST':

        file = request.files['filetopycode']
        mode = request.form['workmode']
        # print(1)
        if file:
            # print(2)

            # Save the uploaded file temporarily
            filename = file.filename
            file_path = 'temp_file' + os.path.splitext(filename)[1]
            file.save(file_path)

            mytxt=''
            highlighted_text=''
            corrected_text=''
            mytxtli = []
            hightxtli = []
            # crcttxtli = []

            # check if uploaded file is image or pdf
            if file_path.endswith('.pdf'):
                mytxtli = extract_text_from_pdf(file_path)
                result = '\n\n\n'.join(mytxtli)
                for txt in mytxtli:
                    hightxtli.append(Markup(highlight_incorrect_words(txt)))
                    # crcttxtli.append(Markup(show_corrected_only(txt)))
                resulthigh = Markup(highlight_incorrect_words(result))
                resultcrct = Markup(show_corrected_only(result))
                os.remove(file_path)
                return jsonify(extracted_texts=mytxtli, highlighted_texts=hightxtli, para=resulthigh, org=result, crct=resultcrct)

            else:
                if(mode=='default'):
                    mytxt0 = extract_text_from_image0(file_path)
                    hgtxt0 = highlight_incorrect_words(mytxt0)
                    crtxt0 = show_corrected_only(mytxt0)
                    mytxt += mytxt0
                    highlighted_text += hgtxt0
                    corrected_text += crtxt0
                
                elif(mode=='vertical'):
                    mytxt2 = extract_text_from_image2(file_path)
                    hgtxt2 = highlight_incorrect_words(mytxt2)
                    crtxt2 = show_corrected_only(mytxt2)
                    mytxt += mytxt2
                    highlighted_text += hgtxt2
                    corrected_text += crtxt2

                elif(mode=='hindi'):
                    mytxt4 = extract_text_from_image4(file_path)
                    hgtxt4 = (mytxt4)
                    crtxt4 = (mytxt4)
                    mytxt += mytxt4
                    highlighted_text += hgtxt4
                    corrected_text += crtxt4
                
                elif(mode=='distorted'):
                    mytxt5 = extract_text_from_image5(file_path)
                    hgtxt5 = (mytxt5)
                    crtxt5 = (mytxt5)
                    mytxt += mytxt5
                    highlighted_text += hgtxt5
                    corrected_text += crtxt5
                
                elif(mode=='scanned'):
                    head0 = '<strong>---------- output 0 ----------</strong>\n\n'
                    mytxt += head0
                    highlighted_text += head0
                    mytxt0 = extract_text_from_image0(file_path)
                    hgtxt0 = highlight_incorrect_words(mytxt0)
                    crtxt0 = show_corrected_only(mytxt0)
                    mytxt += mytxt0
                    highlighted_text += hgtxt0
                    corrected_text += crtxt0
                    head5 = '\n\n\n<strong>---------- output 1 ----------</strong>\n\n'
                    mytxt += head5
                    highlighted_text += head5
                    mytxt5 = extract_text_from_image5(file_path)
                    hgtxt5 = (mytxt5)
                    crtxt5 = (mytxt5)
                    mytxt += mytxt5
                    highlighted_text += hgtxt5
                    corrected_text += crtxt5
                    head4 = '\n\n\n<strong>---------- output 2 ----------</strong>\n\n'
                    mytxt += head4
                    highlighted_text += head4
                    mytxt4 = extract_text_from_image4(file_path)
                    hgtxt4 = (mytxt4)
                    crtxt4 = (mytxt4)
                    mytxt += mytxt4
                    highlighted_text += hgtxt4
                    corrected_text += crtxt4

                else:
                    head0 = '<strong>---------- output 0 ----------</strong>\n\n'
                    mytxt += head0
                    highlighted_text += head0

                    mytxt0 = extract_text_from_image0(file_path)
                    hgtxt0 = highlight_incorrect_words(mytxt0)
                    crtxt0 = show_corrected_only(mytxt0)
                    mytxt += mytxt0
                    highlighted_text += hgtxt0
                    corrected_text += crtxt0

                    head1 = '\n\n\n<strong>---------- output 1 ----------</strong>\n\n'
                    mytxt += head1
                    highlighted_text += head1

                    mytxt1 = extract_text_from_image1(file_path)
                    hgtxt1 = highlight_incorrect_words(mytxt1)
                    crtxt1 = show_corrected_only(mytxt1)
                    mytxt += mytxt1
                    highlighted_text += hgtxt1
                    corrected_text += crtxt1

                    head2 = '\n\n\n<strong>---------- output 2 ----------</strong>\n\n'
                    mytxt += head2
                    highlighted_text += head2

                    mytxt2 = extract_text_from_image2(file_path)
                    hgtxt2 = highlight_incorrect_words(mytxt2)
                    crtxt2 = show_corrected_only(mytxt2)
                    mytxt += mytxt2
                    highlighted_text += hgtxt2
                    corrected_text += crtxt2

                    head3 = '\n\n\n<strong>---------- output 3 ----------</strong>\n\n'
                    mytxt += head3
                    highlighted_text += head3

                    mytxt3 = extract_text_from_image3(file_path)
                    hgtxt3 = highlight_incorrect_words(mytxt3)
                    crtxt3 = show_corrected_only(mytxt3)
                    mytxt += mytxt3
                    highlighted_text += hgtxt3
                    corrected_text += crtxt3


                    head4 = '\n\n\n<strong>---------- output 4 ----------</strong>\n\n'
                    mytxt += head4
                    highlighted_text += head4

                    mytxt4 = extract_text_from_image5(file_path)
                    hgtxt4 = highlight_incorrect_words(mytxt4)
                    crtxt4 = show_corrected_only(mytxt4)
                    mytxt += mytxt4
                    highlighted_text += hgtxt4
                    corrected_text += crtxt4


                    head5 = '\n\n\n<strong>---------- output 5 ----------</strong>\n\n'
                    mytxt += head5
                    highlighted_text += head5

                    mytxt5 = extract_text_from_image4(file_path)
                    hgtxt5 = (mytxt5)
                    crtxt5 = (mytxt5)
                    mytxt += mytxt5
                    highlighted_text += hgtxt5
                    corrected_text += crtxt5


                    # head6 = '\n\n\n<strong>---------- output 6 ----------</strong>\n\n'
                    # mytxt += head6
                    # highlighted_text += head6

                    # mytxt6 = extract_text_from_image6(file_path)
                    # hgtxt6 = (mytxt6)
                    # crtxt6 = (mytxt6)
                    # mytxt += mytxt6
                    # highlighted_text += hgtxt6
                    # corrected_text += crtxt6

                    # mytxt += '\n\n\n---------- output 5 ----------\n\n'
                    # mytxt += extract_text_from_image5(file_path)
                
                # print on console
                print(mytxt)

                my_highlighted_text = Markup(highlighted_text)
                my_corrected_text = Markup(corrected_text)

                # print(my_highlighted_text)

                # Remove the temporary image file
                os.remove(file_path)

                return jsonify(extracted_text=mytxt, highlighted_text=my_highlighted_text, corrected_text=my_corrected_text)

    return render_template('index.html', extracted_text='your extracted text here ...')



def highlight_incorrect_words(text):
    # Replace dots and new lines with HTML entities
    text = html.escape(text).replace('.', '&#46;').replace('\n', '<br>')

    # Split the text into words
    words = re.findall(r'\w+|\S+', text)  # Split by words or non-whitespace characters

    # Initialize the spell checker
    spell_checker = Speller(lang='en')

    # Generate the HTML code with incorrect words and corrected text
    highlighted_text = ""
    for word in words:
        if word.strip() and word not in string.whitespace:  # Ignore empty and whitespace-only words
            corrected_word = spell_checker(word)
            if corrected_word != word:
                highlighted_word = f'<span class="highlighted">{word}</span> <span class="highlightedcorrect">{corrected_word}</span>'
            else:
                highlighted_word = word
            highlighted_text += highlighted_word + ' '

    return highlighted_text

def show_corrected_only(text):
    # Replace dots and new lines with HTML entities
    text = html.escape(text).replace('.', '&#46;').replace('\n', '<br>')

    # Split the text into words
    words = re.findall(r'\w+|\S+', text)  # Split by words or non-whitespace characters

    # Initialize the spell checker
    spell_checker = Speller(lang='en')

    # Generate the HTML code with incorrect words and corrected text
    highlighted_text = ""
    for word in words:
        if word.strip() and word not in string.whitespace:  # Ignore empty and whitespace-only words
            corrected_word = spell_checker(word)
            if corrected_word != word:
                highlighted_word = f'<span class="highlightedcorrect">{corrected_word}</span>'
            else:
                highlighted_word = word
            highlighted_text += highlighted_word + ' '

    return highlighted_text




# FOR PDFS
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        texts = []
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text = page.extract_text() #+ "\n\n\n"
            texts.append(text)
    return texts

# FOR IMAGES
def extract_text_from_image0(file_path):
    try:
        image = Image.open(file_path)

        # pytesseract image to string to get results
        text = str(pytesseract.image_to_string(image))
        # text = pytesseract.image_to_string(grayimg)
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text

def extract_text_from_image1(file_path):
    try:
        # image = Image.open(file_path)

        # preprocessing
        cvimg = cv2.imread(file_path)
    
        grayimg = get_grayscale(cvimg)
    
        # convert the image to black and white for better OCR
        ret,thresh1 = cv2.threshold(grayimg,120,255,cv2.THRESH_BINARY)
    
        # pytesseract image to string to get results
        text = str(pytesseract.image_to_string(thresh1, config='--oem 3 --psm 6'))
        # text = pytesseract.image_to_string(grayimg)
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text

def extract_text_from_image2(file_path):
    try:
        image = Image.open(file_path)
        # preprocessing
        cvimg = cv2.imread(file_path)
    
        # grayimg = get_grayscale(enhanced_image)
        gray_img = image.convert('L')

        # Enhance the contrast of the image
        enhancer = ImageEnhance.Contrast(gray_img)
        enhanced_image = enhancer.enhance(8.0)  # Adjust the enhancement factor as needed
    
        # pytesseract image to string to get results
        text = str(pytesseract.image_to_string(enhanced_image, config='--oem 3 --psm 6'))
        # text = pytesseract.image_to_string(grayimg)
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text

def extract_text_from_image3(file_path):
    try:
        # Load the image using OpenCV
        image = cv2.imread(file_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to create a binary image
        _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Perform image dilation
        kernel = np.ones((3, 3), np.uint8)
        dilation = cv2.dilate(threshold, kernel, iterations=1)

        # Perform image inversion
        inverted = cv2.bitwise_not(dilation)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(inverted)
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text.strip()

def extract_text_from_image4(file_path):
    try:
        reader = easyocr.Reader(['en','hi'], gpu=False)
        output = reader.readtext(file_path, detail=0)
        text = '\n'.join(output)
        # text = ' '.join([result[1] for result in output])
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text

def extract_text_from_image5(file_path):
    try:
        reader = easyocr.Reader(['en'], gpu=False)
        output = reader.readtext(file_path, detail=0)
        text = '\n'.join(output)
        # text = ' '.join([result[1] for result in output])
    except Exception as e:
        print("An exception occurred:", str(e))
        text = ""
    return text.strip()

# def extract_text_from_image6(image_path):
    # try:
    #     # Initialize the OCR tool with Tesseract as the backend
    #     tool = pyocr.get_available_tools()[0]

    #     # Load the image using PIL (Pillow)
    #     image = Image.open(image_path)

    #     # Perform OCR and extract text
    #     extracted_text = tool.image_to_string(
    #         image,
    #         lang="eng",  # Language code for English. Change it based on your image content.
    #         builder=pyocr.builders.TextBuilder()
    #     )

    #     return extracted_text.strip()
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return None


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')


if __name__ == '__main__':
    app.run()

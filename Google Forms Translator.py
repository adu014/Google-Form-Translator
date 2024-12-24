from googletrans import Translator
from PIL import Image
import pyautogui, time, pytesseract
import pyperclip
import re

# Initialize Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create a persistent Translator object
translator = Translator()

def translate_to_french(text):
    # Reuse the global translated text variable
    return translator.translate(text, dest='fr').text

def alt_tab():
    pyautogui.hotkey('alt', 'tab')

def capture_and_read_text():
    # Capture a smaller region if possible for faster screenshots
    region = (100, 100, 1250, 400)  # Modify region size if needed
    screenshot = pyautogui.screenshot(region=region)

    # Use pytesseract to read the screenshot text
    config = '--oem 3 --psm 6'  # Add Tesseract config for speed optimization
    text = pytesseract.image_to_string(screenshot, config=config)
    return text

def type_text_with_accents(text):
    # Use clipboard for pasting the text with accents
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

# Start the process
alt_tab()

# For faster iteration, combine text cleanup into one regex step
pattern = re.compile(r'[\*\(\)1p1P2]')  # Combine unwanted characters into one pattern

for i in range(35):
    try:
        # Capture and OCR the text
        text_transate = capture_and_read_text()
        print(text_transate)

        # Translate the text to French
        translated_text = translate_to_french(text_transate)
        print("Translated text (in French):", translated_text)

        # Clean up the translated text in one step using regex
        translated_text = re.sub(pattern, '', translated_text)

        # Type the translated text with accents
        type_text_with_accents(translated_text)
        
        # Simulate a tab press to move forward
        pyautogui.press('tab')
    
    except Exception as e:
        # Handle exceptions and move forward
        pyautogui.press('tab')
        print("Error occurred:", e)
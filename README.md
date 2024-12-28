# Screen Translation Automation

This repository contains a Python script that automates the process of capturing on-screen text, translating it into French, and typing the translated text with proper accents. The script integrates optical character recognition (OCR), Google Translate API, and automation tools like PyAutoGUI.

---

## Features

### 🌐 Translation and OCR
- **Text Capture:** Extract text from a defined screen region using **Tesseract OCR**.
- **French Translation:** Translate captured text into French using the **Google Translate API**.
- **Text Cleaning:** Automatically remove unwanted characters using regex patterns.

### 💻 Automation
- **Keyboard Shortcuts:** Automate application switching with **Alt+Tab**.
- **Clipboard Integration:** Paste translated text using **Pyperclip**.
- **Tab Navigation:** Simulate keypresses to navigate between input fields.

### 🔧 Customization
- Adjustable screen capture region.
- Configurable Tesseract OCR options for improved speed and accuracy.

---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/screen-translation-automation.git
cd screen-translation-automation
```

### 2️⃣ Install Dependencies
Install required libraries using `pip`:
```bash
pip install googletrans==4.0.0-rc1 pyautogui pytesseract pillow pyperclip
```

### 3️⃣ Configure Tesseract Path
Ensure Tesseract is installed and update the script with the correct path:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## How to Use

1. **Define the Screen Region:**
   Update the `region` parameter in `capture_and_read_text()` to match your desired capture area:
   ```python
   region = (100, 100, 1250, 400)
   ```

2. **Run the Script:**
   Launch the script to start automating the process:
   ```bash
   python screen_translation.py
   ```

3. **Switch Applications:**
   Ensure the target application is active after the **Alt+Tab** automation.

4. **Translation Output:**
   The script:
   - Captures text from the screen.
   - Translates it into French.
   - Types the translated text into the active application.

---

## Example Workflow

- **Text Capture:** A screenshot is taken of a predefined region on the screen.
- **OCR Extraction:** The captured image is processed using Tesseract to extract text.
- **French Translation:** The text is translated into French using Google Translate.
- **Text Entry:** The translated text is pasted into the active field using keyboard automation.

---

## Future Enhancements
- **Language Selection:** Add support for multiple target languages.
- **GUI Interface:** Provide an interface for defining regions and customizing settings.
- **Error Logging:** Implement detailed error handling and logging for debugging.

---

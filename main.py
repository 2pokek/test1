from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf',language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return 'file exists'
    else:
        return 'ERROR'

def main():
    print(pdf_to_mp3(file_path="/"))

if __name__ == '__main__':
    main()
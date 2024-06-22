import fitz 
from gtts import gTTS

def pdf_to_audio(pdf_path, audio_path):
    pdf_document = fitz.open(pdf_path)

    text = ''

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    pdf_document.close()

    tts = gTTS(text)
    tts.save(audio_path)
    print(f"Audio saved to {audio_path}")
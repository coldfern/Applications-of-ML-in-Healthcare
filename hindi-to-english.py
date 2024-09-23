!pip install indic-nlp-library
!pip install fairseq

# Clone the repository to get the models
!git clone https://github.com/AI4Bharat/indicTrans.git
!pip install -r indicTrans/requirements.txt

import torch
from fairseq.models.transformer import TransformerModel

# Load the pre-trained IndicTrans model for Hindi-to-English translation
hi_en = TransformerModel.from_pretrained(
    'indicTrans/models/hi-en/',  # Path to the model
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path='indicTrans/data-bin/hi-en',  # Corresponding data path
    bpe='sentencepiece',
    sentencepiece_model='indicTrans/sentencepiece.bpe.model'
)

# Function to translate Hindi text to English
def translate_hindi_to_english(hindi_text):
    english_translation = hi_en.translate(hindi_text)
    return english_translation

# Example of extracted Hindi transcription
hindi_text = "मेरा नाम रोहन है। मैं 25 साल का हूँ। मेरी ऊंचाई 175 सेंटीमीटर है और मेरा वजन 70 किलो है।"

# Translate to English
english_translation = translate_hindi_to_english(hindi_text)
print("English Translation:", english_translation)

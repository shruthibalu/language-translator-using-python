from googletrans import Translator

# Create a translator object
translator = Translator()

# Input the text to be translated
text = input("Enter the text to be translated: ")

# Specify the source and target languages
src_lang = input("Enter the source language (e.g. en for English): ")
tgt_lang = input("Enter the target language (e.g. es for Spanish): ")

# Translate the text
translation = translator.translate(text, src=src_lang, dest=tgt_lang)

# Print the translated text
print(f"Translated text: {translation.text}")




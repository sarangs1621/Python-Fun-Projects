from translate import Translator
translator= Translator(from_lang=input("enter  your language:"),to_lang=input("which language do you want to translate:"))
translation = translator.translate(input("enter the word or sentence:"))
print( translation)

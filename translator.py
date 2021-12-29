from googletrans import Translator, constants

translator = Translator()

# detects the language automatically and translates by default to English
translation = translator.translate("Kya kar rahe ho")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# lets try changing destination language
translation = translator.translate("Kya kar rahe ho", dest="ar")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# print the detected language
detection = translator.detect("नमस्ते दुनिया")
print("Language code:", detection.lang)                 # returns the code of the language used, returns hi meaning hindi
print("Confidence:", detection.confidence)              # output 1 means its 100% confident about the language detection

# gives the complete name of the language used
print("Language:", constants.LANGUAGES[detection.lang])


# Kannada detection
detection2 = translator.detect("ಊಟ ಆಯಿತು")
print("Language:", constants.LANGUAGES[detection2.lang])
print("Language code:", detection2.lang)                
print("Confidence:", detection2.confidence) 

# English to kannanda
translation2 = translator.translate("What are you doing?", dest='kn')
print(translation2.text)

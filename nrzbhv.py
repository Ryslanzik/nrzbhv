def translate(text):
    
    translated_text = ' '.join(''.join(a for a in text if a not in 'АаЕеЁёИиОоУуЫыЭэЮюЯя.!?,:;-\'"').split())
    return translated_text


print(translate(""))

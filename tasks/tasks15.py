# 15. Программа переводчик на соленый язык.
# Правило: после каждой гласной вставляем с + сама гласная. Привет -> Приcивеcет
# Сальса -> саcальсаcа

text = input('Введите текст для перевода: ')
def translator_to(text):
    text_in_list = list(text)
    translated_text1 = []
    for letter in text_in_list:
        if letter in ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']:
            translated_text1.append(letter)
            translated_text1.append('c' + letter)
        else:
            translated_text1.append(letter)
    return ''.join(translated_text1)

print(translator_to(text))
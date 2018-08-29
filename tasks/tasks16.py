#16. Программа переводчик из соленого языка. Посокесемосон -> Покемон
text = input('Введите текст для перевода: ')
def translator_from(text):
    text_in_list = list(text)
    translated_text1 = []
    for index, letter in enumerate(text_in_list[0:len(text_in_list)]):
        if letter in ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']:
            if index < len(text_in_list) - 1:
                if text_in_list[index + 1] == 'с':
                    if text_in_list[index + 2] == letter:
                        translated_text1.append(letter)
                        translated_text1.append([text_in_list[index + 1], text_in_list[index + 2]])
        else:
            translated_text1.append(letter)
    print(translated_text1)
    for index, letter in enumerate(translated_text1):
        if len(letter) > 1:
            print(index, letter)
            print(translated_text1[index + 1])
            translated_text1.pop(index + 1)
            translated_text1.pop(index)
    return translated_text1

print(translator_from(text))


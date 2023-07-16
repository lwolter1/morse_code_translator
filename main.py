to_morse_dictionary = {'a': '.-',
                       'b': '-...',
                       'c': '-.-.',
                       'd': '-..',
                       'e': '.',
                       'f': '..-.',
                       'g': '--.',
                       'h': '....',
                       'i': '..',
                       'j': '.---',
                       'k': '-.-',
                       'l': '.-..',
                       'm': '--',
                       'n': '-.',
                       'o': '---',
                       'p': '.--.',
                       'q': '--.-',
                       'r': '.-.',
                       's': '...',
                       't': '-',
                       'u': '..-',
                       'v': '...-',
                       'w': '.--',
                       'x': '-..-',
                       'y': '-.--',
                       'z': '--..',
                       '1': '.----',
                       '2': '..---',
                       '3': '...--',
                       '4': '....-',
                       '5': '.....',
                       '6': '-....',
                       '7': '--...',
                       '8': '---..',
                       '9': '----.',
                       '0': '-----',
                       '.': '.-.-.-',
                       ',': '--..--',
                       '?': '..--..',
                       }
from_morse_dictionary = {value: key for (key, value) in to_morse_dictionary.items()}


def is_morse(text):
    if text[0] == "." or text[0] == "-":
        return True
    else:
        return False


def converter(text):
    char_list = []
    if is_morse(text):
        letter = ""
        for char in text:
            if char == " ":
                char_list.append(letter)
                letter = ""
            elif char == text[-1]:
                letter += char
                char_list.append(letter)
                letter = ""
            else:
                letter += char
        return char_list
    else:
        for char in text:
            char_list.append(char.lower())
        return char_list


def translator(char_list):
    translated = []
    if is_morse(char_list[0]):
        for letter in char_list:
            if letter == "/":
                translated.append(" ")
            else:
                translated.append(f"{from_morse_dictionary[letter.strip()]}")
    else:
        for letter in char_list:
            if letter == " ":
                translated.append("/ ")
            else:
                translated.append(f"{to_morse_dictionary[letter]} ")
    return ''.join(translated)


def app(text):
    char_list = converter(text)
    translated_text = translator(char_list)
    if is_morse(text):
        print(f"Original message: {text}\nTranslated from Morse Code: {translated_text}")
    else:
        print(f"Original message: {text}\nTranslated to Morse Code: {translated_text}")


to_translate = input("Enter your message here: ")
app(to_translate)
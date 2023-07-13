dictionary = {'a': '.-',
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


def translator(text):
    char_list = []
    for char in text:
        char_list.append(char)
    translated = []
    for letter in char_list:
        if letter == " ":
            translated.append("/ ")
        else:
            translated.append(f"{dictionary[letter.lower()]} ")
    print(f"Original message: {text}\nTranslated to Morse Code: {''.join(translated)}")


to_translate = input("Enter your message here: ")
translator(to_translate)
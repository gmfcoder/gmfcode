char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.',
  '*': '*'
}

dots_to_char={v: k for k, v in char_to_dots.items()}

def decode_morse(morsetotext,morsedict=dots_to_char):
    print(3*"\n")
    textstr=""
    errorstr=""
    error=False
    listtomorse=morsetotext.split(" ")
    for item in listtomorse:
        if item not in dots_to_char.keys():
            errorstr+=item+","
            error=True
            continue
        else:
            textchar=dots_to_char.get(item)
            textstr+=textchar

    if error==True:
        return print(f"Sorry, Characters [{errorstr[:-1]}] in [{morsetotext}] not decodable in morse code!\n")
    else:
        return print(f"[{morsetotext}] decodes to: [{textstr}] in morse code\n")

def encode_morse(texttomorse,morsedict=char_to_dots):
    print(3*"\n")
    morsestr=""
    errorstr=""
    error=False
    texttomorse=texttomorse.upper()
    for item in texttomorse:
        if item not in morsedict.keys():
            errorstr+=item+","
            error=True
            continue
        else:
            morsechar=morsedict.get(item)+" "
            morsestr+=morsechar

    if error==True:
        return print(f"Sorry, Characters [{errorstr[:-1]}] in [{texttomorse}] not encodable in morse code!\n")
    else:
        return print(f"[{texttomorse}] encodes to: [{morsestr[:-1]}] in morse code\n")




decode_morse(".... . .-.. .--. * -- .")
encode_morse("help*me")

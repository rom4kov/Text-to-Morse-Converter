from morse_code import morse_code 
import os
from logo import logo


class MorseConverter():
    def __init__(self) -> None:
        self.operation = ""
        self.op_choice()
        
    def op_choice(self):
        while self.operation != "e" and self.operation != "d" and self.operation != "q":
            os.system("clear")
            print(logo)
            self.operation = input("Type 'e' to encode text to morse,\ntype 'd' to decode morse to text, or\ntype 'q' to quit:\n\n")
        if self.operation == "e":
            self.operation = ""
            self.encode()
        elif self.operation == "d":
            self.operation = ""
            self.decode()
        elif self.operation == 'q':
            pass

    def encode(self):
        os.system("clear")
        print(logo)
        
        morse_code_string = ""

        text = list(input("Type text to convert to morse code:\n\n").lower())

        error = None

        for char in text:
            if char == " ":
                morse_code_string += "   "
            else:
                try:
                    morse_code_string += morse_code[char] + " "
                except KeyError as e:
                    error = e
                    print(f"\nSorry, there is no corresponding Morse code symbol for the character {e}.\n"
                           "\nPlease provide only characters with corresponding Morse code symbols.\n\n")
                    input("Press any key to continue")

        if not error:
            print(f"\nYour morse code:\n\n{morse_code_string}\n")
            input("Press any key to continue")

        self.op_choice()

    def decode(self):
        os.system("clear")
        print(logo)

        reverse_morse_code = {value: key for key, value in morse_code.items()}

        plain_text_string = ""

        morse_words = input("Please provide morse code to decode to text:\n\n").split("   ")

        error = None

        for word in morse_words: 
            morse_letters = word.split()
            text_word = ""
                    
            try:
                text_word = ''.join(reverse_morse_code[letter] for letter in morse_letters)
            except KeyError as e:
                error = e
                print(f"\n{e} is not a valid morse code symbol.\nPlease provide only valid "
                       "Morse code symbols.\n\n")
                input("Press any key to continue")

            plain_text_string += text_word + " "

        if not error:
            print(f"\nYour text:\n\n{plain_text_string}\n")
            input("Press any key to continue")

        self.op_choice()

morse_converter = MorseConverter()


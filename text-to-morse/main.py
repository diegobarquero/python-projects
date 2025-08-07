from morse_code import morse_code

# Create a dictionary for faster lookup
morse_dict = {char.upper(): code for (char, code) in morse_code}

text = input("Type the text to convert: ")
text_to_morse = ""

"""
for letter in text:
    for code in morse_code:
        if letter.upper() in code:
            text_to_morse += f"{code[1]} "
        elif letter == " ":
            text_to_morse += " "
"""

for letter in text:
    if letter.upper() in morse_dict:
        text_to_morse += f"{morse_dict[letter.upper()]} "
    elif letter == " ":
        # Add a pipe for word separation (optional)
        text_to_morse += "| "

print(text_to_morse)

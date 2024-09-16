import requests
import random

# Define a function to get ASCII art using the API
def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)

# User inputs for text and font
text = input('ASCII Art Text > ')
font = input('ASCII Art Font (leave empty for default or type "random" for random fonts) > ')

# Default font handling
if font == "":
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    print("Font: default")
    print(r.text)

# If a specific font is defined
elif font != "random":
    getAsciiArt(text, font)

# If the user selects "random" fonts
elif font == "random":
    data = requests.get('http://artii.herokuapp.com/fonts_list')
    fontsArray = data.text.split('\n')

    # Display the text in 3 random fonts
    for i in range(3):
        font = random.choice(fontsArray)
        getAsciiArt(text, font)

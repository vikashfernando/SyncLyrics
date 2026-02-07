import time

# Lyrics with pauses (seconds)
lyrics = [
    ("Hamuwuwado Lyrics 🎵:", 1),
    ("Sonduree Hadak Nathi Kaluwara Yameee", 2),
    ("Danune Nubath Nathi Aduwada Aye Paraaa", 2),
    ("Nuba Na Ahan Nathi Hadawatha Mageee", 2),
    ("Huru Na Hithath Hri Kalabala Wagee........", 2)
]

# Function to print letters slowly
def print_letter_by_letter(text, speed=0.09): 
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
    print()  # new line after line

# Print lyrics
for line, pause in lyrics:
    print_letter_by_letter(line)
    time.sleep(pause)  # pause after each line
    
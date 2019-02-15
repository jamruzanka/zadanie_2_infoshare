import os
all_files = open("all_files.txt","w+")
for file in os.listdir(r"C:\Users\mwjam\Desktop\KURS\zadanie_2\words"):
    if file.endswith('.txt'):
        f = open(file)
        f2 = open("all_files.txt","a+")
        for letter in f:
            f2.write(letter.lower())

with open("all_files.txt") as all_letters:
    data = all_letters.read()
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
    ascii_separate = list(ascii_letters)
    for letter in ascii_separate:
        count = 0
        for char in data:
            if letter == char:
                count += 1
        print("Number of {}: {}".format(letter,count))

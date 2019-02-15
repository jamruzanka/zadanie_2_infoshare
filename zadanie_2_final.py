import os

ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
for character in ascii_letters:
    dict[character] = 0
for file in os.listdir(r"C:\Users\mwjam\Desktop\KURS\zadanie_2\words"):
    if file.endswith('.txt'):
        with open(file) as all_letters:
            data = all_letters.read().lower()
            for char in data:
                dict[char] +=1
#print("Number of {}: {}".format(list(dict.keys()), list(dict.values())))
print(dict)

text = input("Matn kiriting: ")

words = text.split()

word_count = len(words)
char_count = len(text)

frequency = {}

for word in words:
    word = word.lower()

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("So'zlar soni:", word_count)
print("Belgilar soni:", char_count)

print("\nSo'zlar statistikasi:")
for word, count in frequency.items():
    print(word, ":", count)

from collections import Counter

text = input("Enter text: ")

words = text.split()
word_count = len(words)
char_count = len(text)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in text if ch in vowels)

word_freq = Counter(words)
repeated_words = {}

for word, count in word_freq.items():
    if count > 1:
        repeated_words[word] = count

print("Word Count:", word_count)
print("Character Count:", char_count)
print("Vowel Count:", vowel_count)
print("Repeated Words:", repeated_words)
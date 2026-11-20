Text Analysis Using Python
📌 Project Overview
This project performs basic text analysis on a given text input. It calculates:

Total number of words
Total number of characters
Total number of vowels
Repeated words and their frequency
This task was completed as part of the Veda Technology Internship Program.

🚀 Features
✅ Word Count

✅ Character Count

✅ Vowel Count

✅ Repeated Word Detection

✅ Simple and Easy-to-Understand Python Code

🛠 Technologies Used
Python 3
Collections Module (Counter)
📂 Project Structure
Text-Analysis-Python/
│
├── text_analysis.py
├── README.md
└── LICENSE
💻 Source Code
from collections import Counter

text = input("Enter text: ")

words = text.split()
word_count = len(words)
char_count = len(text)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in text if ch in vowels)

word_freq = Counter(words)
repeated_words = {word: count for word, count in word_freq.items() if count > 1}

print("Word Count:", word_count)
print("Character Count:", char_count)
print("Vowel Count:", vowel_count)
print("Repeated Words:", repeated_words)
📊 Example
Input
python is easy and python is powerful
Output
Word Count: 7
Character Count: 37
Vowel Count: 12
Repeated Words: {'python': 2, 'is': 2}
🎯 Learning Outcomes
Text Processing Basics
Word Tokenization
Character Counting
Vowel Identification
Repeated Word Analysis
Introduction to NLP Concepts
🏢 Internship
Project completed under:

Veda Technology Internship Program

👨‍💻 Author
Md Yash Johar Ali

GitHub: https://github.com/mdyashjoharali

LinkedIn: https://www.linkedin.com/in/mdyashjoharali/

📜 License
This project is licensed under the MIT License.


# Simple Python program to find most frequent words in a file

# Read the file
with open("sample.txt", "r") as file:
    text = file.read()

# Convert to lowercase and split into words
words = text.lower().split()

# Count word frequencies
word_count = {}
for word in words:
    word = word.strip(".,!?\"'")  # Remove punctuation
    word_count[word] = word_count.get(word, 0) + 1

# Find and print the most frequent words
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(word, ":", word_count[word])

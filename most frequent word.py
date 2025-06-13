# Open and read the file
file = open("sample.txt", "r")
text = file.read()
file.close()

# Convert text to lowercase and split into words
words = text.lower().split()

# Count each word
word_count = {}
for word in words:
    word = word.strip(".,!?")  # remove punctuation
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the most frequent words
print("Most frequent words:")
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(word, ":", word_count[word])

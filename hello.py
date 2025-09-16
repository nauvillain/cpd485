import random
import nltk
from nltk.corpus import words

# Download the word list if not already present
nltk.download('words')

# Get the list of English words
word_list = words.words()

# Select 10 random words
random_words = random.sample(word_list, 10)

# Display the words
print("Ten random words:")
for word in random_words:
    print(word)

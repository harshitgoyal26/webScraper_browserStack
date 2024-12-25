import re
import sys
def analyze_headers(translated_titles):
    all_words = " ".join([str(title) for title in translated_titles]).split()

    word_counts = {}
    for word in translated_titles:
        word_counts[word] = word_counts.get(word, 0) + 1


  
    repeated_words = {word: count for word, count in word_counts.items() if count > 1}
    return repeated_words


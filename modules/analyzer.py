import re

def analyze_headers(translated_titles):
    # Should be strings only
    all_words = " ".join([str(title) for title in translated_titles]).split()

    # Count
    word_counts = {}
    for word in all_words:
        word = re.sub(r"[^a-zA-Z]", "", word).lower()
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1


  
    repeated_words = {word: count for word, count in word_counts.items() if count > 2}


    return repeated_words


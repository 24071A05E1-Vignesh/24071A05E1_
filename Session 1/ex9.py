#Write a function that finds the most common word in a given text.
from collections import Counter
import re

def most_common_word(text):
    # Remove non-alphabetic characters and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Use Counter to count the frequency of each word
    word_counts = Counter(words)
    
    # Find the most common word and its count
    most_common = word_counts.most_common(1)
    
    # Return the most common word
    if most_common:
        return most_common[0]
    else:
        return None
    

# Example usage:
text = "This is a sample text with some repeated words. This is a test text."
result = most_common_word(text)
print(f"The most common word is '{result[0]}' with {result[1]} occurrences.")
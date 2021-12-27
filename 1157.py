import sys
import collections
input_data = sys.stdin.readline().strip()
word_dict = collections.Counter(input_data.lower())
max_word = [k for k,v in word_dict.items() if max(word_dict.values()) == v]
if len(max_word) > 1:
    print("?")
else:
    print(max_word[0].upper())

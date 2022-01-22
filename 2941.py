import sys
test_words = ['c=','c-','dz=','d-','lj','nj','s=','z=']
input_data = sys.stdin.readline().strip()
for word in test_words:
    input_data = input_data.replace(word, "*")
print(len(input_data))
'''
2번 
positions = [[4,3], [2,1], [1,2], [4,3], [4,3], [1,2]]
positions = [[1,1], [1,1], [1,1]]
test = set(list(map(tuple,positions)))

print(len(positions) - len(test))
'''
input_data = list('z')
change_low = 122
for i in input_data:
    if ord(i) >= 97 and ord(i) <=122:
        print(chr(change_low))
    change_low -= 1
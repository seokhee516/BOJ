import sys
input = sys.stdin.readline

def make_trie(dic, arr):
    if len(arr) == 0:
        return
    if arr[0] not in dic:
        dic[arr[0]] = {}
    make_trie(dic[arr[0]], arr[1:])

def print_trie(dic, leng):
    for k in sorted(dic.keys()):
        print("--"*leng + k)
        print_trie(dic[k],leng+1)

n = int(input())
dic = {}
for _ in range(n):
    data = input().strip().split(' ')
    make_trie(dic, data[1:])
    
print_trie(dic, 0)

import sys
input = sys.stdin.readline
while True:
    sur = input().strip()
    if sur == "*":
        break
    def fun(sur=sur):
        for i in range(1,len(sur)):
            tmp = []
            for j in range(len(sur)-i):
                if sur[j]+sur[j+i] in tmp:
                    return print(sur,"is NOT surprising.")
                else:
                    tmp.append(sur[j]+sur[j+i])
        return print(sur,"is surprising.")
    fun()
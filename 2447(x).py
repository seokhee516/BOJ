'''
못 품
'''
def star_function(n):
    if n == 3:
        for e in star[:3]:
            print(e)
    else:
        print("*"*n)
        for i in range(3):
            star_function(int(n/3)) 
    

star = ['***', '* *', '***']
star_function(3)
# print(star_function(3)) 

# print(star[0], "\n", star[1])


# print(star[0]*int(27/3))
# print(star[1]*int(27/3))
# print(star[0]*int(27/3))
# print((star[0]+str(' ')*3+star[0])*3)
# print(star[1]+str(' ')*3+star[1])
# print(star[0]+str(' ')*3+star[0])
# print(star[0]*3)
# print(star[1]*3)
# print(star[0]*3)
import sys
input = sys.stdin.readline

n=int(input())
def draw_stars(n):
  if n==1: # n == 1이 될 때까지 재귀
    return ['*']

  Stars=draw_stars(n//3) 
  L=[]
  for star in Stars:
    L.append(star*3) # n==1 star== * star*3 == *** 
  for star in Stars:
    L.append(star+' '*(n//3)+star) # * *
  for star in Stars:
    L.append(star*3) # ***
  return L

print('\n'.join(draw_stars(n)))
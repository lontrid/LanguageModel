import random
with open('input.txt') as inp:
  l = inp.read()
for char in '?.!/;:—,«»\"()':  
  l = l.replace(char,'')  
l = l.lower()
l = l.split()
for i in range(100):
  print(random.choice(l)+' ', end='')

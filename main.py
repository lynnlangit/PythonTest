#1. Print int array, neg, then zero, then positive
numbers = [0,1,2,-1,0,3,0]
numbers.sort()
for num in numbers:
	print(num)
print("\n"+"This is puzzle #1")

#2. Print all palindromes in string of letters
letters = 'aaaabbbcccgaaaz'
for l in letters:
  print(l)
print("\n"+"This is puzzle #2")

#3. LOOKUP Look at your telephone keypad – each number has some letters associated with it 
#reference list:  2 is ABC, 3 is DEF, 4 is GHI, 5 is KJL, 6 is MNO, 7 is PQR, 8 is STU, 9 is VWX, 0 is YZ
#Given a sequence of letters, print out the equivalent number. 
#But do this without storing an explicit mapping array or hashmap – no additional storage space.
letters = 'abacdcdaaaz'
for l in letters:
  if l == 'a' or l=='b' or l=='c':
  	 print('2')
  elif l == 'd':
  	 print('3')  
  else:
  	 print(l)
print("\n"+"This is puzzle #3")
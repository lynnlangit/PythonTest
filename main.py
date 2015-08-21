#General Convenience Methods
def namePuzzle(puzzle):
	print("\n"+ "Starting puzzle #" + puzzle + "...")
    
def solvePuzzle(puzzle):
   print("\n"+ "Solved puzzle #" + puzzle)
    
#1. Print int array, neg, then zero, then positive
namePuzzle('1')
numbers = [0,1,2,-1,0,3,0, -2]
numbers.sort()
for num in numbers:
	print(str(num),end=', ')
solvePuzzle("1")

#2. Print all palindromes of three or more in string of letters
namePuzzle('2')
letters = 'ababafeefzabazf'
beginPos= 0
currPos = 0 
for firstLetter in letters:  
  posPalin = []
  for nextLetterPosition in range(len(letters)-beginPos): 
    isEvenPal = 1
    isOddPal = 1
    posPalin.append(letters[nextLetterPosition+beginPos])
    posPalString = "".join(posPalin)
    if (((len(posPalString))%2)==0) and (len(posPalString) > 2): 
      middle = int(len(posPalString)/2)
      isEvenPal = 1
      for i in range(middle):
        if posPalString[i] == posPalString[len(posPalString)-(i+1)] and isEvenPal == 1: 
          isEvenPal = 1
        else:
          isEvenPal = 0
      if isEvenPal:
        print(posPalString)
    elif (len(posPalString) > 2): 
      isOddPal = 1
      middle = int(((len(posPalString)+1)/2)-1)
      for i in range(middle):
        if posPalString[middle-(i+1)] == posPalString[middle+(i+1)] and isOddPal == 1:
          isOddPal = 1          
        else:
          isOddPal = 0
      if isOddPal: 
        print(posPalString)
    currPos += 1
  beginPos += 1
solvePuzzle("2")

#3. LOOKUP print number from letter on a telephone keypad w/out using mapping array/hashmap
#ref list:  2 is ABC, 3 is DEF, 4 is GHI, 5 is KJL, 6 is MNO, 7 is PQR, 8 is STU, 9 is VWX, 0 is YZ
namePuzzle('3')
letters = 'lynnabacdcdaeez'
def lookup(l):
  if l == 'a' or l=='b' or l=='c':
  	 print('2', end=", ")
  elif l == 'd' or l == 'e':
  	 print('3', end=", ")  
  elif l == 'z':
    print('0', end=", ")
  else:
  	 print(l, end=", ")
for l in letters:
  lookup(l)
solvePuzzle("3")

#4. STRING OPERATIONS Given a character array which contains a sentence 
#(words separated by spaces), given the indices of two words in the character array, 
#swap the words – words can be anywhere in the sentence, and can be of different lengths.

#5. RECURUSION - NODE WALKING Given the root of a binary tree, where each node has 
#an integer value and has left and right child pointers, print out the values of all the nodes 
#in the tree, in level order. i.e, root first, then its children if any, then grandchildren 
#if any (in visual order left to right), and so on.

#6. RECURISON - NODE SEARCHING Given two nodes in a binary tree where each node structure 
#has a left child, right child and parent pointer, find the node that is the closest common ancestor.

#7. RECURSION - NODE OPERATIONS Given the root of a binary tree, 
#where each node has a left pointer and a right pointer, mirror the tree – 
#i.e., for every node in the tree, its former left child should become its right child 
#and its former right child should become its left child.
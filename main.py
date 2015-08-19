#1. Print int array, neg, then zero, then positive
numbers = [0,1,2,-1,0,3,0]
numbers.sort()
for num in numbers:
	print(str(num),',',end='')
print("\n"+"This answers puzzle #1")

#2. Print all palindromes in string of letters
letters = 'aaaabbbcccgaaaz'
for l in letters:
  print(l)
print("\n"+"This is puzzle #2")

#3. LOOKUP print number from letter on a telephone keypad w/out using mapping array/hashmap
#ref list:  2 is ABC, 3 is DEF, 4 is GHI, 5 is KJL, 6 is MNO, 7 is PQR, 8 is STU, 9 is VWX, 0 is YZ
letters = 'abacdcdaeez'
for l in letters:
  if l == 'a' or l=='b' or l=='c':
  	 print('2')
  elif l == 'd' or l == 'e':
  	 print('3')  
  else:
  	 print(l)
print("\n"+"This is puzzle #3")

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
"""For your Metis application you wrote a program that let's the
user guess a number between 1 and 100. Can you write a program
that does the reverse. Write a function that takes in a number
between 1 and 100 and tries to guess it. Based on whether a guess
is larger or smaller than the input number, the code would come up with
a new guess until it gets it right."""

# Pair Problem 1

import random
def guess(guess_num):
	guess_num = eval(input("Pick a number between 1 and 100: "))
	while guess_num > 100 or guess_num < 1:
		guess_num = eval(input("Must be in between 1 and 100: "))
	x = random.randint(1,101)
	count = 1
	low = 1
	high = 100
	while guess_num != x:
		if guess_num > x:
			high = guess_num
			count += 1
		if guess_num < x:
			low = guess_num + 1
			count += 1
		guess_num = (low+high) // 2

	print("I got it right in", count, "tries.")
guess(1)

"""The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the
1000-digit number that have the greatest product.
What is the value of this product?"""

# Pair Problem 2

def max_product(numberString):
	largest = 1
	i = 0
	while i < len(numberString) - 13:
	    one = int(numberString[i]) 
	    two = int(numberString[i+1])  
	    three = int(numberString[i+2]) 
	    four = int(numberString[i+3])
	    five = int(numberString[i+4])
	    six = int(numberString[i+5])
	    seven = int(numberString[i+6])
	    eight = int(numberString[i+7])
	    nine = int(numberString[i+8])
	    ten = int(numberString[i+9])
	    eleven = int(numberString[i+10])
	    twelve = int(numberString[i+11])
	    thirteen = int(numberString[i+12])
	    product = one*two*three*four*five*six*seven*eight*nine*ten*eleven*twelve*thirteen
	    if product > largest:
	        largest = product
	    i = i + 1 
	print(largest)
max_product('\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450')


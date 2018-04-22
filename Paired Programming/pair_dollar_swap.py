# teller swapped the dollar and cents amounts
# ended up with double the amt but one cent short
# what was the amount of the check

def check(cents):
	coins = str(cents)
	print(coins[4]+coins[3]+coins[2]+coins[1]+coins[0])
check(98.99)
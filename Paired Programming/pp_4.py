# create a list 
# do a while a loop to iterate through the divisors in the list 

def largest_prime(n):
	factors = []
	d = 2
	while n >= d:
		if n%d ==0:
			factors.append(d)
			n /= d
		d += 1
	print(factors)
largest_prime(600851475143)


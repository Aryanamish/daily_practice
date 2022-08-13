# Python implementation of the above Approach
mod = 1_000_000_007
SIZE = 10000

# declaring list initially and making
# it 1 i.e for every index
fact = [1]*SIZE

# Calculation of factorial using Dynamic programming
def factorial():
	for i in range(1, SIZE):	
	
		# Calculation of factorial
		# As fact[i-1] stores the factorial of n-1
		# so factorial of n is fact[i] = (fact[i-1]*i)	
		fact[i] = (fact[i-1]*i) % mod

# function call
factorial()

# Driver code
arr=[3,10,200,20,12]
for i in arr:
	print(fact[i])

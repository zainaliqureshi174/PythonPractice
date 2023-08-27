Fact = input ("Enter a number to Calculate its Factorial: ")
Fact = int(Fact)
factorial = 1
a = 1
while a <= Fact:
	factorial = factorial * a
	a = a + 1

print ("Factorial of", Fact, " is:", factorial)

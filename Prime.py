Num = input("Enter a number to check if it is a prime number or not: ")
Num = int(Num)

is_Prime = True

for i in range (2, Num - 1):
	if ((Num % i) == 0):
		is_Prime = False
		break
	else:
		is_Prime = True

if (is_Prime):
	print(Num, "is a Prime Number")
else:
	print(Num, "is not a Prime Number")
		

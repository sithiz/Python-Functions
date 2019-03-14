def sum_of_all(number):
	total = 0
	for each in range(0, number+1):
		total += each
	return print(total)


sum_of_all(10)

def largest(list):
	base = 0
	for number in list:
		if number > base:
			base = number 
	return print(base)

largest([1,5,3,4,9])

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return print(product)





def RecPermute(sofar, rest):
	if rest == "":
		print(sofar)
	else:
		for i in range(len(rest)):
			next = sofar + rest[i]
			remaining = rest[0:i] + rest[i+1:]
			RecPermute(next,remaining)

def RecSubsets(sofar, rest):
	if rest == "":
		print(sofar)
	else:
		RecSubsets(sofar + rest[0], rest[1:])
		RecSubsets(sofar,rest[1:])					

def ArraySum(arr):
	sum = 0
	for num in arr:
		sum += num
	return sum

def SubsetSum(sofar, remaining, target):		
	if len(remaining) == 0:
		if ArraySum(sofar) == target:
			print(sofar)
			return 1
		else:
			return 0
	else:
		sofar2 = sofar[:]
		sofar2.append(remaining[0])
		return SubsetSum(sofar2, remaining[1:], target) + SubsetSum(sofar, remaining[1:], target)

def main():	
	sofar = []	
	remaining = [3,4,5,-1,0]
	print(SubsetSum(sofar, remaining, 7))

if __name__ == '__main__':
	main()		
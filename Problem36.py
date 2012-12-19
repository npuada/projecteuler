#36081st
def isPalindrome(s):
	end = len(s)-1
	start = 0
	mid = len(s)/2

	while start < mid:
		if not s[start] == s[end]:
			return False
		start += 1
		end  -= 1

	return True

if __name__ == '__main__':
	palindromes10 = [] 
	for i in range(1000000):
		s = str(i)
		if(isPalindrome(s)):
			palindromes10.append(i)

	dual = []
	for i in palindromes10:
		s = bin(i)[2:]
		if(isPalindrome(s)):
			dual.append(i)

	print sum(dual)

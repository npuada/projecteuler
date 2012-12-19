import io
import re

def get_score(str):
	score = 0
	for char in str:
		score += (ord(char) - 64)
	return score

file = io.open('names.txt','rt')
string = file.read()
name_list = re.findall(r'\w+', string)
sorted = []
length = len(name_list)
while length:
	min_index = 0
	min = name_list[min_index]
	i = 0;
	while i < length:
		if name_list[i] < min:
			min_index = i
			min = name_list[min_index]
		i += 1
	min = name_list.pop(min_index)
	length = len(name_list)
	sorted.append(min)
	
i = 0
sum = 0
while i < len(sorted):
	sum += ((i+1) * get_score(sorted[i]))
	i += 1
print sum

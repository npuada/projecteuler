import math

sum_map = {i:1 for i in range(2,28124)}

for i in range(2,28124):
	j = i
	while j < 28124:
		temp = int(math.floor(math.sqrt(j)))
		if i <= temp:
			sum_map[j] += i
			if j/i != i:
				sum_map[j] += j/i
		j += i


abundant = []
for key in sum_map:
	if key < sum_map[key]:
		abundant.append(key)

i = 0
j = 0
sum_of_abundant = []
while i < len(abundant):
	j = i
	while j < len(abundant):
		temp = abundant[i] + abundant[j]
		sum_of_abundant.append(temp)
		j += 1
	i += 1

sum_of_abundant.sort()
curr = sum_of_abundant[0]
i = 1
total = curr
while i < len(sum_of_abundant) and sum_of_abundant[i] < 28124:
	if curr < sum_of_abundant[i]:
		curr = sum_of_abundant[i]
		total += curr
	i += 1

temp = (28123 * 28124)/2
print temp-total
prod_num = 1
prod_den = 1
	
for i in range(10,100):
	ones = i%10
	tens = i//10
	#cancel ones / tens
	for j in range(ones*10, (ones+1)*10):
		if j%10 != 0 and i/j == (tens)/(j%10) and i/j < 1:
			prod_num *= i
			prod_den *= j
			
print(prod_num,"/",prod_den)
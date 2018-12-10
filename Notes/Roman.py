


def numerus(roman):
	rom_list = list(reversed(roman))
	
	total = 0
	previous_num = 0
	
	for x in rom_list:	
		print("Number is " + str(x))
		
		if x == "i":
			x = 1
		elif x == "v":
			x = 5
		elif x == "x":
			x = 10
		elif x == "l":
			x = 50
		elif x == "c":
			x = 100
		else:
			x = 1000
		
		
		if total == 0:
			total = x
			previous_num = x
		else:
				if previous_num <= x:
					total = total + x
					previous_num = x
					print("adding " + str(total)) 
				else:
					total = total - x 
					previous_num = x
					print("subtracting " + str(total)) 
			
			
	return total
				
			
	
	
	
	
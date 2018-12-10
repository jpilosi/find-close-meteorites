def numerus(roman): 
	rom_list = list(reversed(roman))
	
	total = 0
	previous_num = 0
	
	
	rom_value = { "i":1, "v":5, "x":10, "l":50,"c":100,"m": 1000} 
	
	
	for x in rom_list:	
		x = rom_value.get("x")
		
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


firstlist = ["one","two","three","four","five","six"]
secondlist =  ["two","four","six","oddball"]	

def intersect(list1, list2):

	if list1 > list2:
		complist(list1, list2)
	else:
		complist(list2, list1)
		
		

def complist(larger, smaller):

	for l1 in larger:
		if l1 in smaller:
			print(l1 + " duplicat")
		else:
			continue
	
		
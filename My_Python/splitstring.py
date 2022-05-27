def splitthis(string):
	limiters = [' ','@','!','.']
	
	result = string.split(limiters[0])
	
	for i in range(1, len(limiters)):
		for j in range(len(result)):
			subsplit = result[j].split(limiters[i])
			if len(subsplit) > 1:
				result = result[:j] + subsplit +result[j+1:]
	return result

string = 'He!ll@oo'
ss = splitthis(string)
print(ss)
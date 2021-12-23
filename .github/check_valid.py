import sys

def checkPipes(line):
	return (line.count("|") == 10)
	
def checkStatus(cveFields):
	validValues= ['', 'Vulnerable', 'Fix', 'Workaround', 'Not vuln', 'Investigation', 'x']
	valid=True
	#print(cveFields)
	for field in cveFields:
		if field.strip() not in validValues:
			valid=False
	return valid

def checkLine(line):
	table=line.split("|")
	valid=True
	msg=[]
	#print(table)
	if not checkPipes(line):
		msg.append("Entry has not correct number of pipes. This will likely destroy the table.")
		valid=False
	if not checkStatus(table[4:8]):
		msg.append("Entry contains incorrect status value. Please check again.")
		valid=False
	return valid, msg

def parseDiff(difffile):
	errors=[]
	with(open(difffile, "r")) as f:
		for line in f: 
			if line.startswith("+") and not line.startswith("+++"):
				valid, msg = checkLine(line)
				if (not valid):
					errors.append((line, msg))
	return errors

def main():
	difffile=sys.argv[1]
	errors=parseDiff(difffile)
	if (len(errors) != 0):
		for (line, error) in errors:
			print(line, "\t\t", error)
		exit(1)


if __name__ == '__main__':
	main()

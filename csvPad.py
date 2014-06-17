import csv
import sys

def writeStatus(testBed, build, partNumber, status):
	'''
	Writes msg to a file "testBed.csv" as csv
	'''
	try:
		with open(testBed+'.csv', 'a') as f:
			scrapWriter = csv.writer(f, delimiter = ',', lineterminator = '\r')
			#scrapWriter.writeheader(['Build' , 'Part Number' , 'Status'])
			scrapWriter.writerow([build, partNumber, status])
		f.close()
	except csv.Error as e:
		print(e)
	
def readStatus(testBed):
	'''
	Reads msg from file named 'testBed.csv' and returns the value read as string
	'''
	filename = testBed+'.csv'
	with open(filename, 'rU') as f:
		reader = csv.reader(f)
		try:
			for row in reader:
				print(row)
			f.close()
		except csv.Error as e:
			print(e)
			
def isReady(testBed, partNumber):
	'''
	Returns true if the test bed is ready to run test for the partNumber
	'''
	filename = testBed+'.csv'
	with open(filename, 'rU') as f:
		reader = csv.reader(f)
		try:
			result = False
			for row in reader:
				if(row[1] == partNumber and row[2] != 'Running'):
					result = True
					break
				else:
					continue
			return result
			f.close()
		except csv.Error as e:
			print(e)
	return status
	
if __name__ == '__main__':
	testBed = 'GponDvt'
	partNumber = '1187502F1'
	build = 'TAML'
	status = 'Running'
	#writeStatus(testBed, build, partNumber, status)
	#readStatus(testBed)
	print isReady(testBed, partNumber)
	
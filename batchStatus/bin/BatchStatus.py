import csv

#select csv file path having job run times
path='.\\batchStatus\\SharedPath\\JobRunTimes.csv'
file=open(path,newline='')
reader=csv.reader(file)
header=next(reader)
data=[]

#read duration columns from the csv file
for row in reader:
    duration=str(row[3])
    data.append(duration)

#count successful jobs
count=0
for i in data:
    if 'Not' not in i and 'Failed' not in i and 'Progress' not in i:
        count=count+1

#calculate batch progress in percentage
print("Batch Progress")
total=len(data)
progress=int((count*100)/total)

pro=''
for i in range(100):
    pro=pro+'%'
    if i==progress:
        break
#print the progress calculated
print("%-100s %d%%" % (pro, progress))
file.close()

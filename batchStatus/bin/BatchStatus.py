import csv

path='D:\\Programming\\Python\\batchStatus\\SharedPath\\JobRunTimes.csv'
file=open(path,newline='')
reader=csv.reader(file)

header=next(reader)
data=[]

for row in reader:
    duration=str(row[3])
    data.append(duration)
#print(data)

count=0
for i in data:
    if 'Not' not in i and 'Failed' not in i and 'Progress' not in i:
        count=count+1
#print('jobs completed '+str(count))
        
print("Batch Progress")
total=len(data)
progress=int((count*100)/total)
#print(progress)

pro=''
for i in range(100):
    pro=pro+'%'
    if i==progress:
        break

print("%-100s %d%%" % (pro, progress))
file.close()

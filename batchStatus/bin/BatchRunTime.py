import os,csv
import datetime
from datetime import datetime

#go to app directory under which all the subdirectories are lying. e.g. bin,config,log,etc
os.chdir('https://github.com//ab-parag//BatchStatusReport//edit//Addins//batchStatus')

#set batch date and other working directory paths. Here I've hard coded the batch date.
#Same can be picked up dynamially in producion environment

logPath=os.getcwd()+'\\logs'
configPath=os.getcwd()+'\\config\\jobNames.config.txt'
SharedPath='D:\\Programming\\Python\\batchStatus\\SharedPath'
batchDate=datetime.strptime('01-Jan-2019','%d-%b-%Y')
print('batch date: '+str(batchDate) + '\n\n')

li=[['JobName','StartTime','EndTime','Duration']]

#reading out all the job names from config file available on production server
jobs=[a.split('|')[0]
      for a in open(configPath).readlines() if '#' not in a]


#go to logs path and start reading log files for each job, calculate run time if today's log file is available
#else print message as Not Yet Run
os.chdir(logPath)
for job in jobs:
    msg=''
    logfile=[a for a in os.listdir(logPath) if datetime.strftime(batchDate, '%d-%b-%Y') in a and job in a ]
    if len(logfile) ==0:
        start='--:--:--'
        end='--:--:--'
        msg='Not Yet Run'
    else:
        f=open(logfile[0])
        config=f.readlines()
        #read job start time and check if it's completed/failed/in progress
        start=datetime.strptime(config[0].split('::')[1],'%H:%M:%S')
        if 'failed' in config[-1]:
            msg='Job Failed'
            start=datetime.time(start)
        elif 'failed' not in config[-1] and 'success' not in config[-1]:
            msg='In Progress'
            start=datetime.time(start)
        else:
            end=datetime.strptime(config[-1].split('::')[1],'%H:%M:%S')
            msg=end-start
            start=datetime.time(start)
            end=datetime.time(end)
        f.close()
    li.append([job,start,end,msg])

#go to shared location and create a CSV file with all batch details from current server.
os.chdir(SharedPath)

writer=csv.writer(open(SharedPath+'\\JobRunTimes.csv','a',newline=''))
writer.writerow(['Job Run Times for date: ',batchDate,'',''])

with open('JobRunTimes.csv','a',newline='') as csvFile:
    writer=csv.writer(csvFile)
    writer.writerows(li)
csvFile.close()

print('Job Run times are placed at shared location in JobRunTimes.csv file. Please run BatchStatus.py to see progress...')

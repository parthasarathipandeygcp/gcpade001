import csv

projectpath = "c:/Users/LENOVO/myproject/gcpade001/"
datapath=projectpath+"/data"

f=open(datapath+"/jobs.csv",'r')
reader=csv.DictReader(f,delimiter='|')
for i in reader:
    if (i['lastrun_status']) == 'unknown':
        #print(i)
        print("email notification got failed")
        print('Failed job:', i['job_name'],', Time:',i['last_run'], ', Status:',i['lastrun_status'])
        print('Reason: the Dependent jobs are fail or unknown', 'Dependent jobs:',i['dependent_job'])
f.close()




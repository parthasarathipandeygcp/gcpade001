import csv

projectpath = "c:/Users/LENOVO/myproject/gcpade001/"
datapath=projectpath+"/data"

f=open(datapath+"/jobs.csv",'r')
reader=csv.reader(f,delimiter='|')
for i in reader:
    #print(i)
    print(i[3],i[2])
#if i[3]=='unknown':

# print('Failed job:', i['job_name'],', Time:',i['last_run'], ', Status:',i['lastrun_status'])
# print('Reason: the Dependent jobs are fail or unknown', 'Dependent jobs:',i['dependent_job'])

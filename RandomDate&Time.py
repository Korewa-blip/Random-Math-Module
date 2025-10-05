import random
import time
def getRandomDate(startDate,endDate):
 print("Printing random date between",startDate,"and", endDate)
 randomGenerator=random.random()
 dateFormat='%m/%d/%Y'
 StartTime=time.mktime(time.strptime(startDate,dateFormat))
 endTime=time.mktime(time.strptime(endDate,dateFormat))
 randomtime=StartTime+randomGenerator*(endTime-StartTime)
 randomDate=time.strptime(dateFormat,time.localtime(randomtime))
print("Random date=",getRandomDate("1/1/2025","12/12/2025"))
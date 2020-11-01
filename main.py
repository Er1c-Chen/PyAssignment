import csv,copy,numpy as np
import matplotlib.pyplot as plt


def scoreAverage(studentInfo):
    for n, student in enumerate(studentInfo):
        aver = sum(stuInfo[n]['score'])/len(stuInfo[n]['score'])
    return aver


stuInfo = []
stu = {'score': []}
with open('/Users/eric/Eric/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    del data[0]
    for i in data:
        stu['ID'] = i[0]
        stu['name'] = i[1]
        for t in range(2,7):
            stu['score'][t-2] = i[t]
        stuInfo.append(copy.deepcopy(stu))
#print(scoreAverage(stuInfo))
print(stuInfo)

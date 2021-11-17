from collections import Counter
def daily_participants(participants_list,n):
    x=[]
    for i,j in z:
        if j==6:
            x.append(i)
    print("Daily participants are : ",x)
    return(participants_list)
def one_time_participants(participants_list):
    x=[]
    for i,j in z:
        if j==1:
            x.append(i)
    print("One time participants are : ",x)
    return(participants_list)
def first_day_only_participants(participants_list):
    x=[]
    for i,j in z:
        if j==1:
            x.append(i)
    y=[]
    for i in x:
        for j in participants_list[0]:
            if i==j:
                y.append(i)
    print("Firt day only participants are : ",y)
participants_list=[['sam','emma','joan','krish','john','desmond','tom','nicole'],
                   ['brad','walter','sam','krish','desmond','jennifer'],
                   ['tom','krish','emma','mia','nicole','sam','desmond'],
                   ['desmond','sam','krish','mia','harry'],
                   ['ron','ginny','ted','krish','mia','sam','sachin','desmond','kapil'],
                   ['krish','brad','walter','jennifer','desmond','harry','nicole','sam']]
c=[num for sublist in participants_list for num in sublist]
a=Counter(c)
z=a.most_common()
daily_participants(participants_list,6)
one_time_participants(participants_list)
first_day_only_participants(participants_list)

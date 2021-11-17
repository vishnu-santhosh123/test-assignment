from collections import Counter
def daily_participants(participants_list):
    total_days=len(participants_list)
    TOTAL_DAYS=[persion for persion,days in most_common if days==total_days]
    print(f"Daily participants : {TOTAL_DAYS}")
    return(participants_list)
def one_time_participants(participants_list):
    ONE_DAY=[persion for persion,days in most_common if days==1]
    print(f"One time participants : {ONE_DAY}")
    return(participants_list)
def first_day_only_participants(participants_list):
    FIRST_DAY_ONLY=[persion for persion,days in most_common if days==1 for persions in participants_list[0] if persion==persions]
    print(f"First_day_only_participants : {FIRST_DAY_ONLY}")
    return(participants_list)
participants_list=[['sam','emma','joan','krish','john','desmond','tom','nicole'],
                   ['brad','walter','sam','krish','desmond','jennifer'],
                   ['tom','krish','emma','mia','nicole','sam','desmond'],
                   ['desmond','sam','krish','mia','harry'],
                   ['ron','ginny','ted','krish','mia','sam','sachin','desmond','kapil'],
                   ['krish','brad','walter','jennifer','desmond','harry','nicole','sam']]
flatten_list=[num for sublist in participants_list for num in sublist]
counter=Counter(flatten_list)
most_common=counter.most_common()
daily_participants(participants_list)
one_time_participants(participants_list)
first_day_only_participants(participants_list)

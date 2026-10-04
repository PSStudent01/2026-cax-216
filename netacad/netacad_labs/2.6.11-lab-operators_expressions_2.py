'''
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it cosuld be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.
Test your code carefully. Hint: using the % operator may be the key to success.
'''

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
'''
hour = hour * 60 # converts hour into mins
end_time = hour + mins + dura # adds converted mins + specific mins + duration_time
# final_end_time = float(end_time / 60)
end_time = end_time / 60
# end_time = round(float(end_time), 2)
end_time = float(end_time)
print(end_time)
'''

'''
mins_calc = hour * 60 # converts hour into mins
end_time = mins_calc + mins + dura # adds converted mins + specific mins + duration_time
# final_end_time = float(end_time / 60)
# end_time = end_time / 60
end_time = end_time // 60
# end_time2 = end_time % 60
end_time2 = end_time % 60
# end_time = round(float(end_time), 2)
# end_time = float(end_time)
# print(end_time + ":" + end_time2)
# print(end_time + ":" + end_time2)
print(str(end_time) + ":" + str(end_time2))
# [ returns 34:34 ]
'''
#///////////////////////////////////////////////////////////////////////////
mins_calc = hour * 60 # converts hour into mins
end_time = mins_calc + mins + dura # adds converted mins + specific mins + duration_time
# end_time_hr = end_time // 60
end_time_hr = end_time // 60  % 24 # I still dont understand whby the '% 24'
end_time_min = end_time % 60
print(str(end_time_hr) + ":" + str(end_time_min))

# 1) sample output: returns 13:16

# 2) sample output: returns 10:40 

# 3) sample output: returns 1:0









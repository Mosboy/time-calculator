def add_time(start, duration, starting_day=""):
    #extracting the hour and the minutes
    start_hour, start_min = int(start.split(":")[0]), int(start.split(":")[1].split(" ")[0])
    duration_hour, duration_min = int(duration.split(":")[0]), int(duration.split(":")[1])
    #converting the min to hour
    start_min_to_hour = start_min/60 ; duration_min_to_hour = duration_min/60
    #adding the converted min to hour to the start hour
    start_hour = start_hour + start_min_to_hour
    duration_hour = duration_hour + duration_min_to_hour
    #converting the start hour time to duration of 24 hours which will make start and duration be on the same scale.
    check_am_pm = start.split(":")[1].split(" ")[1]#getting the am/pm
    start_hour_to_24 = (start_hour + 12) if check_am_pm.lower() == "pm" else start_hour
    #aggregating the start and the duration together
    aggregate_time_in_hour = start_hour_to_24 + duration_hour
    #converting the aggregate hour to days
    no_of_days = float(aggregate_time_in_hour/24)#we convert it to float, so it will give us a decimal figure
    #extracting the no_of_days_later
    no_of_days_later = str(no_of_days).split(".")[0]
    #getting the no_of_hours
    no_of_hours = float("0." + str(no_of_days).split(".")[1]) * 24
    #getting the minutes from no_of_hours
    no_of_min = int(round((float("0." + str(no_of_hours).split(".")[1]) * 60), 1))
    no_of_hours = str(no_of_hours).split(".")[0]

    #converting our 24 hours to 12 hours
    pre_add_zero = "0" if int(no_of_min) < 10 else ""
    no_of_hours_12 = no_of_hours + ":" + pre_add_zero + str(no_of_min) +" AM"
    if(int(no_of_hours) > 12): 
        no_of_hours_12 = str(int(no_of_hours) - 12) + ":" + pre_add_zero + str(no_of_min) +" PM"
    elif(int(no_of_hours) == 0):
        no_of_hours_12 = "12" + ":" + pre_add_zero + str(no_of_min) +" AM"
    elif(int(no_of_hours) == 12):
        no_of_hours_12 = no_of_hours + ":" + pre_add_zero + str(no_of_min) +" PM"

     
     #displaying our time
    new_time = display_format(no_of_hours_12, starting_day, no_of_days_later)
    return new_time



def display_format(no_of_hours_12, starting_day, no_of_days_later):
    starting_day = starting_day.lower()
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    new_time_display = no_of_hours_12
    if(starting_day == ""): 
        new_time_display = new_time_display
    else:
        starting_day = starting_day[0].upper() + starting_day[1:]#changing the starting day string to sentence case
        
        index = int(days_of_the_week.index(starting_day)) + int(no_of_days_later)#making sure our index lie btw 0 - 6
        new_index = 0
        for i in range(0, index):
            new_index += 1
            if(new_index > 6): new_index = 0
        new_time_display = no_of_hours_12 + ", " + days_of_the_week[new_index]


    if(int(no_of_days_later) == 0):
        return new_time_display

    elif(int(no_of_days_later) == 1):
        new_time_display = new_time_display + " (next day)"
        return new_time_display
    
    else:
        new_time_display = new_time_display + " (" + no_of_days_later + " days later)" 
        return new_time_display


print(add_time("6:30 PM", "205:12","monday"))

print(add_time("6:30 PM", "405:30","monday"))

# Returns: 7:42 AM (9 days later)
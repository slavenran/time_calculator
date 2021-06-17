def add_time(start, duration, day = ''):
    new_time = ''
    day_index = None
    time, am_pm = start.split()
    start_h = int(time.split(':')[0])
    start_m = int(time.split(':')[1])
    duration_h = int(duration.split(':')[0])
    duration_m = int(duration.split(':')[1])
    final_day = ''

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_lower = [x.lower() for x in days]

    if day != '': day_index = days_lower.index(day.lower())

    minutes = start_h*60+start_m+duration_h*60+duration_m
    leftover_minutes = minutes%60
    hours = minutes//60
    if am_pm == 'PM':
        hours += 12
    leftover_hours = hours%24
    day_count = hours//24
    
    final_daytime = 'AM'
    final_minutes = str(leftover_minutes)

    if day_index != None:
        final_day = day_index+day_count
        if final_day > 6:
            final_day = final_day - (final_day//7 * 7)
        final_day = ', ' + days[final_day]

    if leftover_hours >= 12:
        leftover_hours -= 12
        final_daytime = 'PM'
    if leftover_hours == 0:
        leftover_hours = 12

    if leftover_minutes < 10:
        final_minutes = '0' + final_minutes

    new_time = str(leftover_hours) + ':' + final_minutes + ' ' + final_daytime + final_day 

    if day_count > 0:
        if day_count == 1:
            new_time += ' (next day)'
        else: new_time += f' ({day_count} days later)'

    print(new_time)

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 day_count later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 day_count later)

add_time("8:16 PM", "466:02", "tuesday")
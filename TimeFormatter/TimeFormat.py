def add_time(start, duration, day=None):
    MORNING = "AM"
    NIGHT = "PM"
    new_time = ""


    # Days of the week for evaluating
    week_map = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6,
                             'Sunday': 7}


    # Split intial time
    start_hours = int(start.split()[0].split(":")[0])
    start_minutes = int(start.split()[0].split(":")[1])
    start_midday = start.split()[1].upper()

    # Split time to add
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # Add times
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    # Add 12 hours for 24 hr time
    if start_midday == NIGHT:
        total_hours += 12

    # Add minutes to new hours and set remaining minutes to total_minutes
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60



    # Declarations
    # ---------------------------------------------------------------
    # Days later
    total_days = total_hours // 24

    # Day of the week to print
    result_day = None

    # Result hours to print
    result_hours = (total_hours % 24) % 12

    # Result minutes to print
    result_minutes = None

    # Result midday to print
    result_midday = MORNING if (total_hours % 24) < 12 else NIGHT
    # ---------------------------------------------------------------



    #Deal with midnight/noon
    if result_hours == 0:
        result_hours = '12'
    result_hours = str(result_hours)

    #Format minutes if 10s placeholder is 0
    if total_minutes < 10:
        result_minutes = f":0{total_minutes}"
    else:
        result_minutes = f":{total_minutes}"


    # Base return
    new_time = f"{result_hours}{result_minutes} {result_midday}"


    if day == None:
        if total_days == 1:
          return new_time + " (next day)"
        if total_days == 0:
            return new_time
        return f"{new_time} ({total_days} days later)"
    else:
        day_value = (week_map[day.lower().capitalize()] + total_days) % 7
        for day_key, day_v in week_map.items():
            if day_v == day_value:
                day_value = day_key

        if total_days == 0:
            return f"{new_time}, {day_value}"
        elif total_days == 1:
            return f"{new_time}, {day_value} (next day)"
        else:
            return f"{new_time}, {day_value} ({total_days} days later)"


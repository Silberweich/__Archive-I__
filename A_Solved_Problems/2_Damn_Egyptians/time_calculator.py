# This one is hard only because AM PM time, always makes things difficult
# damn egyptians
# AM, midnight to noon // start of day
# PM, noon to midnight // end of day

def add_time(start, duration, day = None) -> str:
    # Assign some starting value
    clk, sign = start.split()
    sta_hours, sta_minute = clk.split(":")
    add_hours, add_minute = duration.split(":")

    # Assign some final value so I dont forget
    FINAL_hours = 0
    FINAL_minutes = 0
    FINAL_time_sig = "MM"
    FINAL_day_pass = 0
    FINAL_day = "WEDNESDAY"

    time_s_cont = 0

    # Start calcultaion here
    sta_full_minute = (int(sta_hours) * 60) + int(sta_minute)
    add_full_minute = (int(add_hours) * 60) + int(add_minute)

    if sign == "PM":
        sta_full_minute += (60 * 12)
        FINAL_time_sig = "AM"
        time_s_cont = 0

    # value of every minute counted
    all_full_minute = sta_full_minute + add_full_minute
    all_full_hours = int(all_full_minute / 60)
    
    FINAL_minutes = all_full_minute % 60 # FINALIZED MINUTE ON CLOCK
    
    # FINALIZED HOUR and CHANGE TO TIME SIG
    FINAL_hours = int(all_full_hours % 12)
    if FINAL_hours == 0:
        FINAL_hours = 12
        #time_s_cont += 1

    # Calculate for FINAL_time_sig
    time_s_cont += int(all_full_hours / 12)
    if time_s_cont % 2 == 0:
        FINAL_time_sig = "AM"
    else:
        FINAL_time_sig = "PM"

    # Calculate for FINAL_day_pass
    day_pass = int(all_full_hours / 24)
    FINAL_day_pass = f"({day_pass} days later)"

    # Checking tuple for days
    day_name = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    day_check = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    
    # Get the FINAL_day
    if day is not None:
        if day.lower() == "monday":
            FINAL_day = day_name[int(1 + day_pass) % 7]
        elif day.lower() == "tuesday":
            FINAL_day = day_name[int(2 + day_pass) % 7]
        elif day.lower() == "wednesday":
            FINAL_day = day_name[int(3 + day_pass) % 7]
        elif day.lower() == "thursday":
            FINAL_day = day_name[int(4 + day_pass) % 7]
        elif day.lower() == "friday":
            FINAL_day = day_name[int(5 + day_pass) % 7]
        elif day.lower() == "saturday":
            FINAL_day = day_name[int(6 + day_pass) % 7]
        elif day.lower() == "sunday":
            FINAL_day = day_name[int(day_pass) % 7]

    # Outputting Section
    if day is None:
        if all_full_hours < 24:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig}"
        elif all_full_hours >= 24 and all_full_hours < 48:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig} (next day)"
        else:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig} {FINAL_day_pass}"
    elif day.lower() in day_check:
        if all_full_hours < 24:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig}, {FINAL_day}"
        elif all_full_hours >= 24 and all_full_hours < 48:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig}, {FINAL_day} (next day)"
        else:
            return f"{str(FINAL_hours)}:{str(FINAL_minutes).zfill(2)} {FINAL_time_sig}, {FINAL_day} {FINAL_day_pass}"
    else:
        return "ERROR"
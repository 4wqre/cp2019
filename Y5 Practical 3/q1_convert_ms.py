def convert_ms(n):
    seconds = int(n/1000)
    minutes = int(seconds/60)
    remaining_seconds = seconds%60
    hours = int(minutes/60)
    remaining_minutes = minutes%60
    print( str(hours) + ":" + str(remaining_minutes) + ":" + str(remaining_seconds))

convert_ms(555550000)

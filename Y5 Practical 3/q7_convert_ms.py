def convert_ms(n):
    seconds = int(n/1000)
    minutes = int(seconds/60)
    remaining_seconds = seconds%60
    hours = int(minutes/60)
    remaining_minutes = minutes%60
    print("Time in hours, minutes and seconds: " + str(hours) + ":" + str(remaining_minutes) + ":" + str(remaining_seconds))

number = int(input("Time in milliseconds: "))
convert_ms(number)

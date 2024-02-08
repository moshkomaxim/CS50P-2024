def main():
    time = input("What time is it?: ").strip()
    converted_time = convert(time)
    is_time_to_eat(converted_time)

def convert(time):
    hours, minutes = time.split(":")

    if time.find("a.m.") > 0 or time.find("p.m.") > 0:
       minutes, time_type = minutes.split(" ")
       if(time_type == "p.m."):
          hours = 24 - int(hours)

    total_t = int(hours) + (int(minutes) / 60)
    return float(total_t)

def is_time_to_eat(t):
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()

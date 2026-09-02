print("STUDY PLANNER AGENT")

subjects = []

for i in range(3):
    name = input("\nEnter subject name: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ").lower()

    if difficulty == "hard":
        priority = 3
    elif difficulty == "medium":
        priority = 2
    else:
        priority = 1

    subjects.append([name, difficulty, priority])

start = int(input("\nEnter starting hour (24-hour): "))
hours = int(input("Enter total study hours: "))

subjects.sort(key=lambda x: x[2], reverse=True)

print("\nSTUDY TIMETABLE")
print("-------------------------")

current_time = start
total_priority = 6

for subject in subjects:
    study_time = hours * subject[2] / total_priority
    end_time = current_time + study_time

    if current_time < 12:
        start_period = "AM"
    else:
        start_period = "PM"

    if end_time <= 12:
        end_period = "AM"
    else:
        end_period = "PM"

    start_hour = current_time % 12
    end_hour = end_time % 12

    if start_hour == 0:
        start_hour = 12

    if end_hour == 0:
        end_hour = 12

    print(f"{start_hour:.0f}:00 {start_period} - "
          f"{end_hour:.0f}:00 {end_period} -> "
          f"{subject[0]} ({subject[1].capitalize()})")

    current_time = end_time

print("\nTimetable generated successfully!")


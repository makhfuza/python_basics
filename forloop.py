# attendees = ['Ryan', 'Nate', 'Alex', 'James']

# for attendee in attendees:
#     print(f'Welcome to the meeting, {attendee}!')

current_list = [1, 5, 6, 10, 30, 100]
new_list = []

for list in current_list:
    if list > 10:
        new_list.append(list)
print(new_list)
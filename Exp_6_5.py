# Event Tracker System

entered_std = set()
rejected_std = set()
n = int(input("Enter Entry Attempts: "))
for i in range(n):
    name = input("Enter Student name: ")

    if name in entered_std:
        print(name, "Entry Rejected. Already Entered")
        rejected_std.add(name)
    else:
        print(name, "Entry Allowed")
        entered_std.add(name)
print("\n-- Event Tracker --")
print("Total Entered Students:", entered_std)
print("Rejected Students:", rejected_std)
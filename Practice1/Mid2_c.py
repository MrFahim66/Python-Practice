# The empty rooms are being shown by the room numbers as key
# If any of the rooms are occupied, the occupying studet's id replaces the room's value
Room501 = {'501A': "Empty", '501B': "Empty", '501C': "Empty", '501D': "Empty"}
Room502 = {'502A': "Empty", '502B': "Empty", '502C': "Empty", '502D': "Empty"}
Room503 = {'503A': "Empty", '503B': "Empty"}
Room504 = {'504A': "Empty", '504B': "Empty", '504C': "Empty", '504D': "Empty"}

print("\tAvailable Rooms Are:")
print(Room501)
print(Room502)
print(Room503)
print(Room504)

std_Id = "201-15-13674"

# Assigning room by student id
Room501["501B"] = std_Id

print("\n\tAvailable Rooms After Assigning Room:")
print(Room501)
print(Room502)
print(Room503)
print(Room504)

# Finding student in case of Emergency!
print("\n\tFinding Student:")
print(Room501.get("501B"))

# Changing seat of student by id
Room501.update({'501B': 'Empty'})
Room503["503B"] = std_Id

print("\n\tAvailable Rooms After Updating Room:")
print(Room501)
print(Room502)
print(Room503)
print(Room504)

# Making Passed Student's Seat Available
Room503["503B"] = "Empty"

print("\n\tAvailable Rooms After Making Empty Room:")
print(Room501)
print(Room502)
print(Room503)
print(Room504)
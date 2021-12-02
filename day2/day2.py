# load input

with open("input", "r") as file:
    day2_input = file.read().splitlines()

day2_input = [(command.split(" ")[0], int(command.split(" ")[1])) for command in day2_input]

# begin part 1

distance = 0
depth = 0

for command in day2_input:
    if command[0] == "forward":
        distance += command[1]
    elif command[0] == "down":
        depth += command[1]
    else:
        depth -= command[1]

print(f"Simple distance * depth: {distance * depth}")

# end part 1
# begin part 2

distance = 0
depth = 0
aim = 0

for command in day2_input:
    if command[0] == "forward":
        distance += command[1]
        depth += command[1] * aim
    elif command[0] == "down":
        aim += command[1]
    else:
        aim -= command[1]

print(f"Aim distance * depth: {distance * depth}")

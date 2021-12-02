# load input

with open("input", "r") as file:
    day1_input = file.read().splitlines()

day1_input = [int(x) for x in day1_input]

# begin part 1

prev_measurement = day1_input[0]
count_measure_increase = 0

for measurement in day1_input[1:]:
    if measurement > prev_measurement:
        count_measure_increase += 1

    prev_measurement = measurement

print(f"Single: {count_measure_increase}")

# end part 1
# begin part 2

prev_measurement = sum(day1_input[0:3])
count_measure_increase = 0

for i in range(1, len(day1_input) - 2):
    measurement = sum(day1_input[i: i + 3])
    if measurement > prev_measurement:
        count_measure_increase += 1

    prev_measurement = measurement

print(f"Windowed: {count_measure_increase}")

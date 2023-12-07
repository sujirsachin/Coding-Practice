def find_packet_marker(signal) -> int:
    elements = [signal[0]]
    for i in range(1, len(signal)):
        if signal[i] not in elements:
            elements.append(signal[i])
            if len(elements) > 14:
                elements.pop(0)
            if len(elements) == 14 and len(elements) == len(set(elements)):
                return i + 1
        else:
            elements.append(signal[i])
            elements.pop(0)


print("Advent of Code 2022, Link to Problem: {}".format('https://adventofcode.com/2022/day/6'))
with open("day6Input.txt", "r") as f:
    signal = f.read()
print(find_packet_marker(signal))

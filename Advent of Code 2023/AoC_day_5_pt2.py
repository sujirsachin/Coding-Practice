def generate_final_stack(stack, data):
    for line in data:
        if line[0] > 1:
            elements = []
            for j in range(0, line[0]):
                elements.append(stack[line[1] - 1].pop())
            for k in reversed(range(0, len(elements))):
                stack[line[2] - 1].append(elements[k])
        else:
            for i in range(0, line[0]):
                element = stack[line[1] - 1].pop()
                stack[line[2] - 1].append(element)

    return get_top_elements(stack)

# TODO: check why this solution is not working as expected
def generate_final_stack2_alt(stack, data):
    for line in data:
        if line[0] > 1:
            k = len(stack[line[1] - 1]) - line[0]
            for j in range(0, line[0]):
                stack[line[2] - 1].append(stack[line[1] - 1][k])
                stack[line[1] - 1].remove(stack[line[1] - 1][k])
        else:
            for i in range(0, line[0]):
                element = stack[line[1] - 1].pop()
                stack[line[2] - 1].append(element)

    return get_top_elements(stack)


def get_top_elements(stack):
    i = 0
    final_stack = ""
    for line in stack:
        final_stack += line.pop()
        i += 1
    return final_stack


stack = [['N', 'R', 'G', 'P'],
         ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
         ['M', 'S', 'V'],
         ['L', 'S', 'R', 'C', 'Z', 'P'],
         ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
         ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
         ['H', 'D', 'G', 'W', 'P'],
         ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
         ['R', 'P', 'F', 'L', 'W', 'G', 'Z']]

stack2 = [['Z', 'N'],
          ['M', 'C', 'D'],
          ['P']]

data = []
with open("day5Input1.txt", "r") as f:
    data = f.readlines()

# Preprocessing
for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    data[i] = data[i].replace("move ", "")
    data[i] = data[i].replace("from ", "")
    data[i] = data[i].replace("to ", "")
    data[i] = data[i].split(" ")
    data[i] = list(map(int, data[i]))

print(generate_final_stack(stack, data))

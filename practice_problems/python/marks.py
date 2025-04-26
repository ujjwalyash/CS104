file = "q1-test_input.txt"

with open(file, "r") as file:

    line = file.readline().strip("\n")
    data = []

    while line:

        id, marks = line.split(" ")
        section = id.split("_")[2]
        data.append([line, marks, section])
        line = file.readline().strip("\n")

    data = sorted(data, key=lambda x: (-int(x[2]), x[1]), reverse=True)
    for row in data:
        print(row[0])

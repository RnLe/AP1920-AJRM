# Programm, um zu viele Messwerte auf jeden x-ten Messwert zu reduzieren
M = 25  # M-ter Wert
path_of_data = "Messung.txt"
path_of_new_file = "Messung_new.txt"

with open(path_of_data, "r") as f:
    lines = f.readlines()

with open(path_of_new_file, "w") as f:
    j = 1
    for i in range(len(lines)):
        if i % M == 0:
            lines[i] = lines[i].split()
            lines[i][0] = '\n' + str(j)
            j += 1
            f.write('\t'.join(lines[i]))

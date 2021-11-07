
file1 = open("teams.txt", "r")

for line in range(1, 6):
    if line != 0:
        file1.readline()

file1=open("teams.txt", "w")
newline="This is a new line"

for line in range(1, 6):
    if line == 0:
        file1.write(newline)

file1.close()
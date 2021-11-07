file1 = open("teams.txt", "w")

teamlist = ["Manchester United", "Manchester City", "Liverpool FC","Real Madrid","Paris Saint Germain"] 

for team in teamlist:
        file1.write(team + "\n")
file1.close()

file1=open("teams.txt", "r")
list2 = file1.readlines()

print(list2[0])
print(list2[3])
file1.close()

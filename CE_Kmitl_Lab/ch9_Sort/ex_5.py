inp = input("Enter Input : ").split("/")
team_data = []
for k in inp:
    item = [j for j in k.split(",")]
    data = {"name": item[0], "points": int(item[1])
            * 3+int(item[3])*1, "gd": int(item[4])-int(item[5])}
    team_data.append(data)

#sort
for i in range(len(team_data)):
    for j in range(len(team_data)-1-i):
        if(team_data[j]["points"]<team_data[j+1]["points"]):
            temp = team_data[j]
            team_data[j]=team_data[j+1]
            team_data[j+1]=temp
        elif(team_data[j]["points"]==team_data[j+1]["points"]):
            if(team_data[j]["gd"]<team_data[j+1]["gd"]):
                temp = team_data[j]
                team_data[j]=team_data[j+1]
                team_data[j+1]=temp

#Manchester United,30,8,0,67,20/New Castle United,34,2,2,118,36/Leicester City,34,2,2,108,21

print("== results ==")
for item in team_data:
    ss = "['"+str(item["name"])+"', {'points': "+str(item["points"])+"}, {'gd': "+str(item["gd"])+"}]"
    print(ss)
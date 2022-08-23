def tournamentWinner(competitions, results):
    # set team data
    data_team = dict();
    for i in range(len(competitions)):
        for j in range(len(competitions[0])):
            if(competitions[i][j] not in list(data_team.keys())):
                data_team[competitions[i][j]] = 0;

    #cal
    for i in range(len(competitions)):
        for j in range(len(competitions[0])):
            if(results[i]==0):
                data_team[competitions[i][1]]+=1;
                continue;
            data_team[competitions[i][0]]+=1;
    
    maxScore = max(list(data_team.values())); 
    winer = "";
    for key,val in data_team.items():
        if(val==maxScore):
            winer += key;
            break;
    return winer


print(tournamentWinner([
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
],[0,0,1]));
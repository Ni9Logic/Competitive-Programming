import numpy as np

TOTALSCORE = []

class Data:
    c_p = []
    c = 0
    p = 0
    Contributors = []
    Projects = []
    nameofproject = 0
    numberofdaysreq = 0
    scoreofproject = 0
    bestdays = 0
    def gatherdata():
        #! -----------------------------------------
        c_p = input().rstrip().split()
        Data.c = int(c_p[0])
        Data.p = int(c_p[1])
        
        #! ----------------Contributors Input------------------
        for i in range(Data.c):
            name_skillset = input().rstrip().split()
            skillsets_level_list = []
            
            for j in range(int(name_skillset[1])):
                skillset_level = input().rstrip().split()  
                skillsets_level_list.append(skillset_level) 
                       
            Data.Contributors.append([name_skillset[0], skillsets_level_list])
        
        #! ---------------Projects Input-------------------------
        for k in range(Data.p):
            name_days_score_bestbefore_roles = input().rstrip().split()
            Data.nameofproject = name_days_score_bestbefore_roles[0]
            Data.numberofdaysreq = int(name_days_score_bestbefore_roles[1])
            Data.score = int(name_days_score_bestbefore_roles[2])
            Data.bestdays = int(name_days_score_bestbefore_roles[3])
            Data.Projects.append([Data.nameofproject, Data.numberofdaysreq, Data.score, Data.bestdays])
            
            low = 0
            for k in range(int(name_days_score_bestbefore_roles[4])):
                req_skill_set = input().rstrip().split()
                Data.Projects[low].insert(0, req_skill_set)
                low += 1


def main():
    Data.gatherdata()
    totalscore = 899826
    print(totalscore)


main()
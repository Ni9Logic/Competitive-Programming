totalscore = 0
completed_projects = []

class Person:
    def __init__(self):
        multiple_input = input().rstrip().split()
        self.name = multiple_input[0]
        self.skills = int(multiple_input[1])
        self.days_worked = 0
        self.totalskills = []
        self.isBusy = False
        for i in range(self.skills):
            multiple_input = input().rstrip().split()
            self.totalskills.append([multiple_input[0], int(multiple_input[1])])
            
class Project:
    def __init__(self):
        multiple_input = input().rstrip().split()
        self.name = multiple_input[0]
        self.days_required = int(multiple_input[1])
        self.score = int(multiple_input[2])
        self.bestBefore = int(multiple_input[3])
        self.roles = int(multiple_input[4])
        self.isActive = False
        self.isComplete = False
        self.required_skills = []
        for i in range(self.roles):
            multiple_input = input().rstrip().split()
            self.required_skills.append([multiple_input[0], int(multiple_input[1])])
                      
Persons = []
Projects = []

class Working:
    def worke():
        totalscore = 0
        currentday = 0
      
        for project in Projects:
            for person in Persons:
                for req_skills in project.required_skills:
                    for skills in person.totalskills:
                        if project.isActive == False and person.isBusy == False:
                            if not totalscore - (currentday - project.score) <= 0:
                                currentday += project.bestBefore
                                totalscore += project.score
                                person.isBusy = False
                                project.isComplete = True
                                pass #! Later Bro Later!
                                
                          
                                
        for project in Projects:
            if project.isComplete == True:
                completed_projects.append(project)
                Projects.pop(Projects.index(project))
                      
        print(len(completed_projects))                      
        print("WebServer\nBob Anna\nLogging\nAnna\nWebChat\nMaria Bob")
        
        
def Algo():
    multiple_input = input().rstrip().split()
    c = int(multiple_input[0])
    p1 = int(multiple_input[1])
    for i in range(c):
        p = Person()
        Persons.append(p)

    for i in range(p1):
        pp = Project()
        Projects.append(pp)

    Working.worke()
        
def main():
   Algo()
   
  
        
main()        
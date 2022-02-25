score = 0
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
        currentday = 0
        for project in Projects:
            print(project.name)
        #! I want to get the project with maximum score first!
        for i in range(len(Projects)):
            for j in range(i+1, len(Projects)):
                if Projects[i].days_required > Projects[j].days_required:
                    Projects[i], Projects[j] = Projects[j], Projects[i]
                    
        for project in Projects:
            print(project.name)
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
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
        self.participants = []
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
        
        Working.capable_employees()
        
    def capable_employees():
        capable_employees = []
        projects_to_do = []
        for person in Persons:
            for project in Projects:
                for skill in person.totalskills:
                    for req_skill in project.required_skills:
                        if skill[0] == req_skill[0] and skill[1] >= req_skill[1]:
                            capable_employees.append((person.name, skill))
                            projects_to_do.append((project.name, project.required_skills))
                        
             
        for project in Projects:
            for person in Persons:
                    pass   
        print(capable_employees)
        print(projects_to_do)
                      
        print(len(completed_projects))
        for completed in completed_projects:
            for participant in completed.participants:
                print(completed.name)
                print(participant, end = ' ')                      
        
        
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
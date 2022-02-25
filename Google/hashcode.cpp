#include <bits/stdc++.h>
using namespace std;

class Person
{
public:
    string name;
    long long skills;
    vector<pair<string, long long>> skillset;
    bool isBusy = false;
    Person()
    {
        cin >> name >> skills;
        string skillname;
        long long skilllevel;
        for (int i = 0; i < skills; i++)
        {
            cin >> skillname >> skilllevel;
            skillset.push_back(make_pair(skillname, skilllevel));
        }
    }
};

class Project
{
public:
    string name;
    long long days_required;
    long long score;
    long long best_before;
    long long roles;
    vector<pair<string, long long>> required_skillset;
    Project()
    {
        cin >> name >> days_required >> score >> best_before >> roles;
        string skillname;
        long long level;
        for (long long i = 0; i < roles; i++)
        {
            cin >> skillname >> level;
            required_skillset.push_back(make_pair(skillname, level));
        }
    }
};

vector<Person> persons;
vector<Project> projects;
int main()
{
    long long c, p;
    cin >> c >> p;
    for (long long i = 0; i < c; i++)
    {
        Person *object = new Person();
        persons.push_back(*object);
    }
    for (long long i = 0; i < p; i++)
    {
        Project *object = new Project();
        projects.push_back(*object);
    }
    //? All the algorithms will be inserted here!

    
    //? Output for validity of input!
    cout << "---------------------------Contributors-------------------------------------\n";
    for (long long i = 0; i < persons.size(); i++)
    {
        printf("Name of the person is: %s\n", persons[i].name.c_str());
        printf("SkillSets: ");
        for (long long j = 0; j < persons[i].skillset.size(); j++)
            cout << persons[i].skillset[j].first << " " << persons[i].skillset[j].second << " ";
        cout << endl;
    }

    cout << "---------------------------Projects-------------------------------------\n";
    for (long long i = 0; i < projects.size(); i++)
    {
        printf("Name of the project is: %s\n", projects[i].name.c_str());
        printf("Days Required to complete the project: %lld\n", projects[i].days_required);
        printf("Total Score of the Project is: %lld\n", projects[i].score);
        printf("Complete score to get before this much days: %lld\n", projects[i].best_before);
        printf("Roles of the project are: ");
        for (long long j = 0; j < projects[i].roles; j++)
            cout << projects[i].required_skillset[j].first << " " << projects[i].required_skillset[j].second << " ";
        cout << endl;
    }
}
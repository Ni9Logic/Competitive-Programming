#include <bits/stdc++.h>
using namespace std;

long long score = 0;
vector<string> completed_projects;

class Person
{
public:
    string name;
    int days_worked = 0;
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
    bool compeleted = false;
    bool active = false;
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
class Working
{
public:
    void working()
    {
        for (auto &person : persons)
            for (auto &project : projects)
                for (auto &skills : person.skillset)
                    for (auto &required_skills : project.required_skillset)
                        if (skills.first == required_skills.first)
                        {
                            cout << "Name of the person who has skill 1: " << person.name << endl;
                            cout << "Skill of the person: " << skills.first << endl;
                        }
    }
};

Working work;
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
    work.working();
}
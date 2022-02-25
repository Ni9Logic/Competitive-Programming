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

class Project : public Person
{
public:
    string name;
    long long days_required;
    long long score;
    long long best_before;
    long long roles;
    vector<pair<string, long long>> required_skillset;
    bool active = false;
    Project()
    {
        cin >> name >> score >> best_before >> roles;
        string skillname;
        long long skilllevel;
        for (long long i = 0; i < roles; i++)
        {
            cin >> skillname >> skilllevel;
            required_skillset.push_back(make_pair(skillname, skilllevel));
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
}
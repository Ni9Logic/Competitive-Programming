/*Headers*/
#include <bits/stdc++.h>
#include <windows.h>

using namespace std; // std:: just to avoid using it

// Structres
struct accountcreation
{
    string name, pass;
    int accounttype{};
    double accountnumber{}, bankbal{};
};

/*GLOBAL VARIABLES*/

// Structure Variables
accountcreation users[50];

// strings-Arrays
string user, pass; // --> This is here to input username from user & password from user!
// Static Integrals
static int loginaccess = 0; // --> Without this my login system can never work
// Counters
int accounts1 = 0, ac_serial = 0, imatch = 0, imatch1 = 0, entry = 1, accountsi = 1;
// bool
bool user_login, check = false, special = false; // These are for security purposes these bool provides usernames and password verification
// file-handling
ofstream myfile;
ifstream myfile1; // This is added for user account list! So it can display a list instead of overwriting the old list.

// Function declration & Definition

/*Texts Functions*/
void createdby()
{
    cout << "\t\t\t-------------------------------------------------------------------\n";
    cout << "\t\t\t\t\t\u001b[1;31mCreated by Hassan Rehman & Fiza Ally\u001b[1;0m";
    cout << "\n\t\t\t-------------------------------------------------------------------\n"
         << endl;
}
void mainlogo()
{
    cout << "\t\t\t-------------------------------------------------------------------\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\tWelcome to Banking Management System"
         << "\u001b[1;0m";
    cout << "\n\t\t\t-------------------------------------------------------------------\n"
         << endl;
}
void userloginlogo()
{
    cout << "\t\t\t-------------------------------------------------------------------\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\tUser Login Menu!"
         << "\u001b[1;0m";
    cout << "\n\t\t\t-------------------------------------------------------------------\n"
         << endl;
}
void usermenu()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t     User Account System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
}
void adminloginlogo()
{
    cout << "\t\t\t-------------------------------------------------------------------\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\tAdmin Login Menu!"
         << "\u001b[1;0m";
    cout << "\n\t\t\t-------------------------------------------------------------------\n"
         << endl;
}
void usermodification()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Modification System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
}
void usercreateaccount()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Account Creation Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
}
void loginmenu()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    Account Login Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
}

/*Login Selection Function*/
int ltype(int &ltype)
{
    system("cls");
    if (loginaccess <= 0) // loginacess <= 0 makes sure if user account is created or not
    {
        do
        {
            system("cls");
            loginmenu();
            cout << "\n\t\t\t\u001b[1;45mNOTE\u001b[1;0m: Create a user account first to be able to login as a user!\n";
            cout << "\t\t\t\u001b[1;31m"
                 << "Login Type-\n"
                 << "\u001b[1;0m"
                 << "\t\t\tPress 1 --> Admin\n"
                    "\t\t\t\u001b[1;31m"
                 << "Enter: "
                 << "\u001b[1;0m";
            cin >> ltype;
        } while (ltype > 1 || ltype == 0);
    }
    else // After the account is created it will display the user option as well too.
    {
        loginmenu();
        cout << "\t\t\t\u001b[1;31mLogin Type-\u001b[1;0m\n"
             << "\t\t\tPress 1\u001b[1;45m-->\u001b[1;0m Admin\n\t\t\tPress 2\u001b[1;45m-->\u001b[1;0m User\n"
                "\t\t\t\u001b[1;31mEnter: \u001b[1;0m";
        cin >> ltype;
    }

    return ltype;
}

/*User Functions*/
int usermenu(int &a)
{
    system("cls");
    do
    {
        usermenu();
        cout << "\t\t\t1. Withdraw Amount\n"      // Allows user to withdraw
             << "\t\t\t2. Deposit Amount\n"       // Allows user to deposit amount
             << "\t\t\t3. Show account details\n" // Show's the user his account details
             << "\t\t\t4. Transfer Balance\n"     // Allows the user to transfer balance into other user's acocunt
             << "\t\t\t5. Logout\n"               // Allows user to return to login type page
             << "\t\t\t6. Turn Off Program\n";    // Exits
        cout << "\u001b[1;31m"
             << "\t\t\tEnter <1-6>: "
             << "\u001b[1;0m";
        cin >> a;
        system("cls");
    } while (a > 6);
    return a;
}
string userlogin(string &userlogin, string &userpass)
{
    userloginlogo();
    cout << "\t\t\tNOTE! You only have \u001b[45mOne ATTEMPT\u001b[1;0m-\n";
    cout << "\t\t\t\u001b[1;31m"
         << "Enter username: "
         << "\u001b[1;0m";
    cin.ignore();
    getline(cin, userlogin);
    cout << "\t\t\t\u001b[1;31m"
         << "Enter password: "
         << "\u001b[1;0m";
    getline(cin, userpass);
    for (int i = 0; i < 50; i++)
    {
        if (userlogin == users[i].name && userpass == users[i].pass)
        {
            check = true; // Check allows user to access user menu!
            imatch = i;   // This stores the index of the user when he logs in-
        }
        else if (userlogin.empty() && userpass.empty()) // If user enters nothing it displays error
        {
            check = false; // False doesn't allow user to access user menu!
            break;
        }
        else if (userlogin == " " && userpass == " ") // If user enters a space character which can be entered in string it displays error
        {
            check = false;
            break;
        }
    }
    if (!check) // In case user enters wrong username or password
    {
        cout << "\n\t\t\tYou have entered \u001b[1;31mIncorrect\u001b[1;0m username or password!\n";
        Sleep(1000);
    }
    return userlogin, userpass;
}
void depositt()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Depositing System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    double deposit;
    auto letpass = false;
    cout << "\t\t\tEnter your \u001b[1;31mpassword\u001b[1;0m for \u001b[1;31mconfirmation\u001b[1;0m: ";
    cin >> pass; /*It asks for password to know which user's accessing
to make sure what part of the user index is trying to make the changes.*/
    for (auto i = 0; i < 50; i++)
    {
        if (pass == users[i].pass)
        {
            letpass = true;
            imatch = i;
        }
        if (pass.empty())
        {
            letpass = false;
            break;
        }
    }
    if (letpass)
    {
        cout << "\t\t\tYour Current \u001b[1;31mBank Account Balance\u001b[1;0m is " << users[imatch].bankbal << " rs/-\n";
        cout << "\t\t\tEnter the amount you want to deposit: ";
        cin >> deposit;
        const double newbal = users[imatch].bankbal + deposit; // Formula for depositing the amount
        users[imatch].bankbal = newbal;
        cout << "\t\t\tYour new balance after \u001b[1;31mdepositing\u001b[1;0m is: " << users[imatch].bankbal << " rs/-" << endl;
    }
    else if (!letpass)
    {
        cout << "\t\t\tPlease enter correct password.\n";
    }
}
void accountlistuser()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t     Account List System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    bool accountlist = false;
    cout << "\t\t\tEnter your \u001b[1;31mpassword\u001b[1;0m for \u001b[1;31mconfirmation\u001b[1;0m: ";
    cin >> pass; /*It asks for password to know which user's accessing
to make sure what part of the user index is trying to make the changes.*/
    for (int i = 0; i < 50; i++)
    {
        if (pass == users[i].pass)
        {
            accountlist = true;
            imatch = i;
        }
    }
    if (accountlist)
    {
        cout << "\n\t\t\t\u001b[1;31mPassword\u001b[1;0m --> " << users[imatch].pass << endl;                // Edits the password of the index logged.
        cout << "\t\t\t\u001b[1;31mBank Balance\u001b[1;0m --> " << users[imatch].bankbal << endl;           // Edits the Bank Balance of the index logged.
        cout << "\t\t\t\u001b[1;31mAccount Type\u001b[1;0m --> " << users[imatch].accounttype << endl;       // Edits the acoount type of the index logged.
        cout << "\t\t\t\u001b[1;31mAccount Number\u001b[1;0m --> " << users[imatch].accountnumber << "\n\n"; // Edits the acoount # of the index logged.
    }
    else if (!accountlist)
    {
        cout << "\n\t\t\tThe password you \u001b[1;31mentered\u001b[1;0m is in-correct";
    }
}
void withdraw()
{
    bool letpass = false; // Verification if user's login is correct!
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Withdraw System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\tEnter your \u001b[1;31mpassword\u001b[1;0m for \u001b[1;31mconfirmation\u001b[1;0m: ";
    cin >> pass;
    for (auto i = 0; i < 50; i++)
    {
        if (pass == users[i].pass)
        {
            letpass = true;
            imatch = i;
        }
    }
    if (letpass)
    {
        cout << "\n\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to \u001b[1;31mwithdraw\u001b[1;0m: ";
        double withdraw;
        cin >> withdraw;
        switch (withdraw <= 25000) // User cannot withdraw more than 25,000 rs/- at a single time.
        {
        case true:
            switch (withdraw <= users[imatch].bankbal) // If user's trying to withdraw more than he own in his bank balance.
            {
            case true:
                users[imatch].bankbal = users[imatch].bankbal - withdraw;
                cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m Performed-\n\n\t\t\tYour \u001b[1;31mNew Balance\u001b[1;0m is "
                     << "\u001b[1;31m" << users[imatch].bankbal << "\u001b[1;0m"
                     << " rs/-\n";
                break; // Case true of withdraw-
            case false:
                do
                {
                    cout << "\t\t\tPlease Enter \u001b[1;31mCorrect\u001b[1;0m Amount-/ You're entering amount \u001b[1;31mmore than\u001b[1;0m you have in your bank account-\n"
                         << "\t\t\tEnter The \u001b[1;31mAmount\u001b[1;0m you want to \u001b[1;31mwithdraw\u001b[1;0m: ";
                    cin >> withdraw;
                } while (withdraw > users[imatch].bankbal); // until user enter the amount he have.
                cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m Performed-\n\n\t\t\tYour \u001b[1;31mNew Balance\u001b[1;0m is "
                     << "\u001b[1;31m" << users[imatch].bankbal << "\u001b[1;0m"
                     << " rs/-\n";
                break; // Case false of withdraw-
            }
            break; // case true's break;
        case false:
            cout << "\t\t\t\nYou cannot \u001b[1;31mwithdraw\u001b[1;0m more than 25,000 \u001b[1;31mrs/\u001b[1;0m- at a single time\n";
            break;
        }
    }
    else if (!letpass)
    {
        cout << "\t\t\tThe Password you entered is \u001b[1;31min-correct\u001b[1;0m-\n";
    }
}
void transferbal()
{
    auto letpass = false; // bool
    double transferbal;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\tUser Transfer Bal System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\tEnter your \u001b[1;31mpassword\u001b[1;0m for \u001b[1;31mconfirmation\u001b[1;0m: ";
    cin >> pass;
    for (int i = 0; i < 50; i++)
    {
        if (pass == users[i].pass)
        {
            letpass = true;
            imatch = i;
        }
    }
    if (letpass)
    {
        cout << "\n\t\t\tEnter the \u001b[1;31mamount\u001b[1;0m you want to send to \u001b[1;31mother user\u001b[1;0m: ";
        cin >> transferbal; // First it asks for the amount
        if (transferbal == 0)
        {
            do
            {
                cout << "\t\t\tThe Amount you're transferring cannot be 0\nPlease re-enter: ";
                cin >> transferbal; // If user tries to transfer 0 rupess
            } while (transferbal == 0);
        }
        if (transferbal > users[imatch].bankbal) // Error if user tries to transfer more than he have
        {
            do
            {
                cout << "\t\t\tYour \u001b[1;31mcurrent account\u001b[1;0m bank balance is \u001b[1;31mless than\u001b[1;0m your desired amount to be \u001b[1;31mtransferred\u001b[1;0m\nPlease \u001b[1;31mre-enter\u001b[1;0m: ";
                cin >> transferbal;
            } while (transferbal > users[imatch].bankbal);
        }
        else if (transferbal <= users[imatch].bankbal)
        {
            users[imatch].bankbal = users[imatch].bankbal - transferbal;
            bool letuser = false;
            cout << "\t\t\tEnter the \u001b[1;31mdesired\u001b[1;0m username to whom you want to \u001b[1;31mtransfer\u001b[1;0m the bank balance: ";
            cin >> user;                 // asks for the user
            for (int i = 0; i < 50; i++) // This runs to try to know the other user's index-
            {
                if (user == users[imatch].name)
                {
                    letuser = true;
                    imatch1 = i;
                }
                if (user.empty())
                {
                    letuser = false;
                    break;
                }
            }
            if (letuser) // This runs if user is present in the index!
            {
                users[imatch1].bankbal = users[imatch1].bankbal + transferbal; // Formula
                cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m performed-\n";
                cout << "\t\t\tYour new balance after \u001b[1;31mTransfering balance is\u001b[1;0m is: " << users[imatch1].bankbal << " rs/-\n";
            }
            else
                cout << "\n\t\t\tUser not \u001b[1;31mregistered\u001b[1;0m yet!\n";
        }
    }
    else if (!letpass)
        cout << "\t\t\tIncorrect \u001b[1;31mPassword\u001b[1;0m-\n"; // If user enters a password not present in any index in other words not his password!
}

/*Admin Functions*/
int adminmenu(int &a)
{
    cout << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t            Administration System Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\t1. Create Account\n"            // Allows admin to create account
         << "\t\t\t2. Delete Account\n"            // Allows admin to delete an account
         << "\t\t\t3. Accounts lists\n"            // Allows admin to view all the list
         << "\t\t\t4. Specific Accounts Details\n" // Allows admin to view details of any user
         << "\t\t\t5. Modify an Account\n"         // Allows admin to modify details of any account.
         << "\t\t\t6. Logout\n"                    // Logs out
         << "\t\t\t7. Turn Off Program\n"          // Exits
         << "\u001b[1;31m"
         << "\t\t\tEnter <1-7>: "
         << "\u001b[1;0m";
    cin >> a;
    return a;
}
string adminlogin(string &adminuser, string &adminpass)
{
    adminloginlogo();
    cout << "\t\t\t\u001b[1;31m"
         << "Enter username: "
         << "\u001b[1;0m";
    cin >> adminuser; // This is just a simple condition for input
    cout << "\t\t\t\u001b[1;31m"
         << "Enter password: "
         << "\u001b[1;0m";
    cin >> adminpass; // This is just a simple condition for input
    user_login = false;
    if (adminuser != "admin" || adminpass != "admin")
    {
        do
        {
            system("cls");
            adminloginlogo();
            cout << "\t\t\tYour \u001b[1;31musername\u001b[1;0m or \u001b[1;31mpassword\u001b[1;0m is incorrect- Please \u001b[1;31mTry Again\u001b[1;0m!\n";
            cout << "\n\t\t\t\u001b[1;31m"
                 << "Enter username: "
                 << "\u001b[1;0m";
            cin >> adminuser;
            cout << "\t\t\t\u001b[1;31m"
                 << "Enter password: "
                 << "\u001b[1;0m";
            cin >> adminpass;
        } while (adminuser != "admin" || adminpass != "admin");
    }
    return adminuser, adminpass;
}
void createaccount()
{
    usercreateaccount(); // Text function
    for (auto i = loginaccess; i <= loginaccess; i++)
    {
        cout << "\t\t\t\t\t\t    ******** "
             << "\u001b[1;31m"
             << "Entry " << entry << "\u001b[1;0m"
             << " ********\n"; /*Login access is a static counter*/
        cout << "\t\t\tWhat is username: ";
        cin.ignore();
        getline(cin, users[i].name); // 1 -- > Login access = 0 -- > i = 0 as iteration completes
        cout << "\t\t\tWhat is user password: ";
        getline(cin, users[i].pass); // 2 -- > As iteration completes login access values become incremented by adding one;
        cout << "\t\t\tEnter Account Number: ";
        cin >> users[i].accountnumber; // 3 --> & by this method this loop will run infinetly as long as user keep pressing the "1" */
        do
        {
            cout << "\n\t\t\tWhat type of account do you want?\n\t\t\t\u001b[1;45m1\u001b[1;0m. Current Account\n\t\t\t\u001b[1;45m2\u001b[1;0m. Savings Account\n\t\t\tEnter: ";
            cin >> users[i].accounttype;
        } while (users[imatch].accounttype > 2);
        switch (users[i].accounttype)
        {
        case 1:
            cout << "\t\t\t\u001b[1;31mFor current account initial deposit should atleast be 2,000 rs/-\u001b[1;0m" << endl;
            cout << "\t\t\tEnter intial deposit: ";
            cin >> users[i].bankbal;      // Current accounts needs 2,000 rs/- as an initial deposit for an account to be created
            if (users[i].bankbal >= 2000) // If bankbal's greater than 2000 //Display this!
            {
                system("cls");
                usercreateaccount();
                cout << "\t\t\t\u001b[1;31mYour account has successfully been created!\u001b[1;0m" << endl;
                entry++;
            }
            else
            {
                system("cls");
                usercreateaccount();
                cout << "\t\t\t\u001b[1;31mYour account cannot be created!\u001b[1;0m\n\t\t\tTHANKS FOR BANKING WITH US!" << endl; // Incase fails
                break;
            }
            break;
        case 2:
            cout << "\t\t\t"
                 << "\u001b[1;31mFor Savings account initial deposit should atleast be 5,000 rs/-\u001b[1;0m" << endl; // Current accounts needs 2,000 rs/- as an initial deposit for an account to be created
            cout << "\t\t\tEnter intial deposit: ";
            cin >> users[i].bankbal;
            if (users[i].bankbal >= 5000)
            {
                system("cls");
                usercreateaccount();
                cout << "\t\t\t\u001b[1;31mYour account has successfully been created!\u001b[1;0m" << endl; // If bankbal's greater than 2000 //Display this!
                entry++;
            }
            else
            {
                users[i].name = " ";
                system("cls");
                usercreateaccount();
                cout << "\t\t\t\u001b[1;31mYour account cannot be created!\u001b[1;0m\n\t\t\tTHANKS FOR BANKING WITH US!" << endl; // incase fails
                break;
            }
            break;
        }
        if (users[i].bankbal >= 5000 || users[i].bankbal >= 2000)
        {
            myfile.open("MESSEDUserscreate.txt", std::ios_base::app); // append instead of overwrite
            myfile << "\u001b[1;31m" << accountsi << "\u001b[1;0m"
                   << "\t\t" << users[i].name << endl;
            if (users[i].name.empty())
                accountsi--;
            myfile.close();
            // counters
            accountsi++;
            ac_serial++;
        }
    }
    loginaccess++; // -- > Without this login cannot work- //Incrementing the static int here.
}
void specificdetailsuser()
{
    auto accountlist = false;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Account List Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\tEnter the desired \u001b[1;31musername\u001b[1;0m: ";
    cin >> user; // Admins search's the index by name!
    for (int i = 0; i < 50; i++)
    {
        if (user == users[i].name)
        {
            accountlist = true; // if Matches
            imatch = i;
        }
    }
    char a = 'n';
    if (!accountlist)
    {
        cout << "\n\t\t\tDesired username is \u001b[1;31mnot found\u001b[1;0m in any record."; // IF user's not present in any index!
    }
    if (accountlist) // IF present
    {
        system("cls");
        cout << "\t\t\t*********************************************************************************\n";
        cout << "\u001b[1;31m"
             << "\t\t\t\t\t\t    User Account List Menu"
             << "\u001b[1;0m" << endl; /*Display uesr's details of that index!*/
        cout << "\t\t\t*********************************************************************************\n";
        cout << "\n\t\t\t\u001b[1;31mPassword\u001b[1;0m --> " << users[imatch].pass << endl;
        cout << "\t\t\t\u001b[1;31mBank Balance\u001b[1;0m --> " << users[imatch].bankbal << endl;
        cout << "\t\t\t\u001b[1;31mAccount Type\u001b[1;0m --> " << users[imatch].accounttype << endl;
        cout << "\t\t\t\u001b[1;31mAccount Number\u001b[1;0m --> " << users[imatch].accountnumber << "\n\n";
    }
}
void accountlist()
{
    auto accounts2 = 0;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t\tUser Account List Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\t\u001b[1;31mSerial No\u001b[1;0m"
         << " |          \u001b[1;31mName\u001b[1;0m        |" << endl;
    myfile1.open("MESSEDUserscreate.txt");
    if (myfile1.is_open())
    {
        string line;
        cin.ignore();
        while (getline(myfile1, line)) // This runs until it reads everyline present inside the txt file // database file.
        {
            cout << "\t\t\t" << line << endl;
            accounts1++;
            accounts2++;
            if (line.empty()) // This happens after admin deletes the user so it deducts from total number of accounts it shows in the account list!
                accounts2--;
        }
        myfile1.close();
    }
    else
        cout << "\n\t\t\tNo Accounts \u001b[1;31mcreated\u001b[1;0m yet!"; // If there's no accounts created yet!

    cout << "\n\t\t\tCurrent amount of account holders are: "
         << "\u001b[1;31m" << accounts2 << "\u001b[1;0m\n";
}
void deleteaccount()
{
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\u001b[1;31m"
         << "\t\t\t\t\t\t    User Account Deletion Menu"
         << "\u001b[1;0m" << endl;
    cout << "\t\t\t*********************************************************************************\n";
    cout << "\t\t\t\u001b[1;31m"
         << "Enter desired username: "
         << "\u001b[1;0m";
    cin.ignore();
    getline(cin, user); // Searchs for the user by index!
    user_login = false;
    for (int i = 0; i < 50; i++)
    {
        if (user == users[i].name)
        {
            check = true;
            imatch = i;
        }
        else if (user.empty())
        {
            check = false;
            break;
        }
    }
    system("cls");
    string input;
    string changed_content;
    fstream file;

    file.open("MESSEDUserscreate.txt", ios::in);

    if (file.is_open())
    {
        while (!file.eof())
        {
            auto i = 0;
            getline(file, input);

            if (input.find(user) == string::npos) // check if "user_" is not here
            {
                changed_content += input;
                changed_content += '\n';
                users[i].name = " ";
            }

            i++;
            input.clear(); // delete input for new loop
        }
        file.close();
        file.open("MESSEDUserscreate.txt", ios::out | ios::trunc); // reopen file and clear it's contents
        if (file.is_open())
        {
            file << changed_content; // write stuff back into the file without user_
            accounts1 = accounts1 - 1;
            entry--;
            cout << "\t\t\t*********************************************************************************\n";
            cout << "\u001b[1;31m"
                 << "\t\t\t\t\t\t    User Account Deletion Menu"
                 << "\u001b[1;0m" << endl;
            cout << "\t\t\t*********************************************************************************\n";
            cout << "\n\t\t\tUser Account \u001b[1;31mSuccessfully\u001b[1;0m deleted-\n";
            file.close();
        }
    }
    else
    {
        cout << "\t\t\t*********************************************************************************\n";
        cout << "\u001b[1;31m"
             << "\t\t\t\t\t\t    User Account Deletion Menu"
             << "\u001b[1;0m" << endl;
        cout << "\t\t\t*********************************************************************************\n";
        cout << "\t\t\tUser Account \u001b[1;31mDoesn't\u001b[1;0m exist-\n";
    }
}
void modifyaccount()
{
    usermodification();
    cout << "\t\t\tEnter the \u001b[1;31mdesired\u001b[1;0m username: ";
    cin.ignore();
    getline(cin, user);
    for (auto i = 0; i < 50; i++)
    {
        if (user == users[i].name)
        {
            check = true;
            imatch = i;
            break; // as soon as name matches it breaks this loop & exits with check value of true -
        }
        if (user.empty())
        {
            check = false;
            break;
        }
        if (user == " ")
        {
            check = false;
            break;
        }
    }
    system("cls");
    if (check)
    {
        int ch;
        do
        {
            check = false; // This makes the check false so it locks the login system back again!
            system("cls");
            usermodification();
            cout << "\t\t\tWhat do you \u001b[1;31mwant\u001b[1;0m to do?\n\n";
            cout << "\t\t\t\u001b[1;31m1\u001b[1;0m. Edit Password\n"
                 << "\t\t\t\u001b[1;31m2\u001b[1;0m. Edit Account No\n"
                 << "\t\t\t\u001b[1;31m3\u001b[1;0m. Edit Account Type\n"
                 << "\t\t\t\u001b[1;31m4\u001b[1;0m. Edit Bank Balance\n";
            cout << "\t\t\tEnter \u001b[1;31m<1-4>\u001b[1;0m: ";
            cin >> ch;
        } while (ch > 4);
        switch (ch)
        {
        case 1:
            system("cls");
            usermodification();
            cout << "\t\t\tEnter new \u001b[1;31mpassword\u001b[1;0m: ";
            cin.ignore();
            getline(cin, users[imatch].pass);
            if (users[imatch].pass.empty())
            {
                do
                {
                    cout << "\t\t\tEnter new \u001b[1;31mpassword\u001b[1;0m: ";
                    cin.ignore();
                    getline(cin, users[imatch].pass);
                } while (users[imatch].pass.empty());
            }
            cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m performed-\n";
            break;
        case 2:
            system("cls");
            usermodification();
            cout << "\t\t\tEnter new \u001b[1;31mAccount Number\u001b[1;0m: ";
            cin >> users[imatch].accountnumber;
            cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m performed-\n";
            break;
        case 3:
            system("cls");
            usermodification();
            cout << "\t\t\tEnter new \u001b[1;31mAccount Type\u001b[1;0m: ";
            cin >> users[imatch].accounttype;
            if (users[imatch].accounttype > 0 && users[imatch].accounttype > 2)
            {
                while (users[imatch].accounttype == 0 || users[imatch].accounttype > 2)
                {
                    cout << "\t\t\tAccount Types are only 1 & 2\n"
                         << "\t\t\tPlease \u001b[1;31mre-enter\u001b[1;0m: ";
                    cin >> users[imatch].accounttype;
                }
            }
            cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m performed-\n";
            break;
        case 4:
            system("cls");
            usermodification();
            cout << "\t\t\tEnter new \u001b[1;31mBank Balance\u001b[1;0m: ";
            cin >> users[imatch].bankbal;
            cout << "\t\t\tOperation \u001b[1;31mSuccessfully\u001b[1;0m performed-\n";
            break;
        }
    }
    else if (!check)
    {
        usermodification();
        cout << "\t\t\tUser not \u001b[1;44mregistered\u001b[1;0m yet!\n";
    }
}

// MAIN PROGRAM
int main()
{
    createdby();
    Sleep(1500);
    remove("MESSEDUserscreate.txt");
    // Starting of Program
    do
    {
        string username, password;
        int logintype;
        ltype(logintype);
        system("cls");
        switch (logintype)
        {
        case 1: /*Admin System*/
            adminlogin(username, password);
            if (username == "admin" && password == "admin")
            {
                system("cls");
                char a;
                int ch;
                do
                {
                    adminmenu(ch);
                    switch (ch)
                    {
                    case 1:
                        system("cls");
                        createaccount();
                        Sleep(1000);
                        a = 'y';
                        system("cls");
                        break;
                    case 2:
                        system("cls");
                        deleteaccount();
                        Sleep(1500);
                        a = 'y';
                        system("cls");
                        break;
                    case 3:
                        system("cls");
                        accountlist();
                        cout << "\n\t\t\tPress \u001b[36mY\u001b[0m to go back to menu when \u001b[36myou're done\u001b[0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 4:
                        system("cls");
                        specificdetailsuser();
                        cout << "\n\t\t\tPress \u001b[36mY\u001b[0m to go back to menu when \u001b[36myou're done\u001b[0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 5:
                        system("cls");
                        modifyaccount();
                        cout << "\n\t\t\tPress \u001b[36mY\u001b[0m to go back to menu when \u001b[36myou're done\u001b[0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 6:
                        user_login = true;
                        a = 'n';
                        break;
                    case 7:
                        system("pause");
                        return 0;
                    default:
                        cout << "\t\t\tEnter an integer between (1-7)\nTHANK YOU!" << endl;
                        break;
                    }
                } while (a == 'y' || a == 'Y');
            }
            break;

        case 2: /*User System*/
            userlogin(user, pass);
            system("cls");
            if (check)
            {
                usermenu();
                cout << "\t\t\tWelcome \u001b[1;31m" << users[imatch].name << "\u001b[1;0m!"
                     << "\n\t\t\tYou have \u001b[1;31mSuccessfully\u001b[1;0m logged in!\n\t\t\tPlease wait..." << endl;
                Sleep(2000);
                system("cls");
                // Actual-Program
                // for do while/
                char a;
                do
                {
                    int ch;
                    usermenu(ch);
                    switch (ch)
                    {
                    case 1:
                        system("cls");
                        withdraw();
                        cout << "\n\t\t\tPress Y to go to back to menu? \u001b[1;31m(y/n)\u001b[1;0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 2:
                        system("cls");
                        depositt();
                        cout << "\n\t\t\tPress Y to go to back to menu? \u001b[1;31m(y/n)\u001b[1;0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 3:
                        system("cls");
                        accountlistuser();
                        cout << "\n\t\t\tPress Y to go to back to menu? \u001b[1;31m(y/n)\u001b[1;0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 4:
                        system("cls");
                        transferbal();
                        cout << "\n\t\t\tPress Y to go to back to menu? \u001b[1;31m(y/n)\u001b[1;0m: ";
                        cin >> a;
                        system("cls");
                        break;
                    case 5:
                        check = false;
                        imatch = 0;
                        a = 'n';
                        break;
                    case 6:
                        system("pause");
                        return 0;
                    default:
                        cout << "Enter an integer between (1-5)\nTHANK YOU!" << endl;
                        break;
                    }
                } while (a == 'y' || a == 'Y');
            }
            break;

        default: /*Login Type*/
            cout << "\t\t\tEither \u001b[1;31mChoose\u001b[1;0m 1 or 2\n";
            break;
        }
    } while (user_login);
}
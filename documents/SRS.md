# <center>Human Resource Management</center>
***
## 1.Introduction
### 1.1 Purpose
The purpose of this document is to give a detailed description of the requirements for the “Human Resources Management". It will illustrate the purpose and complete declaration for the
development of system. It will also explain system constraints, interface and interactions with application.
### 1.2 Scope
"HUMAN RESOURCES MANAGEMENT" is a web application designed for managing departments and personnel.
***
## 2.Overall Description
### 2.1 Product perspective
This system will consist of two parts:databases and web applications. The database will act as a data warehouse. The web application will provide managers with all the necessary information on employee management(processing and managing information), such as:work schedule, Department names, data about all employees and vacations.

![](https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/databasenormal.png)

Pic. 2.1 DFD diagram.

### 2.2 Product functions
With this web application, users can manage the organization's employees and create reports on their work. The Manager will have access to such functions as: entering employee information, viewing employee information, editing and deleting data from the database. This app will also show the working hours of each employee and their activity using an interactive calendar.
### 2.3 User characteristics
There are two types of users who interact with the system:Manager and employee.The Manager has full access to the app and can view and manage information about all employees.Employees, in turn, when they log in to the app, will confirm the time when they arrived at work and choose what their mood is.
***
## 3.Specific requirements
### User interfaces
"HRM" - is a web application that automates the management of employees in an organization.
The application must provide:

- Displaying information about employee
- Editing employee information
- Updating information about employees
- Delete and add new employees to the database
- Display information about activity of the employee
- Creating work schedules
- Display of work/activity schedules using a calendar

### 3.1 Registration and Login
#### 3.1.1 Login form
This form is used to log in to your account.

***Main scenario:***

+ The user selects the login form.
+ Enters the appropriate data.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/reg1.png"  width="600" height="600">

Pic. 3.1.1 Login form.

If the data was entered incorrectly, the following window will appear:

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/loginError.png"  width="600" height="600">


Pic. 3.1.1.1 Login form Eror.

You can perform the following actions on the page:

+ The input of personal data.
+ Autofill data every time you log in.
+ Log in to your account.
+ Recover a forgotten password.

#### 3.1.2 Registration
This form is used to register a new account.

***Main scenario:***

+ The user registers.
+ The system checks the entered data.
+ If the specified email exists, the corresponding label is displayed.
+ Checks whether the user is a robot.
+ If the user has not passed verification, it is not registered.
+ Otherwise, registration is performed.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/reg2.png"  width="600" height="600">

Pic. 3.1.2 Sign up form.

If the passwords do not match, the user is given the following window:

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/registration.png"  width="600" height="600">

Pic. 3.1.2 Sign up form Error.


#### 3.1.3 Password recovery

This operation allows you to restore a lost or forgotten password.

***Main scenario:***

+ The user enters their email address.
+ The program checks whether such an email exists.
+ A confirmation email.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/forgetpas.png"  width="600" height="600">

Pic. 3.1.3 Password recovery.

After clicking the confirm button, an email will be sent to your email address with instructions on how to change your password.

#### 3.1.4 Confirm Passcode

In the course of this operation is the confirmation passcode.

***Main scenario:***

+ The user enters the passcode that was sent to their email address.
+ If it matches, the user is redirected to a new tab,where they enter a new password.
+ If it doesn't fit, the user is prompted to resend the email.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/confirmupdate.png"  width="600" height="600">

Pic. 3.1.4 Confirm Passcode.

Using the new message button, you can resend the message with a passcode.

#### 3.1.5 Confirm New Password

New password entry field.

***Main scenario:***

+ Entering a new password.
+ Re-confirming it.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/connewpass.png"  width="600" height="600">

Pic. 3.1.5 Confirm New Password.

### 3.2 Dashboard

The mode is designed to view information about the organization number of employees, departments, active employees and employees on vacation. The sidebar allows you to switch to other control tabs.

***Main scenario:***

- The user goes to the main page.
- The app displays information about the organization.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/calen.png"  width="600" height="600">

Pic. 3.2 Dashboard.

The page displays the following information:

- Number of employees.
- Number of departments.
- Number of employees online.
- Number of employees on vacation.
- Calendar with daily statistics.

### 3.3 Departments
#### 3.3.1 Department List

***Main scenario:***

- User selects item "Departments”;
- Application displays a list of departments.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/dpList.png"  width="600" height="600">

Pic. 3.3.1 Department List.

The list displays the following columns:

- Department - department name.
- Designation - designation of the department.
- Total employees - number of employees.
- Action - editing / deleting a table row.

Number of records displayed:

- In the department list view mode, the user sets the number of entries to display;
- The app will display the form with the required number of entries.

#### 3.3.2 New Department

***Main scenario:***

- User clicks the “+ New” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Save” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new department record is successfully added, then list of departments with added records is displaying.

***Cancel operation scenario:***

- User clicks the “+ New” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Cancel” button;
- Data don’t save in data base, then list of departments records is displaying to user.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/newdep.png"  width="600" height="600">

Pic. 3.3.2 New Department.

If such a department exists, the following window is displayed:

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/newDepartmentError2.png"  width="600" height="600">

Pic. 3.3.2.1 New Department Error.

When adding a department, the following details are entered:

- Department – department name;
- Designations – department designation;

#### 3.3.3 Edit Department

***Main scenario:***

- User clicks the “Edit” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Save” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new department record is successfully added, then list of departments with added records is displaying.

***Cancel operation scenario:***

- User clicks the “Edit” button in the department list view mode;
- Application displays form to enter department data;
- User enters department data and presses “Cancel” button;
- Data don’t save in data base, then list of departments records is displaying to user.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/newdep2.png"  width="600" height="600">

Pic. 3.3.3 Edit Department.

When editing a department, the following details are entered:

- Department – department name;
- Designations – department designation;

Constraints for data validation:

- Department – maximum length of 90 characters;
- Designations – maximum length of 90 characters;

#### 3.3.4 Removing the Departament

***Main scenario:***

- The user, while in the list of department, presses the "Delete" button in the selected department line;
- If the department can be removed, a confirmation dialog is displayed;
- The user confirms the removal of the department;
- Record is deleted from database;
- If error occurs, then error message displays;
- If department record is successfully deleted, then list of departments without deleted records is displaying.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/delDepar.png"  width="600" height="600">

Pic. 3.3.4 Removing the Departament.

When the manager accepts the deletion, a window pops up with a warning about what might happen:

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/departmentdelete.png"  width="600" height="600">

Pic. 3.3.4.1 A warning about removing.

Note:If you delete a department, all employees will also be deleted. In the table, delete the department and also all the data adjacent to it.

***Cancel operation scenario:***

- User is in display mode of department list and press “Delete” button;
- Application displays confirmation dialog “Please confirm delete department?”;
- User press “Cancel” button;
- List of departments without changes is displaying.

### 3.4 Employee
#### 3.4.1 Employee List

***Main scenario:***

- User selects item "Departments”;
- Application displays a list of departments.


<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/employeeList.png"  width="600" height="600">

Pic. 3.4.1 Employee List.


The list displays the following columns:

- ID - employee ID;
- Photo – employee photo;
- Name - employee name;
- Department - employee department;
- Position - employee position;
- Salary - employee salary;
- Email - employee email;
- Status - employee status;
- Actions - employee active.

Number of records displayed:

- In the Employee list view mode, the user sets the number of entries to display;
- The app will display the form with the required number of entries.

A date filter is also used,and employees can be filtered by year of birth.

#### 3.4.2 New Employee

***Main scenario:***

- User clicks the “+ New” button in the Employee list view mode;
- Application displays form to enter Employee data;
- User enters Employee data and presses “Save” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new Employee record is successfully added, then list of Employers with added records is displaying.

***Cancel operation scenario:***

- User clicks the “+ New” button in the Employee list view mode;
- Application displays form to enter Employee data;
- User enters Employee data and presses “Cancel” button;
- Data don’t save in data base, then list of Employers records is displaying to user.


<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/addemployee2.png"  width="600" height="600">

Pic. 3.4.2 New Employee.

If the user has entered user data while a user with such data in the required fields already exists.It displays the following error message.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/addemployeeError.png"  width="600" height="600">

Pic. 3.4.2.1 New Employee Error.

When you add an employee, you enter information about them.

#### 3.4.3 Edit Employee

***Main scenario:***

- User clicks the “Edit” button in the Employee list view mode;
- Application displays form to enter Employee data;
- User enters Employee data and presses “Save” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new Employee record is successfully added, then list of departments with added records is displaying.

***Cancel operation scenario:***

- User clicks the “Edit” button in the Employee list view mode;
- Application displays form to enter Employee data;
- User enters Employee data and presses “Cancel” button;
- Data don’t save in data base, then list of Employee records is displaying to user.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/addEmploy.png"  width="600" height="600">
Pic. 3.4.3 Edit Employee.


#### 3.4.4 Removing the Employee

***Main scenario:***

- The user, while in the list of employee, presses the "Delete" button in the selected employee line;
- If the employee can be removed, a confirmation dialog is displayed;
- The user confirms the removal of the employee;
- Record is deleted from database;
- If error occurs, then error message displays;
- If department record is successfully deleted, then list of employee without deleted records is displaying.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/employeeListDelete.png"  width="600" height="600">

Pic. 3.4.4 Removing the Employee.

Cancel operation scenario:

- User is in display mode of employee list and press “Delete” button;
- Application displays confirmation dialog “Please confirm delete employee ?”;
- User press “Cancel” button;
- List of employee without changes is displaying.

#### 3.4.5 Schedules List

***Main scenario:***

- User selects item "Schedules”;
- Application displays a list of Schedules.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/Sheduels.png"  width="600" height="600">

Pic. 3.4.5 Schedules List.


The list displays the following columns:

- ID - employee ID;
- Photo – employee photo;
- Name - employee name;
- Time in - start work time;
- Time out - end work time;
- Actions - editing / deleting a table row.

The table will be generated automatically from the employeelist table and from the user interface shown below.


### 3.5 User Mode

***Main scenario:***

- This form opens after the user is logged in to the system;
- If the system determines that this is a user and not a Manager, this tab opens;
- Otherwise, the page for managers opens;
- The user confirms their time;
- Chooses what his mood is.

<img src="https://github.com/EgorHubBrest/HRM/blob/subordinate/documents/pictures/usermi4ode.png"  width="600" height="600">

Pic. 3.6 User Mode

Note:When the user confirms their time, it is entered in the schedules database.




# Sprint 2 Report 
Video Link: 

Kanban Link: https://cpts451mealplanmanagement.atlassian.net/jira/software/projects/MPM/boards/1
## What's New (User Facing)
 * Students can select from the available meal plans on account creation
 * When creating an account, students can only use unique student IDs that are 8 digits exactly.
 * Admins can now login to their own page to manage the system
 * Admins can add items to menus and view the already created menus
 * Admins can add items to student purchase histories, which reduces the student balance and updates the usage report
 * Admins can view the usage report
 * Students can view all available menus and their items
 * Students can view their current balance
## Work Summary (Developer Facing)
We set up our Django system at https://rileyjnielsen.pythonanywhere.com, updated to the prerelease version 5.2b1 for the use of composite primary keys, and created all the models and the basic views for creating an account and logging in.
## Unfinished Work
We were unable to finish the entire Admin management system because it is larger than all the other requirments. Currently, admins can view everything they should, however, they can only add items to menus. Eventually, they will be able to edit and remove menu items, as well as edit and remove the active meal plans.
## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
 * [As a student, I want to select a meal plan so I can get access to funds to pay for meals.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-3)
 * [Bug where students can enter an already used student ID](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-16)
 * [Need to add restriction so student id in creation is of length 8 and is only numbers](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-17)
 * [Create an admin login page](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-15)
 * [Admin needs a way to add items to a student's purchase history](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-20)
 * [As a student, I want to be able to see each menu item and its nutritional info so I can plan what I want to eat.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-4)
 * [As a student, I want to be able to access a meal plan tracker so that I can check my remaining balance.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-6)
 * [As an administrator, I want to be able to track every item purchased so that I can manage usage reports.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-9)
 
## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:
 
 * [As an administrator, I want to be able to manage the menus, meal plans, and usage reports so that I can keep the meal plan service functioning properly.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-10)

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [dashboard.html](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/templates/administration/dashboard.html)
 * [nav.html](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/templates/nav.html)
 * [views.py](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/views.py)
 
## Retrospective Summary
Here's what went well:
 * Item 1: We worked collaboratively and helped each other whenever we got stuck.
 * Item 2: We learned more HTML so that we could actually interact with our project.
 * Item 3: We stay in constant communication so that we can get our work done on time and properly.
 
Here's what we'd like to improve:
 * Item 1: We want to improve the look of our website so that it is more user friendly.
  
Here are changes we plan to implement in the next sprint:
 * Item 1: We want everything to be working from both the student and admin standpoints.

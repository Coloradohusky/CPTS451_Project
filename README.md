# Sprint 2 Report 
Video Link: 

Kanban Link: https://cpts451mealplanmanagement.atlassian.net/jira/software/projects/MPM/boards/1?atlOrigin=eyJpIjoiNTlkM2VhN2VjMDA2NDE1Nzk3ODYwODE1ZjA2YTQ5MzAiLCJwIjoiaiJ9
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
We were unable to finish the implementation of a student picking a meal plan. Currently during account creation, they pick from pre-determined meal plans, but in the future we want them to pick from the meal plans in the meal plan table. We weren't able to get this done due to running out of time. We also have 2 unresolved bugs. First, students can attempt to create an account using an already in use student id, which causes the program to error out. Second, students can input anything as a student id, but it should only be an input of 8 digits. Both of these bugs are unresolved because we ran out of time, and they weren't high on out priority list.
## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
 * [Get SQL and DJANGO working](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-12)
 * [Create all tables in SQL](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-13)
 * [As a student, I want to register a student id and password so that I can log into the meal plan service.](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-2)
 * [Students should be able to log in](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-18)
 
## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:
 
 * [Meal plans selection dropdown is not linked to the actual list of meal plans](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-3)
 * [Should safely error when creating a duplicate student ID](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-16)
 * [Add restriction for student users only](https://cpts451mealplanmanagement.atlassian.net/browse/MPM-17)
## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [models.py](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/models.py)
 * [views.py](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/views.py)
 * [create.html](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/templates/registration/create.html)
 * [login.html](https://github.com/Coloradohusky/CPTS451_Project/blob/master/diningHall/templates/registration/login.html)
 
## Retrospective Summary
Here's what went well:
 * Item 1: We worked collaboratively and helped each other whenever we got stuck.
 * Item 2: We learned how to use DJANGO, which is the building block of our project.
 * Item 3: We also learned how to use a Kanban board, which has helped us stay organized.
 * Item 4: We stay in constant communication so that we can get our work done on time and properly.
 
Here's what we'd like to improve:
 * Item 1: We want to improve the look of our website so that it is more user friendly.
  
Here are changes we plan to implement in the next sprint:
 * Item 1: We want students to be able to pick from the actual list of meal plans, and not the pre-determined ones we have now
 * Item 2: We want to resolve our student account creation issues.

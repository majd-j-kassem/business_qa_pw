# Product Overview
This product is designed to support student or profissional to earn the skills needed for thie career path also in their study:
1. Register account and apply for coures
2. courses added by teachers 
3. teachers can create their profile and dashboard showing their courses and some statistical information
4. Teasher registeration remains in active , Admin can activate the teacher and admin should provide a commission which should be agreed outside the system

## Purpose
1. Support student , providing them with high quality courses 
2. support teacher to market their courses, and manage their portfolio

## Users and Roles
Admin: contrl and manage:
1. Account 
2. course categories
3. course level 
4. commission rate 
5. review and approve course before publish them
6. publish / un publish approved courses 
7. label courses as featured 
Student
1. can have their profile
2. can submit for courses on their own pace 
Teacher
1. Join the system
2. add their courses 
3. follow thier activity 

## Main Features
1. Student Registration and profiling 
2. student enrollement in courses
3. student self-pace continue their courses 
4. Teacher registeration , profiling and dashboard
5. Teacher selling their courses

## Important User Workflow

    Student Registration
    Homepage -> Login -> create new account

    Studendt enrollment:
    Courses page -> select course -> enrollment 

    Teacher Registration:
    Homepage -> Login -> create new account
    Teacher should contact Admin to make him as teacher and ask for approval after commission agreements 
    Teacher Adding courses
    Log in -> Dashboard -> add Course , Course is pending under review -> Admin accept and publish -> course is published 


## Dependencies
- pytest-django             4.11.1
- djangorestframework       3.16.0
- SQLite for local data storage.
- Local storage for uploaded files.

## Information Sources
- Source: Exploration of the application running locally.
- Application commit: 496dd4d
- Exploration date: 2026-11-12
## Open Questions

1. What criteria does the administrator use to approve or reject a course?
2. What happens after rejection? Can the teacher revise and resubmit the course?
3. Must a commission rate be agreed before approving a teacher or publishing a course?
4. How do students pay for courses, and when is enrollment confirmed?
5. How Admin and teacher make financial settelement and what the frequency of doing it, what the channel , and do admin sent invoices showing Revenu, Commetion, and due money 
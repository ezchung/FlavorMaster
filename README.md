# FlavorMaster

FlavorMaster is a platform for virtual cooking classes, similar to online workout programs. Users can browse and register for classes, and instructors can manage their offerings. The platform will also work with stores to facilitate purchasing the correct items for recipes.

## Features

- **Browse Classes:** Users can explore available cooking classes by category, date, or instructor.
- **Class Registration:** Users can register for classes and attend either live or recorded sessions.
- **Instructor Management:** Instructors can create and manage their classes, upload recipes, and provide instructions.
- **Purchase Items:** Users can purchase the items they need for the class through a dedicated store page.

## Tech Stack

- **Frontend:** React
- **Backend:** Django
- **Tools:** AWS

Objectives
- Users enter the site authorized. Users can create their own class. Classes can have multiple instructors. Users can register for classes. Users are able to see what classes they registered for. Users can be both instructors and attendes. Instructors can create and manage their classes, upload recipes, and provide instructions. Users can unregister for classes.

When instructors make a class, they need to input the syllabus pdf, etc.

## Models
Users
    - username
    - password
    - uuid
Join table
- Attende
- Instructor

Course
    -uuid
    -instructor or instructors
    -course details
    -syllabus pdf (will be stored in AWS S3)
    -time of class
    -recipe list
    -style of cooking
    -level of cooking
    -Class size limit

Registration
    who registered for what class
    uuid

Waitlist
    if there is a waitlist, if you were in the class and unregistered, you go to the back of line


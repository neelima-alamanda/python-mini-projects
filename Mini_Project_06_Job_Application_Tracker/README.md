# 💼 Job Application Tracker

## 📌 About

The Job Application Tracker is a console-based Python application developed using Object-Oriented Programming (OOP) and modular programming concepts. The application allows users to manage profiles, job listings, and job applications. It demonstrates JSON file handling, CRUD operations, custom exception handling, date and time handling, and recursive job recommendations based on partial skill matching.

---

## 🎯 Problem Statement

Develop a modular Python application that manages user profiles, job opportunities, and job applications. The application should:

- Create, view, update, and delete user profiles
- Create, view, update, and delete job listings
- Allow users to apply for available jobs
- Validate GPA and required skills before applying
- Handle validation errors using custom exceptions
- Recommend jobs using recursive partial skill matching
- Store application data using JSON files
- Organize functionality into separate Python modules

---

## ✨ Features

### 👤 User Profile Management

- ➕ Create user profiles
- 📋 View user profiles
- ✏️ Update user profiles
- 🗑️ Delete user profiles
- 💾 Store user information using JSON

### 💼 Job Management

- ➕ Add job listings
- 📋 View available jobs
- ✏️ Update job information
- 🗑️ Delete job listings
- 🔎 Store required skills and minimum GPA

### 📝 Application Processing

- 📌 Apply for available jobs
- ✅ Validate minimum GPA
- 🔍 Validate required skills
- ⚠️ Handle application eligibility errors
- 🕒 Store application date and time
- 📋 View submitted applications

### 🧩 Job Recommendation

- 🔎 Recommend suitable jobs for users
- 🧠 Perform partial skill matching
- 🔄 Use recursion to check available jobs

### ⚠️ Exception Handling

- Custom GPA validation exception
- Custom missing skills exception
- Input validation and error handling
- Handling duplicate and unavailable records

---

## 🛠 Technologies Used

- Python 3
- JSON
- Visual Studio Code
- Command Prompt / Terminal
- Object-Oriented Programming
- Modular Programming

---

## 📂 Project Structure

```text
Mini_Project_06_Job_Application_Tracker/
│
├── README.md
├── JOB_APPLICATION_TRACKER.pdf
├── main.py
├── profile.py
├── job.py
├── application.py
├── utils.py
├── exceptions.py
├── users.json
├── jobs.json
└── applications.json
```
## 📁 Project Files

### 📄 main.py

The main driver program that provides the menu-driven interface and connects the user profile, job management, application processing, and job recommendation modules.

### 📄 profile.py

Defines the `User` class and handles user profile operations such as creating, viewing, updating, and deleting user profiles.

### 📄 job.py

Defines the `Job` class and handles job operations such as adding, viewing, updating, and deleting jobs. It also implements recursive job recommendations based on partial skill matching.

### 📄 application.py

Defines the `Application` class and handles job applications, GPA validation, skill validation, and application date and time tracking.

### 📄 utils.py

Provides reusable functions for initializing, reading, and writing JSON files used by the application.

### 📄 exceptions.py

Defines custom exceptions such as `InsufficientGPAError` and `MissingSkillsError` for handling job eligibility validation.

### 📄 users.json

Stores user profile information including name, skills, and GPA.

### 📄 jobs.json

Stores available job information including job ID, title, required skills, and minimum GPA.

### 📄 applications.json

Stores submitted job applications along with application date and time.

### 📄 JOB_APPLICATION_TRACKER.pdf

Contains the complete project documentation including:

- Project Overview
- Problem Statement
- Features
- Technologies Used
- Python Concepts Used
- Program Workflow
- Output Screenshots and Explanation
- Learning Outcomes
- Conclusion

---

## 🎓 Learning Outcomes

After completing this project, I learned how to:

- Develop modular Python applications
- Apply Object-Oriented Programming concepts
- Perform CRUD operations using JSON files
- Create and handle custom exceptions
- Validate user eligibility using GPA and skills
- Work with date and time using Python
- Implement recursive functions
- Perform partial skill matching
- Build menu-driven console applications
- Organize code into reusable modules

---

## 🚀 Future Enhancements

- Add application status tracking
- Add job search and filtering
- Improve job recommendation logic
- Add more advanced skill matching
- Store application data using SQLite or a database
- Build a graphical user interface using Tkinter
- Develop a web-based version using Flask

---

## 👩‍💻 Connect

**GitHub:** https://github.com/neelima-alamanda

**LinkedIn:** https://www.linkedin.com/in/neelima-alamanda-64b1752a1

---

⭐ This project was developed as part of my **Python Backend Learning Journey** to strengthen my understanding of Object-Oriented Programming, modular programming, JSON file handling, exception handling, recursion, and practical application development.
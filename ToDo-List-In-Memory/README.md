# 📝 To-Do List CLI App

A simple, modular **Command-Line To-Do List** application built in **Python** with **Poetry**, managing all data **in-memory** (for now 👀).  
This app helps you create, edit, and organize projects and their tasks — all from your terminal.

> ⚡ **Next Phase:** Database integration is planned — to persist all projects and tasks between sessions!

---

## ✨ Features

### 🗂 Project Management
- Create new projects with name and description limits  
- Edit existing projects safely with validation  
- Delete projects (and automatically remove their related tasks)  
- View all projects with creation time ordering  

### ✅ Task Management
- Add new tasks under projects  
- Edit task description, deadline, and status  
- Change task status (`todo → doing → done`) with proper flow validation  
- Delete tasks by ID with success/error feedback  
- Display all tasks of a project with details  

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Poetry** for dependency & environment management
- **In-Memory storage** (Phase 1)
- **Database support (Coming Soon 🚀)** in the next phase  
- **Modular architecture** — clear separation of logic (models, managers, cli)

---

## 🧱 Project Structure

todo_cli_app/

├── todo_cli_app/

│ ├── init.py

│ ├── main.py # CLI entry point

│ ├── project_manager.py # Project creation/edit/delete logic

│ ├── task_manager.py # Task management logic

│ ├── models.py # Data models for Project and Task

├── pyproject.toml # Poetry configuration file

└── README.md

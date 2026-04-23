# Git & GitHub Assignment - Flask To-Do Project

## 👩‍💻 Project Overview
This project demonstrates Git and GitHub workflow using a Flask-based To-Do application.  
It includes frontend form development, backend API creation, MongoDB integration, and advanced Git operations like branching, merging, conflict resolution, reset, and rebase.

---

## 📁 Repository Structure
- main → Final integrated code
- master_1 → Frontend development (To-Do form)
- master_2 → Backend API development
- <username>_new → JSON API update branch

---

## 🚀 Features Implemented

### 1. Frontend (To-Do Form)
- Item Name
- Item Description
- Item ID
- Item UUID
- Item Hash

### 2. Backend (Flask API)
- POST route: `/submittodoitem`
- Accepts form data
- Stores data in MongoDB

### 3. JSON API Branch
- Updated API response structure

---

## 🔀 Git Operations Performed

- Created multiple branches:
  - master_1
  - master_2
  - username_new
- Performed sequential commits for form fields:
  - Item ID
  - Item UUID
  - Item Hash
- Merged branches into main
- Handled merge conflicts
- Used git reset --soft
- Performed git rebase while preserving commit history

---

## 🧪 Tech Stack
- Python (Flask)
- HTML (Frontend)
- MongoDB
- Git & GitHub

---

## 📌 How to Run Project

```bash
git clone git@github.com:bhavanagowda28/git-github-assignment.git
cd git-github-assignment
pip install flask pymongo
python app.py

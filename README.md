# Budget Tracker Application

## Overview
The **Budget Tracker Application** is a simple GUI-based application built using Python. It allows users to securely manage their budget, add transactions, and view their financial records. Each user has their own secure, individual file to store their budget data. The application includes features for user registration, login, and transaction management.

---

## Features
- **User Authentication**:
  - Secure registration and login system.
  - Stores credentials in a `users.txt` file.
- **Personalized Budget Tracking**:
  - Each user has a separate CSV file to store their transaction data.
  - View, add, and manage budget transactions.
- **User-Friendly Interface**:
  - Clean, intuitive interface built with `Tkinter`.
  - Designed with a professional banking theme (beige background).
- **Data Security**:
  - Budget data is stored locally in a directory named `user_data`.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pandas`: For managing and storing transaction data.
  - `tkinter`: For building the graphical user interface.
  - `os`: For file and directory management.

---

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/budget-tracker.git
   cd budget-tracker
   ```

2. **Install Dependencies**:
   - Ensure Python (version 3.7 or later) is installed.
   - Install the `pandas` library if not already installed:
     ```bash
     pip install pandas
     ```

3. **Run the Application**:
   - Execute the script:
     ```bash
     python budget_app.py
     ```

---

## File Structure
```
budget-tracker/
│
├── budget_app.py          # Main application file
├── users.txt              # Stores user credentials (created after registration)
├── user_data/             # Directory to store individual user budget files
└── README.md              # Documentation for the repository
```

---

## Usage
1. **Register**: 
   - Enter a unique username and password.
   - Click "Register" to create an account.
2. **Login**:
   - Enter your registered credentials.
   - Click "Login" to access your account.
3. **Add Transactions**:
   - Enter the date, description, category, and amount of the transaction.
   - Click "Add Transaction" to save the record.
4. **View Transactions**:
   - Click "View Transactions" to see all recorded transactions in a table.

---

## SCREENSHOTS
![image alt](https://github.com/Garvitsharma-gs/Budget-Tracker-Application/blob/4dcd1faf1a56ca974e8f3c5dc4a6bce3c4a1b4f3/Budget%20App%2024-11-2024%2004_23_02.png)
![image alt](https://github.com/Garvitsharma-gs/Budget-Tracker-Application/blob/4dcd1faf1a56ca974e8f3c5dc4a6bce3c4a1b4f3/Budget%20App%2024-11-2024%2004_23_15.png)

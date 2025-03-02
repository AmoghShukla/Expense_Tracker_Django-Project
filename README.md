# Expense Tracker - Django Project

## Overview
Expense Tracker is a Django-based web application that allows users to manage their expenses efficiently. Users can input their monthly salary, add and categorize expenses, and view real-time insights, including the remaining balance and detailed analysis with graphs.

## Features
- **User Authentication**: Secure login and registration system.
- **Add Expenses**: Users can add and categorize their expenses.
- **Real-time Balance Calculation**: Displays money left after expenses.
- **Detailed Analysis**: Interactive graphs and insights on spending patterns.
- **Responsive UI**: Clean and user-friendly design.

## Technologies Used
- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (can be switched to PostgreSQL/MySQL)
- **Visualization**: Matplotlib, Chart.js

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AmoghShukla/Expense_Tracker_Django-Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Expense_Tracker_Django-Project
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- **Sign up/Login** to start tracking expenses.
- **Enter your monthly salary** in the dashboard.
- **Add expenses** with appropriate categories.
- **View real-time updates** on remaining money.
- **Click on 'Detailed Analysis'** to get insights and graphs.

## Screenshots
![image](https://github.com/user-attachments/assets/9e918a48-294f-4b06-9c2e-6e05ad3d5b0d)


## Contributing
Feel free to fork this repository and submit pull requests for new features or improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).

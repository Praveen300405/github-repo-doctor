🚑 GitHub Repo Doctor

A Streamlit-based web application that analyzes a public GitHub repository and checks its development quality.

✨ Features

🔗 Accepts a public GitHub repository URL

📊 Shows repository statistics:

⭐ Stars

🍴 Forks

🐛 Open Issues

👀 Watchers

❤️ Calculates a Repository Health Score out of 100

🟢 Provides a repository health status

🔎 Checks important project quality indicators:

README.md

.gitignore

requirements.txt

Automated tests

Git commits

💡 Gives recommendations for improving repository quality

🧪 Includes automated tests using Pytest

🎨 Modern dark-themed Streamlit interface

🛠️ Technologies Used

Python

Streamlit

GitHub API

Requests

Pytest

Git

GitHub

📁 Project Structure

github-repo-doctor/
│
├── app.py
├── github_api.py
├── analyzer.py
├── scoring.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    ├── test_analyzer.py
    └── test_scoring.py

⚙️ How It Works

Enter a public GitHub repository URL.

The application retrieves repository information using the GitHub API.

It checks the repository files and commit history.

The analyzer identifies the available quality indicators.

The scoring system calculates a score out of 100.

The application displays the repository health and recommendations.

📊 Scoring System

Quality Check

Points

README.md

20

.gitignore

15

requirements.txt

15

Tests

20

Git Commits

30

Total

100

Health Status

Score

Status

80–100

🟢 Excellent

60–79

🟡 Good

40–59

🟠 Needs Improvement

0–39

🔴 Poor

🚀 Installation

Clone the repository:

git clone https://github.com/Praveen300405/github-repo-doctor.git
cd github-repo-doctor

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\Activate.ps1

Install the required packages:

pip install streamlit requests pytest

▶️ Run the Application

streamlit run app.py

The application will open in your browser.

🧪 Run Tests

Run the automated tests with:

python -m pytest

Expected result:

3 passed

💡 Recommendations

The application recommends improvements when important repository practices are missing, such as:

Add a README.md file.

Add a .gitignore file.

Add a requirements.txt file.

Add automated tests.

🎯 Project Goal

The goal of GitHub Repo Doctor is to provide a simple way to evaluate the basic development quality and health of a public GitHub repository.

👨‍💻 Author

Praveen

GitHub: https://github.com/Praveen300405

📄 License

This project is created for learning and portfolio purposes.
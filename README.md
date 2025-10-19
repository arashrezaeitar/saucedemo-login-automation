# 🧪 SauceDemo Login Automation (Selenium + Pytest)

This project automates the **Login functionality** of the SauceDemo website using **Selenium WebDriver** and **Pytest** framework.

---

## 📁 Project Structure

saucedemo-login-automation/
│
├── pages/ # Page Object files (e.g., login_page.py)
├── tests/ # Test cases (e.g., test_login.py)
├── utils/ # Helpers & configuration files
├── reports/ # HTML test reports
├── screenshots/ # Test screenshots (PASS/FAIL)
├── requirements.txt # Dependencies list
└── README.md # This file


---

## ⚙️ Setup Instructions

1. **Install dependencies:**
   ```bash
   py -m pip install -r requirements.txt


(Optional) Install HTML reporting plugin:

py -m pip install pytest-html pytest-metadata


Run all tests:

py -m pytest -v


Generate HTML report:

py -m pytest --html=reports/login-report.html --self-contained-html

🧠 Test Scenarios
Test ID	Scenario	Expected Result
TC-AUTO-01	Valid Login with correct credentials	User is redirected to inventory page
TC-AUTO-02	Invalid Login with wrong password	Error message “Epic sadface…” displayed
📸 Test Artifacts

Screenshots: stored in /screenshots/

HTML Report: generated in /reports/login-report.html

🧰 Tech Stack

Python 3.13+

Selenium WebDriver

Pytest

ChromeDriver

Pytest-HTML

👨‍💻 Author

Arash Rezaei
Software Tester 
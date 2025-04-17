# 🛍️ BDD Shopping - Selenium Automation Project

This project is a real-time **BDD (Behavior-Driven Development)** framework using **Python**, **Behave**, **Selenium WebDriver**, and **WebDriver Manager** to automate test scenarios for [automationexercise.com](https://www.automationexercise.com).

## 📁 Project Structure
BDD Shopping/
│
├── features/
│   ├── steps/                  ← Step definitions (glue code)
│   │   └── test_homepage_steps.py
│   ├── pages/                  ← Page Object Model (POM)
│   │   └── homepage.py
│   ├── testdata/               ← (Optional) JSON, Excel, YAML test data
│   ├── homepage.feature        ← Feature files written in Gherkin
│   └── environment.py          ← Setup and teardown hooks
│
├── drivers/                    ← Optional (WebDriver binaries if needed)
├── reports/                    ← Store HTML or screenshot reports
├── screenshots/                ← Captured screenshots on failure
├── requirements.txt            ← Dependencies
├── .gitignore                  ← To ignore `__pycache__`, `.env`, etc.
└── README.md                   ← Project overview and setup instructions



## 🧪 Tools & Technologies

- Python 3
- Behave (BDD)
- Selenium WebDriver
- WebDriver Manager
- Gherkin syntax

## 🚀 Getting Started

1. **Clone the repo**  
   `git clone https://github.com/YOUR_USERNAME/bdd-shopping.git`

2. **Navigate to the project**  
   `cd bdd-shopping`

3. **(Optional) Create a virtual environment**  
   `python -m venv venv && venv\Scripts\activate`

4. **Install dependencies**  
   `pip install -r requirements.txt`

5. **Run the tests**  
   `behave`

## ✅ Sample Test Case

```gherkin
Feature: Homepage

  Scenario: Verify the homepage title
    Given I launch the browser and open the website
    Then the title should be "Automation Exercise"



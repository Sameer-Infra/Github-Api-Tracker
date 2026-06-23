# 🚀 GitHub API Tracker

A sleek and efficient DevOps scripting tool written in Python to fetch and parse live user data directly from the GitHub REST API.

---

## 🛠️ Features
- **Live Data Fetching:** Uses the Python `requests` module to communicate with GitHub's public API.
- **JSON Parsing:** Automatically converts API responses into clean, readable Python dictionaries.
- **Smart Data Extraction:** Safely extracts specific fields like Name, Public Repos, and Bio.
- **Status Code Validation:** Checks for `200 OK` responses before processing data to ensure uptime verification.

---

## 📦 Prerequisites
Make sure you have Python installed on your system. You will also need the `requests` library. If you don't have it, install it using:

```bash
pip install requests

🚀 How to Run
Clone this repository or download the github_tracker.py file.

Run the script using your terminal:

Bash
python3 github_tracker.py

📸 Sample Output
When you run the script, it hits the API and prints data like this:

Plaintext
Github s Sameer-Infra ka data nikal rha hu...

--- 😎 Github profile Details ---
Name: Sameer
Public Repositories: 7
Bio: Devops & Agentic Ai Learner 🤖

# 🚀 Selenium Automation Practice Repository

Welcome to the **Selenium Automation Open-Source Practice Repository** 🎉  
This project is designed for learners who want to practice **Selenium with Python** using real websites.  
It is linked with my tutorials on [My Blog](https://aigen023.blogspot.com/), where you can learn concepts step by step and run them here.

---

# 📌 Why This Repo?
- ✅ Hands-on Selenium practice with **real websites**
- 📈 Beginner → Advanced structured examples
- 🤝 Open for contributions (add new test cases, improve docs, fix bugs)
- 🔗 Directly connected to my **learning course/blog**

---

# 📂 Repository Structure

```
Selenium-Automation-Practice/
│── README.md                # Documentation (you are here)
│── requirements.txt         # Dependencies
│── .gitignore               # Ignore unnecessary files
│── CONTRIBUTING.md          # Guidelines for contributors
│
├── basics/                  # Beginner level tests
│   ├── test_open_browser.py
│   ├── test_navigation.py
│   ├── test_locators.py
│
├── intermediate/            # Intermediate level tests
│   ├── test_forms.py
│   ├── test_login.py
│   ├── test_dropdowns.py
│
├── advanced/                # Advanced level tests
│   ├── test_waits.py
│   ├── test_iframes.py
│   ├── test_file_upload.py
│
└── resources/               # Extra resources
    ├── testing_sites.md
    └── sample_data.json
```

---

# ⚙️ Getting Started

### 0️⃣ Fork This Repository

Click the **Fork** button at the top right of this page to create your own copy of the repository on GitHub.  
This lets you make changes and contribute without affecting the original project.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Selenium-Automation-Practice.git
cd Selenium-Automation-Practice
```

### 2️⃣ Install Dependencies

Make sure you have Python 3.8+ installed. Then run:

```bash
pip install -r requirements.txt
```

**Dependencies included:**
- 🐍 selenium → Browser automation
- 🧪 pytest → Testing framework
- 📊 pytest-html → Generate test reports

### 3️⃣ Run Your First Test

```bash
pytest basics/test_open_browser.py --html=report.html
```

📄 After running, open `report.html` in your browser to see results ✅

---

# 🌐 Testing Sites Used

We use multiple public websites for practice:

- 🔗 Herokuapp → Elements, Alerts, Login tests
- 🔗 OrangeHRM Demo → Login/HRM workflows
- 🔗 FormSite Demo → Forms & input fields
- 🔗 SauceDemo → E-commerce flows
- 🔗 jQueryUI → Drag & drop, sliders
- 🔗 Google → Search automation
- 🔗 Playwright → Compare Selenium vs Playwright
- 🔗 My Blog → Course reference

---

# 📝 Example Test Case

`basics/test_open_browser.py`:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium automation python")
    time.sleep(2)
    driver.quit()
```

---

# 📖 Learning Path (Linked with Blog)

- 📕 Basics: Browser & Locators → `basics/` folder
- 📗 Intermediate: Forms & Login → `intermediate/` folder
- 📘 Advanced: Waits, iFrames, Uploads → `advanced/` folder

---

# 🤝 Contributing

We ❤️ contributions!

1. 🍴 Fork this repo
2. 🌱 Create a new branch (`feature-new-test`)
3. 📝 Add your test script in the correct folder
4. ✅ Run and verify with pytest
5. 💾 Commit & push:

    ```bash
    git add .
    git commit -m "Added new test case for dropdown"
    git push origin feature-new-test
    ```

6. 🔀 Open a Pull Request 🎉

👉 See `CONTRIBUTING.md` for full details.

---

# 📊 Reporting

Generate an HTML report for test results:

```bash
pytest --html=report.html
```

Open `report.html` in a browser.

---

# 📜 License

📄 This project is open source under the MIT License.  
You are free to use, modify, and distribute with attribution.

---

# 🙌 Credits

👨‍💻 Maintainer: Shivam Dubey  
📚 Course & Tutorials: My Blog

⭐ If you like this project, please star the repo! ⭐

---

  

# 🚀 Selenium Automation Practice Repository

**Learn Selenium with Python using real-world websites!**  
Practice, contribute, and master browser automation with hands-on examples.  
Linked with [Next-Gen AI Blog](https://aigen023.blogspot.com/) and [Automation_Selenium_Python](https://github.com/kuro-shiv/Automation_Selenium_Python).

---

## ⭐ Why Star This Repo?

- **Real Selenium Projects:** Practice automation on actual websites.
- **Beginner to Advanced:** Structured examples for all skill levels.
- **Open Source & Community Driven:** Contribute, suggest, and collaborate.
- **Linked Tutorials:** Step-by-step guides on [My Blog](https://aigen023.blogspot.com/).
- **SEO Keywords:** Selenium, Python, Automation, Testing, Open Source, Practice, Tutorial.

---

## 📂 Repository Structure

```
Selenium-Automation-Practice/
│── README.md                # Documentation
│── requirements.txt         # Dependencies
│── .gitignore               # Ignore unnecessary files
│── CONTRIBUTING.md          # How to contribute
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

## ⚡ Getting Started

### 1️⃣ Fork & Clone

Click **Fork** (top right) to create your copy.  
Then clone:

```bash
git clone https://github.com/YOUR_USERNAME/Selenium-Automation-Practice.git
cd Selenium-Automation-Practice
```

### 2️⃣ Install Dependencies

Python 3.8+ required.

```bash
pip install -r requirements.txt
```

**Main Packages:**
- `selenium` – Browser automation
- `pytest` – Testing framework
- `pytest-html` – HTML test reports

### 3️⃣ Run Your First Test

```bash
pytest basics/test_open_browser.py --html=report.html
```

Open `report.html` in your browser to view results.

---

## 🌐 Practice Websites

- [Herokuapp](https://the-internet.herokuapp.com/) – Elements, Alerts, Login
- [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) – HRM workflows
- [FormSite Demo](https://www.formsite.com/) – Forms & inputs
- [SauceDemo](https://www.saucedemo.com/) – E-commerce flows
- [jQueryUI](https://jqueryui.com/droppable/) – Drag & drop, sliders
- [Google](https://www.google.co.in/) – Search automation
- [Playwright](https://playwright.dev/) – Compare Selenium vs Playwright
- [My Blog](https://aigen023.blogspot.com/) – Tutorials & exercises

---

## 📝 Example Test Case

```python
# basics/test_open_browser.py
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

## 📖 Learning Path

- **Basics:** Browser, Locators → `basics/`
- **Intermediate:** Forms, Login → `intermediate/`
- **Advanced:** Waits, iFrames, Uploads → `advanced/`
- **Tutorials:** [Next-Gen AI Blog](https://aigen023.blogspot.com/)

---

## 🤝 How to Contribute

We ❤️ contributions!

1. **Fork** the repo
2. **Create a branch:** `feature-your-feature`
3. **Add your test** in the right folder
4. **Run & verify** with pytest
5. **Commit & push:**
    ```bash
    git add .
    git commit -m "Added new test case for dropdown"
    git push origin feature-your-feature
    ```
6. **Open a Pull Request**  
   See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📊 Test Reporting

Generate an HTML report:

```bash
pytest --html=report.html
```

Open `report.html` in your browser.

---

## 📜 License

MIT License – Free to use, modify, and distribute with attribution.

---

## 🙌 Credits

- **Maintainer:** [Shivam Kumar Dubey](https://github.com/kuro-shiv)
- **Blog & Tutorials:** [Next-Gen AI](https://aigen023.blogspot.com/)
- **Related Repo:** [Automation_Selenium_Python](https://github.com/kuro-shiv/Automation_Selenium_Python)

---

## ⭐ Star & Share!

If you find this project helpful, **star the repo** and share with others!  
Help us grow the Selenium automation community 🚀

---

## 🔎 Recommended GitHub Topics

```
selenium
python
automation
testing
pytest
open-source
practice
tutorial
webdriver
qa
```

---

**Boost your skills. Contribute. Star. Share.**  
Happy Testing!


# 🤝 Contributing to Selenium Automation Practice

Thank you 🙏 for considering contributing to this project!  
We welcome all contributions — whether it’s **adding test cases, fixing bugs, improving documentation, or suggesting ideas**.

---

## 🛠 How to Contribute

### 1️⃣ Fork the Repository
- Go to the repo page: https://github.com/YOUR_USERNAME/Selenium-Automation-Practice
- Click **Fork** (top right corner) to create your own copy

### 2️⃣ Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Selenium-Automation-Practice.git
cd Selenium-Automation-Practice
```

### 3️⃣ Create a New Branch
Always create a feature branch instead of working on main:
```bash
git checkout -b feature-my-test
```

### 4️⃣ Add Your Contribution
- Add your test in the correct folder:
  - `basics/` → Beginner-level tests
  - `intermediate/` → Medium-level tests
  - `advanced/` → Advanced-level tests
- Follow PEP8 coding style (clean, readable code)
- Use meaningful test names (e.g., `test_login_valid_user.py`)

### 5️⃣ Run Tests Locally
Before pushing, make sure everything works:
```bash
pytest --html=report.html
```
✅ Check `report.html` for results.

### 6️⃣ Commit Your Changes
```bash
git add .
git commit -m "Added new test case for login form"
```

### 7️⃣ Push to Your Fork
```bash
git push origin feature-my-test
```

### 8️⃣ Open a Pull Request
- Go to your fork on GitHub
- Click **New Pull Request**
- Write a clear description of your changes

---

## 🧑‍💻 Contribution Ideas

- Add new Selenium test cases for listed testing sites
- Improve existing test scripts (better locators, waits, exception handling)
- Add more resources in `resources/` folder
- Improve documentation (README, setup guides, examples)
- Create new blog-linked exercises

---

## 📝 Code Style Guidelines

- ✅ Follow PEP8 (Python standard style guide)
- ✅ Use pytest style tests (functions prefixed with `test_`)
- ✅ Keep code modular and reusable
- ✅ Add comments if logic is complex

**Example:**
```python
def test_valid_login():
    """Test valid login on OrangeHRM demo site"""
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Add test steps here
    driver.quit()
```

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License of this project.

---

## 🙌 Thank You!

Every contribution counts ❤️  
Together we are making Selenium learning easier for everyone 🚀
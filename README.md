# 🍊 OrangeHRM End-to-End Automation Framework

A scalable **Selenium WebDriver** automation framework for the [OrangeHRM demo](https://opensource-demo.orangehrmlive.com/) application, built with **Python**, **PyTest**, and the **Page Object Model (POM)** design pattern.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.x-green.svg)](https://www.selenium.dev/)
[![PyTest](https://img.shields.io/badge/pytest-8.x-orange.svg)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## ✨ Features

- ✅ Clean **Page Object Model (POM)** architecture
- ✅ Reusable **Base Page** methods (click, type, wait, get text, etc.)
- ✅ **Explicit waits** for stable, reliable execution
- ✅ **Automatic WebDriver management** via `webdriver-manager`
- ✅ **Centralized configuration** using YAML + JSON
- ✅ **Automatic logging** to file & console
- ✅ HTML reporting with `pytest-html`
- ✅ **Screenshot capture** on failed tests (auto-attached to reports)
- ✅ **Cross-browser support** — Chrome, Firefox, Edge
- ✅ **Parallel execution** with `pytest-xdist`
- ✅ **CI/CD ready** with GitHub Actions
- ✅ Modular and extensible framework architecture

---

## 🧱 Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| Browser Automation | Selenium WebDriver 4.x |
| Test Runner | PyTest |
| Design Pattern | Page Object Model (POM) |
| Config Management | YAML + JSON |
| Driver Management | webdriver-manager |
| Reporting | pytest-html |
| Parallel Execution | pytest-xdist |
| CI/CD | GitHub Actions |

---

## 📁 Project Structure

```text
OrangeHRM-Automation/
├── config/
│   ├── config.yaml
│   └── test_data.json
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│   ├── pim_page.py
│   ├── leave_page.py
│   ├── recruitment_page.py
│   ├── time_page.py
│   └── my_info_page.py
├── tests/
│   ├── test_login.py
│   ├── test_admin.py
│   ├── test_pim.py
│   ├── test_leave.py
│   ├── test_recruitment.py
│   ├── test_time.py
│   └── test_my_info.py
├── utils/
│   ├── driver_factory.py
│   ├── config_reader.py
│   └── logger.py
├── reports/
├── screenshots/
├── logs/
├── .github/workflows/ci.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🧪 Modules Covered

| Module | Test File | Description |
|---|---|---|
| Login | `test_login.py` | Valid/invalid login, logout |
| Admin | `test_admin.py` | User management, user search |
| PIM | `test_pim.py` | Add, search, and delete employees |
| Leave | `test_leave.py` | Apply and view leave requests |
| Recruitment | `test_recruitment.py` | Add and manage candidates |
| Time | `test_time.py` | Timesheets and attendance |
| My Info | `test_my_info.py` | Personal information updates |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Chrome, Firefox, or Edge
- Git

### Clone the Repository

```bash
git clone https://github.com/ruturaj-m1/OrangeHRM-Automation.git
cd OrangeHRM-Automation
```

### Create a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Tests

Run the complete suite:

```bash
pytest
```

Run on a specific browser:

```bash
pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge
```

Run tests in parallel:

```bash
pytest -n 4
```

Run specific tests:

```bash
pytest tests/test_login.py -v
pytest -m smoke
pytest -m "login or admin"
```

### View Reports

Open `reports/report.html` after execution to review the test report and any captured failure screenshots.

---

## ⚙️ Configuration

Update `config/config.yaml` to configure the execution environment.

```yaml
base_url: "https://opensource-demo.orangehrmlive.com/"
browser: "chrome"
headless: false
implicit_wait: 10
explicit_wait: 20
```

Store test data in `config/test_data.json`.

---

## 🖼️ Screenshot Capture

Failed test cases automatically generate timestamped screenshots in the `screenshots/` directory and attach them to the HTML report.

---

## 📝 Logging

Framework actions such as navigation, clicks, waits, and element interactions are logged with timestamps to both the console and `logs/automation.log`.

---

## 🤖 CI/CD

GitHub Actions executes the test suite on every push and pull request using headless Chrome. Generated artifacts include:

- HTML reports
- Failure screenshots
- Execution logs

Workflow configuration is available in:

```
.github/workflows/ci.yml
```

---

## ➕ Extending the Framework

To add support for a new module:

1. Create a new Page Object under `pages/`.
2. Implement locators and page actions.
3. Create corresponding test cases under `tests/`.
4. Register additional markers in `pytest.ini` if required.

The framework is designed to support new modules without modifying the core architecture.

---

## 🧭 Framework Highlights

- Explicit waits reduce test instability.
- Parallel execution improves overall test runtime.
- Automatic driver management eliminates manual setup.
- Modular architecture simplifies maintenance and scalability.
- Built-in reporting, logging, screenshots, and CI/CD support.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Ruturaj Mohapatra** • QA Automation Engineer • Python • Selenium
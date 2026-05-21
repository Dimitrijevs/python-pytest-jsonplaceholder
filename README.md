# pytest_automation

Automated API testing system for [JSONPlaceholder](https://jsonplaceholder.typicode.com) built with Python and pytest.

---

## Tech Stack

- **Python 3.13**
- **pytest** — test framework
- **requests** — HTTP client
- **pydantic** — data models and schema validation
- **faker** — test data generation
- **pytest-html** — HTML reports
- **allure-pytest** — Allure reports
- **pytest-retry** — automatic test retries
- **python-dotenv** — environment configuration

---

## Project Structure

```
pytest_automation/
│
├── api/
│   ├── base_client.py        # Base HTTP client with retries, timeout, logging
│   ├── posts_api.py          # Posts endpoints
│   ├── users_api.py          # Users endpoints
│   └── albums_api.py         # Albums endpoints
│
├── models/
│   ├── base_api_model.py     # Base model with shared assertions
│   ├── post.py               # Post DTO + assertions
│   ├── user.py               # User DTO + assertions
│   ├── album.py              # Album DTO + assertions
│   ├── album_photo.py        # AlbumPhoto DTO + assertions
│   ├── post_comment.py       # PostComment DTO + assertions
│   ├── todo.py               # Todo DTO + assertions
│   ├── address.py            # Address nested model
│   ├── company.py            # Company nested model
│   └── geo.py                # Geo nested model
│
├── tests/
│   ├── base_test.py          # Base test class with shared logger
│   ├── test_posts.py         # Posts tests
│   ├── test_users.py         # Users tests
│   └── test_albums.py        # Albums tests
│
├── utils/
│   ├── constants.py          # Test IDs and constants
│   ├── post_data_generator.py
│   ├── user_data_generator.py
│   └── album_data_generator.py
│
├── reports/                  # Generated reports (gitignored)
├── conftest.py               # Global fixtures
├── pytest.ini                # pytest configuration
├── .env                      # Environment variables
├── requirements.txt          # Dependencies
└── README.md
```

---

## Architecture

The system follows a three-layer architecture:

| Layer | Responsibility | Location |
|---|---|---|
| **API Layer** | HTTP requests, endpoints | `api/` |
| **Assertions** | Data validation, schema checks | `models/` |
| **Test Logic** | Test scenarios, expected behavior | `tests/` |

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd pytest_automation
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Allure CLI (for Allure reports)

```bash
brew install allure
```

### 5. Configure environment

Create a `.env` file in the root directory:

```
BASE_URL=https://jsonplaceholder.typicode.com
```

---

## Running Tests

### Run all tests
```bash
pytest
```

### Run by scope
```bash
pytest -m smoke       # fast critical tests
pytest -m full        # complete test suite
pytest -m negative    # negative scenarios
```

### Run by resource
```bash
pytest -m post        # posts tests only
pytest -m user        # users tests only
pytest -m album       # albums tests only
```

---

## Reports

### HTML Report

Generated automatically after every test run at:
```
reports/report.html
```

Open in browser:
```bash
open reports/report.html
```

### Allure Report

Generate results and open report:
```bash
pytest                              # run tests first
allure serve reports/allure-results # open interactive report
```



https://github.com/user-attachments/assets/9000b3e0-5b41-4af5-ae3e-bc3e1d9154c4


**Project Title**

Pet store API testing (Swagger UI)

**Description**

This project demonstrates API testing techniques using both manual and automated approaches. It covers four core functionalities:

* **POST:** Create a new resource (e.g., pet)
* **PUT:** Update existing resource information (e.g., pet details)
* **GET:** Retrieve resource details (e.g., pet information)
* **DELETE:** Remove a resource (e.g., delete a pet)

**Manual Testing**

* **Tool:** Postman
* **Documentation:**
    * `Manual API Testing.pdf`: Provides a detailed walkthrough of the manual testing process for all four functionalities.
    * `Defect Report.pdf`: Documents any defects encountered during manual testing.

**Test Cases:**

For each functionality, the project includes one positive and one negative test case:

* **Positive Test Cases:** Verify successful API interaction under expected conditions.
* **Negative Test Cases:** Identify and report unexpected API behavior.

**Automated Testing**

* **Framework:** Python `requests` library for sending HTTP requests
* **Test Runner:** Pytest

**Project Structure**

```
.
├── Manual_Testing/
│   ├── Manual_API_Testing.pdf
│   └── Defect_Report.pdf
├── automated_tests/
│   ├── test_web_server_api_endpoints.py  # Tests for web server API endpoints
│   └── UTILS/
│       ├── __init__.py  # (Optional: Empty file to treat the directory as a package)
│       ├── utils.py      # Utility functions for testing
│       └── payload.py    # payload generation
├── requirements.txt  # Lists Python dependencies (requests, pytest)
└── README.md        # This file (you are here)
```

**Running Tests**

1. Install project dependencies: `pip install -r requirements.txt`
2. Navigate to the project directory in your terminal.
3. Run automated tests: `pytest`

**Further Development**

* Expand test coverage to include more functionalities and edge cases.
* Enhance automation with data-driven testing and parameterization.
* Integrate continuous integration (CI) to automate testing on code changes.


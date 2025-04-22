
# 📝 auto-tests-gherkin-python

This repository features a simple to-do list implementation in Python, along with automated tests written in Gherkin syntax. The project showcases behavior-driven development (BDD) practices using Python and Gherkin.

## 📂 Project Structure

```
├── to_do_list.py          # Core logic of the to-do list
├── features/
│   ├── to_do_list.feature # Gherkin scenarios
│   └── steps/
│       └── steps.py       # Step definitions for the scenarios
├── requirements.txt       # Project dependencies
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RemmReyy/auto-tests-gherkin-python.git
   cd auto-tests-gherkin-python
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running Tests

To run the tests, simply execute:

```bash
behave
```

This will run all scenarios defined in the `.feature` files using the step implementations.

## 📌 Dependencies

- Python 3.7+
- behave

All necessary packages are listed in the `requirements.txt` file.

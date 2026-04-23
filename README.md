# Inventory Management System - TDD Practice

## Overview

This project is a simplified inventory management system developed in Python using the Test-Driven Development (TDD) methodology.

The purpose of this repository is to demonstrate how software functionality can be built incrementally through automated testing, following the Red-Green-Refactor cycle.

This project was created as part of a software analysis and development workshop focused on TDD practices.

---

## Project Goals

The system allows users to:

- Register products in inventory
- Update product quantity
- Retrieve product information
- List all registered products

The project intentionally avoids database integration and graphical interfaces to focus on testing and software design.

---

## Technologies Used

- Python 3
- Pytest
- Git
- VS Code / IDE

---

## Project Structure

```text
inventory_tdd/
│
├── src/
│   ├── inventory.py
│   └── product.py
│
├── tests/
│   ├── test_inventory.py
│   └── test_product.py
│
├── requirements.txt
└── README.md
```

---

## TDD Workflow

This project follows the TDD cycle:

1. **Red** → Write a failing test
2. **Green** → Write minimal code to pass the test
3. **Refactor** → Improve code structure while keeping tests passing

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd inventory_tdd
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

To execute automated tests:

```bash
pytest
```

---

## Features

- Add products to inventory
- Update stock quantity
- Search products
- Display inventory list
- Automated unit testing

---

## Educational Purpose

This repository is intended for learning and practicing:

- Test-Driven Development (TDD)
- Python unit testing
- Incremental software design
- Code refactoring
- Repository organization

---

## License

This project is for educational purposes.
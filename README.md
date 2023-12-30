# Adamfroggy's Student BloomData Tests

This repository contains test functions for a set of classes and functions implemented in the `student.py` file. The primary purpose is to ensure the proper functionality of the code related to student information.

## Table of Contents

- [Introduction](#introduction)
- [Test Functions](#test-functions)
- [How to Run Tests](#how-to-run-tests)
- [License](#license)
- [Citation](#citation)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [References](#references)

## Introduction

The code in this repository focuses on creating code and testing various functionalities related to student information. It includes classes such as `Student` and `BloomTechStudent`, along with the `student_generator` function.

## Test Functions

### [test_student_instance](#test_student_instance)

This test function checks the instantiation of a `Student` object, ensuring that the attributes `name` and `age` are correctly assigned.

### [test_bloomtechstudent_instance](#test_bloomtechstudent_instance)

This test function verifies the instantiation of a `BloomTechStudent` object, checking if attributes such as `name`, `age`, and `major` are assigned correctly.

### [test_student_generator](#test_student_generator)

The purpose of this test function is to validate the functionality of the `student_generator` function. It ensures that the function generates a list of `BloomTechStudent` objects with the expected attributes.

## How to Run Tests

To run the tests, use the [pytest](https://docs.pytest.org/en/stable/) framework. If you don't have it installed, you can do so by running:


pip install pytest

After installing pytest, you can execute the tests by running the following command in the terminal:
pytest test_student.py

# License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

# Citation

If you use or find inspiration from this project, please consider citing it using the provided [CITATION](CITATION) file.

# Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

# Code of Conduct

We aim to foster an inclusive and respectful community. Please review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct.

# References

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Python Official Documentation](https://docs.python.org/3/)

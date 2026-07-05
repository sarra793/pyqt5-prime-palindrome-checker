# Prime Palindrome Checker (PyQt5)

A simple desktop application developed with **Python** and **PyQt5** that checks whether a number is a **prime palindrome**.

This project was created as an educational exercise inspired by the BAC SI algorithmic programming curriculum.

## Features

- Graphical user interface using PyQt5
- Input validation
- Prime number verification
- Palindrome verification
- Prime palindrome detection
- Custom square root implementation (Newton's Method)
- Custom string length function

## Project Structure

```
.
├── main.py
├── Interface.ui
└── README.md
```

## Requirements

- Python 3.8+
- PyQt5

Install PyQt5:

```bash
pip install PyQt5
```

## Running the Application

```bash
python main.py
```

Make sure `Interface.ui` is in the same directory as `main.py`.

## How It Works

The application performs the following steps:

1. Reads the user's input.
2. Validates that the input is a decimal integer with at least three digits.
3. Checks whether the number is prime.
4. Checks whether the number is a palindrome.
5. Displays the result in the interface.

## Algorithms

### Prime Test

Determines whether a number is prime by checking divisibility from **2** up to the square root of the number.

### Palindrome Test

Compares characters from the beginning and end of the string until the middle is reached.

### Square Root

Uses **Newton's Method** to compute the square root without relying on Python's `math.sqrt()`.

## Example

Input:

```
131
```

Output:

```
131 est premier palindrome.
```

Input:

```
123
```

Output:

```
123 n'est pas premier palindrome.
```

## Technologies

- Python
- PyQt5
- Qt Designer (.ui)

## Educational Purpose

This project demonstrates:

- GUI programming with PyQt5
- Functions and modular programming
- Basic algorithm design
- Input validation
- Event-driven programming

## License

This project is released under the MIT License.

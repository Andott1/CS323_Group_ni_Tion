# Python Calculator (Windows Style)

A simple, robust calculator application built with Python and PyQt6. It replicates the visual design and core functionality of the standard Windows 10/11 Calculator, featuring a dark mode UI and responsive text resizing.

## Features

* **Windows UI Replica:** Dark mode design using standard Windows colors and "Segoe UI" font.
* **Dynamic Display:**
* **Auto-Resizing Text:** Font shrinks automatically as numbers get longer to fit the screen.
* **Comma Formatting:** Automatically adds commas for readability (e.g., `1,000,000`).
* **16-Digit Limit:** Prevents overflow by capping input at 16 digits.

* **Core Math:** Handles Addition, Subtraction, Multiplication, and Division.
* **History View:** Displays the current operation above the main number (e.g., `50 +`).

## Requirements

* Python 3.x
* PyQt6

## Installation & Run

1. **Install Dependencies:**

```bash
pip install PyQt6
```

1. **Run the Application:**

```bash
python Main.py
```

## Project Structure

* `Main.py`: Contains the entry point, the `Calculator` UI class, and the `CalculatorOperations` logic class.

## Controls

* **0-9**: Enter numbers
* **Operators (+, -, ×, ÷)**: Perform calculations
* **=**: Calculate result
* **C**: Clear all (reset)
* **CE**: Clear current entry only
* **⌫**: Backspace
* **+/-**: Toggle positive/negative

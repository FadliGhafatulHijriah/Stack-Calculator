# Stack-Calculator

Stack-based calculator with infix-to-postfix conversion. Supports +, -, \*, /, ^ operators and parentheses. Built with Python.

#### 🧮 Stack Calculator

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Status](https://img.shields.io/badge/Status-Complete-success.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

#### 📖 Description

A **Stack-based Calculator** that evaluates mathematical expressions using the **Stack data structure**. The calculator converts infix notation (normal math) to postfix notation (Reverse Polish Notation) and evaluates it step-by-step.

This project demonstrates:

- ✅ Stack implementation
- ✅ Shunting Yard Algorithm (Infix to Postfix conversion)
- ✅ Postfix evaluation algorithm
- ✅ Proper code organization and documentation

#### ✨ Features

###### **Core Features:**

- **Stack Data Structure** - Implemented with Program Class
- **Infix to Postfix Conversion** - Using Dijkstra's Shunting Yard Algorithm
- **Postfix Evaluation** - Efficient evaluation using stack
- **Multi-operator Support:**
  - Addition (+)
  - Subtraction (-)
  - Multiplication (\*)
  - Division (/)
  - Exponentiation (^)
- **Parentheses Support** - Handles complex expressions with nested parentheses
- **Decimal Numbers** - Works with floating-point numbers

#### **User Experience Features:**

- **Interactive Mode** - Input multiple expressions
- **Step-by-step Visualization** - See how algorithm works
- **Calculation History** - Track all your calculations
- **Error Handling** - Clear error messages for invalid input
- **Quick Test Mode** - Automated testing

#### 🚀 Installation

##### Prerequisites

- Python 3.8 or higher

#### Setup

1. Clone the repository:

```bash
git clone https://github.com/FadliGhafatulHijriah/Stack-Calculator.git
cd Stack-Calculator
```

2. No external dependencies needed! Pure Python implementation.

3. Run the calculator:

```bash
cd src
python calculator.py
```

#### 🎮 How to Use

##### Interactive Mode

1. Run the program:

```bash
python calculator.py
```

2. Select Interactive Mode (option 1)

3. Enter mathematical expressions:

```
Expression: 3 + 4
Result: 7.0

Expression: ( 5 + 6 ) * 2
Result: 22.0

Expression: 10 / 2 + 3 * 4
Result: 17.0
```

**Important:** Always add SPACES between numbers and operators!

✅ Correct: `3 + 4 * 2`
❌ Wrong: `3+4*2`

##### Example Expressions

```
Simple:          3 + 4
                 Result: 7

With precedence: 3 + 4 * 2
                 Result: 11  (4*2 first, then +3)

With parentheses: ( 3 + 4 ) * 2
                  Result: 14  (3+4 first, then *2)

Complex:         ( 5 + 6 ) * ( 7 - 2 )
                 Result: 55

Exponentiation:  2 ^ 3 + 1
                 Result: 9
```

#### 📊 How It Works

##### 1. Stack Data Structure

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):      # Add to top
    def pop(self):             # Remove from top
    def peek(self):            # View top without removing
    def is_empty(self):        # Check if empty
```

**LIFO (Last In First Out):**

```
Push 5 → [5]
Push 10 → [5, 10]
Push 15 → [5, 10, 15]
Pop → 15 (Stack: [5, 10])
```

##### 2. Infix to Postfix Conversion

**Shunting Yard Algorithm:**

Example: `3 + 4 * 2`

| Step | Input | Stack  | Output     |
| ---- | ----- | ------ | ---------- |
| 1    | 3     | []     | 3          |
| 2    | +     | [+]    | 3          |
| 3    | 4     | [+]    | 3 4        |
| 4    | \*    | [+, *] | 3 4        |
| 5    | 2     | [+, *] | 3 4 2      |
| 6    | (end) | []     | 3 4 2 \* + |

Result: `3 4 2 * +`

##### 3. Postfix Evaluation

Example: `3 4 2 * +`

| Step | Token | Stack     | Operation                 |
| ---- | ----- | --------- | ------------------------- |
| 1    | 3     | [3]       | Push 3                    |
| 2    | 4     | [3, 4]    | Push 4                    |
| 3    | 2     | [3, 4, 2] | Push 2                    |
| 4    | \*    | [3, 8]    | Pop 2, Pop 4, Push 4\*2=8 |
| 5    | +     | [11]      | Pop 8, Pop 3, Push 3+8=11 |

Result: **11**

#### 🤝 Contributing

This is a learning project, but suggestions are welcome!

#### 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

#### 👨‍💻 Author

**Fadli Ghafatul Hijriah**

- GitHub: [@FadliGhafatulHijriah](https://github.com/FadliGhafatulHijriah)
- Instagram: [@fadl.bee](https://instagram.com/fadl.bee)
- University: Universitas Al-Azhar Indonesia - Informatics Engineering S1

⭐ If you found this helpful, please give it a star!

**Made with ❤️ for learning Data Structures & Algorithms**

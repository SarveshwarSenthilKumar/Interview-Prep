# Interview Preparation Repository

This repository serves as my personal knowledge base and practice space for technical interview preparation. It contains:

- Data structures and algorithms implementations
- Solutions to coding problems from various platforms (LeetCode, HackerRank, etc.)
- System design notes and examples
- Behavioral interview preparation
- Common interview questions and solutions
- Study plans and progress tracking
- Currently have done multiple CCC questions

## Structure

```
├── algorithms/         # Algorithm implementations and practice
├── data-structures/    # Data structure implementations
├── leetcode/          # LeetCode problem solutions
├── ccc/               # Canadian Computing Competition problems
├── system-design/     # System design concepts and examples
├── behavioral/        # Behavioral interview preparation
└── resources/         # Helpful resources and study materials
```

## CCC Problem Format

For Canadian Computing Competition (CCC) problems, each solution file includes the problem statement at the beginning of the file in a comment block, followed by the implementation. This makes it easy to understand the problem context when reviewing solutions.

Example format:
```python
"""
CCC '20 J1 - Dog Treats
Problem: https://dmoj.ca/problem/ccc20j1

Given three integers (s, m, l) representing the number of small, medium, and large treats,
calculate the total happiness score using the formula: 1s + 2m + 3l.
Return 'happy' if score >= 10, otherwise return 'sad'.
"""

def calculate_happiness(s, m, l):
    score = s + 2*m + 3*l
    return 'happy' if score >= 10 else 'sad'
```

## Getting Started

1. Clone this repository
2. Navigate to the relevant section
3. Start practicing!

## Contributing

This is a personal repository for interview preparation. While contributions aren't expected, feel free to use it as a reference or inspiration for your own preparation.

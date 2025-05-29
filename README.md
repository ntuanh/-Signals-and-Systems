# Signals and Systems Project (ET2060)

This project implements various signal processing and system analysis tools, focusing on linear difference equations and their solutions. It provides functionality for analyzing different types of input signals and visualizing their responses.

## Features

- Implementation of various input signals:
  - Exponential signals
  - Sine and cosine signals
  - Unit step signals
  - Impulse signals
  - Combined signals
- Solution of linear difference equations
- Visualization of signal responses
- Support for different types of input conditions

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - numpy
  - matplotlib
  - sympy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/-Signals-and-Systems.git
cd -Signals-and-Systems
```

2. Install required packages:
```bash
pip install numpy matplotlib sympy
```

## Usage

The project includes several example implementations in `LinearDifferenceEquation.py`. To run the examples:

```bash
python LinearDifferenceEquation.py
```

This will execute three example cases:
1. A simple homogeneous equation
2. An equation with exponential input
3. An equation with sinusoidal input

Each example will display:
- The general solution
- Numerical results
- A plot of the solution

## Project Structure

- `LinearDifferenceEquation.py`: Main implementation file containing:
  - Input signal classes
  - Equation solving functions
  - Visualization tools
  - Example implementations

## Contributing

Feel free to submit issues and enhancement requests!

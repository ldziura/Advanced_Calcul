
# Advanced Calculator

Advanced Calculator is a project made as a part of a larger project.
It allow for user input of any mathematical formula as a string, with any number of unknowns.
The formula then gets solved with the value associated for each unknowns





## Features

- Support most mathematical operator : +, -, *, /, sqrt, log, sin, cos, tan, mod, pow, factorial, abs, floor, ceil
- Support for constant such as PI
- Built-in check adn sanitization for inputs
- Built-in Exception error for most errors
- How-to-use example in main.py
- Fast : Average of 0.0003s per solve
- Built-in 2670 tests with edge cases with inputs such as 2^32, 2^64
- Comment at every step with optional print to understand how the code works
 




## Example

With the code provided in main.py this is an example input/output :


Enter a formula: sqrt(x) + (x*y)/2

Enter the number of unknowns: 2

Enter the name of the unknown 1 : x

Enter the value of x : 3

Enter the name of the unknown 2 : y

Enter the value of y : 8

sqrt(x) + (x*y)/2 with {'x': 3.0, 'y': 8.0} = 13.732050807568877

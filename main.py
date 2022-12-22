from ComputeFormula import compute_formula

# Function that asks the user for an input formula, the number of unknowns, the name and values of unknowns and solves the formula
# exemple log :

'''
Enter a formula: sqrt(x) + (x*y)/2
Enter the number of unknowns: 2
Enter the name of the unknown 1 : x
Enter the value of x : 3
Enter the name of the unknown 2 : y
Enter the value of y : 8
sqrt(x) + (x*y)/2 with {'x': 3.0, 'y': 8.0} = 13.732050807568877
'''


def input_and_solve() -> str:
    """
    Function that asks the user for an input formula, the number of unknowns, the name and values of unknowns and solves the formula

    Example of a log:

    Enter a formula: sqrt(x) + (x*y)/2 \n
    Enter the number of unknowns: 2 \n
    Enter the name of the unknown 1 : x \n
    Enter the value of x : 3 \n
    Enter the name of the unknown 2 : y \n
    Enter the value of y : 8 \n
    sqrt(x) + (x*y)/2 with {'x': 3.0, 'y': 8.0} = 13.732050807568877 \n

    :return: str
    """

    input_formula = input("Enter a formula: ")

    number_of_unknowns = input("Enter the number of unknowns: ")
    # check if the number of unknowns is a number
    if number_of_unknowns.isdigit():
        number_of_unknowns = int(number_of_unknowns)
    else:
        print("Number of unknowns must be a number")
        exit()

    unknown_dict = {}
    for i in range(int(number_of_unknowns)):

        unknown_name = input(f"Enter the name of the unknown {i + 1} : ")
        # check if unknown name is a string
        if not unknown_name.isalpha():
            print("Unknown name must be a string")
            exit()

        unknown_value = input(f"Enter the value of {unknown_name} : ")
        # check if unknown value is a number
        if not unknown_value.isnumeric():
            print("Unknown value must be a number")
            exit()

        unknown_dict[unknown_name] = float(unknown_value)

    try:
        print(f"{input_formula} with {unknown_dict} = {compute_formula(input_formula, unknown_dict)}")
        return compute_formula(input_formula, unknown_dict)
    except Exception as e:
        print("An error occurred:", e)
        exit()


input_and_solve()



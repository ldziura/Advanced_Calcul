import math
import re


def get_sqrt_value(string):
    # Compile a regular expression pattern that matches a string
    # (possibly containing whitespace characters) inside a pair of
    # parentheses after the 'math.sqrt' part of the string
    pattern = re.compile(r"math\.sqrt\((.+?)\)")

    # Use the findall method to extract all matches of the pattern
    # in the input string
    matches = pattern.findall(string)

    # If there is a match, return the value inside the parentheses
    # (i.e. the first and only element of the list of matches)
    if matches:
        return matches[0]
    else:
        # If there is no match, return an empty string
        return ""


# # print(f"{get_sqrt_value('math.sqrt(-25)')} should be -25 ")

def get_operator_value(string: str, operator: str):
    # Find the index of the first occurrence of 'mod(' in the string
    start_index = string.index(f'{operator}(')

    # Find the index of the first occurrence of ',' after 'mod('
    end_index = string.index(',', start_index)

    # Extract the string between 'operator(' and ','
    x = string[start_index + (len(operator)+1):end_index]

    # Find the index of the last occurrence of ')' in the string
    end_index = string.rindex(')')

    # Extract the string between the first ',' and the last ')'
    y = string[end_index - 1]

    return [x, y]

# Test the function with some examples
# # print(get_operator_value('mod(x,y)', 'mod'))  # should return ['x', 'y']
# # print(get_operator_value('mod(x,7)', 'mod'))  # should return ['x', '7']
# # print(get_operator_value('mod((sqrt(25)+3), 8)', 'mod'))  # should return ['sqrt(25)+3', '8']


def is_word(word: str) -> bool:
    # Use a regular expression to check if the string contains only letters
    return bool(re.match(r'^[a-zA-Z]+$', word))

def is_number(x):
    return isinstance(x, (int, float))


def dict_split_comma(d: dict):
    split_operator = ['math.fmod(', 'math.pow(']

    new_list = d.copy()

    for key, value in d.items():

        for operator in split_operator:
            if key.find(operator) != -1:
                # print(f"found {operator} in {key}")
                break
        else:

            if key.find(',') != -1:
                n_k = key.split(',')
                # print(f"n_k = {n_k} at nest level {value}")
                n_v1 = f"{n_k[0]})".replace(' ', '')
                n_v2 = f"({n_k[1]}".replace(' ', '')

                # print(f"n_v1 = {n_v1}")
                # print(f"n_v2 = {n_v2}")

                new_list.pop(key)
                new_list[n_v1] = value
                new_list[n_v2] = value

    return new_list


def check_parentheses(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack


def is_well_formed(formula: str, unknowns=None) -> bool:
    # check if any ',' character is enclosed in parentheses

    if check_parentheses(formula):
        pass
    else:
        raise ValueError("Parentheses are not matched")

    # check if the formula is an empty string or only whitespaces
    if formula.isspace() or formula == '':
        raise ValueError("Formula is empty")

    # define the regex pattern
    # pattern = r"^\s*(?:sqrt|log|sin|cos|tan|floor|ceil|factorial|abs|mod|PI|pow)\s*\(|[-+*/(),0-9.]+|\s*$"
    # pattern = r"\s*(?:sqrt|log|sin|cos|tan|floor|ceil|factorial|abs|mod|PI|pow)\s*\(\s*((?:(?:[-+*/(),0-9x]|(?:\s*(?:sqrt|log|sin|cos|tan|floor|ceil|factorial|abs|mod|PI|pow)\s*\())\s*[^()]*\s*)*)\s*\)|[-+*/(),0-9x]+|\s*"
    pattern = r"^\s*[-+*/()0-9.xyz,sqrtlogsincostanfloorceilfactorialabsmodPIpow\s]+\s*$"


    #add unknowns
    if unknowns is not None:

        char_to_add = unknowns
        index = pattern.find("sqrt")
        pattern = pattern[:index] + ''.join(char_to_add) + pattern[index:]

    # compile the pattern
    regex = re.compile(pattern)

    # test the string against the pattern
    matches = regex.findall(formula)

    # print the result
    if matches:
        # print("The string matches the pattern.")
        return True
    else:
        # print("The string does not match the pattern.")
        return False

    # Use a regular expression to check if the formula is well-formed
    # return bool(re.match(r"^\s*[-+*/()0-9.x,sqrtlogsincostanfloorceilfactorialabsmodPIpow\s]+\s*$", formula))
    # return bool(re.match(r"^\s*(?:sqrt|log|sin|cos|tan|floor|ceil|factorial|abs|mod|PI|pow)\s*\(|[-+*/(),0-9.x]+|\s*$", formula))

# print(f"is_well_formed('x+y') = {is_well_formed('x+y')}")

# The input string
string = "sqrt( sqrt(7*7) + sin(cos(12/6) + tan(PI/4)) + (7*9+2) * log(4+8 * sqrt(64))) + (7*(3+2 / (8-6)) - floor(sqrt(PI*5*5))) + tan(PI/4) + y*PI" # 44.07065812843417
# string = 'factorial(ceil(sin(7)+5))' # 720
# string = 'log(10)' #2.302585092994046
# string = 'mod(7*2, 3) + 4' #6
# string = 'pow((mod(sqrt(5*5) + mod(44, 55) * mod( pow(5, 3) , 65), 3 * mod(88, 77)) + 4), 2) + x' #86
# string = '(8+6*8) + sqrt(mod(7*2+(x+5), 3) + 4 - 50) + sqrt((8*7+5)+7)' # Can't sqrt with value (-46.0) in (56) + math.sqrt(-46.0) + math.sqrt(68)
# string = "(7*9+2) * log(4+8 * sqrt(64) )" #274.26800083644696
# string = "(8+5) + (3*7 + mod(5,2))" #35
# string = 'x*y'




def compute_formula(input_string: str, unknown_value=None) -> str:


    #Check if unknown_value is a dictionary
    if unknown_value is not None:
        if isinstance(unknown_value, dict):
            pass
        else:
            raise ValueError("unknown_value is not a dictionary")



    # Check if the input string is well-formed
    try:
        iwf = is_well_formed(input_string, unknowns=list(unknown_value.keys()))
        if iwf == False:
            return "Formula is not well formed"
    except ValueError as e:
        return str(e)
    except:
        return "Unknown error"


    # Initialize an empty dictionary to hold the results
    results = {}

    # A stack to keep track of nested parentheses
    stack = []

    string = input_string

    string = string.replace("PI", "math.pi")

    string = string.replace("sqrt(", "math.sqrt(")
    string = string.replace("log(", "math.log(")  # log(x) is the natural logarithm of x

    # trigo in radians
    string = string.replace("sin(", "math.sin(")
    string = string.replace("cos(", "math.cos(")
    string = string.replace("tan(", "math.tan(")
    #
    # of the form : mod(x, y) and pow(x, y)
    string = string.replace("mod(", "math.fmod(")
    string = string.replace("pow(", "math.pow(")
    #
    # # factorial and absolute
    string = string.replace("factorial(", "math.factorial(")
    string = string.replace("abs(", "math.fabs(")

    # # Floor and ceilling
    string = string.replace("floor(", "math.floor(")
    string = string.replace("ceil(", "math.ceil(")

    # Check unknowns values

    for key, value in unknown_value.items():
        if is_word(key):

            #check if value is a number
            if is_number(value):

                if str(key) in input_string:
                    if value is not None:
                        # Replace x with its value in the formula
                        string = string.replace(str(key), f"({str(value)})")
                    else:
                        # print(f"'x' must be defined for {input_string}")
                        return 'Undefined x'
            else:
                raise ValueError(f"Value of : {key} = {value} is not a number")

        else:
            raise ValueError(f"Unknown key {key} is not a word")


    # print(f"string = {string}")

    # Loop through each character in the string
    for i, c in enumerate(string):
        # If the character is an opening parenthesis, add it to the stack
        if c == "(":
            stack.append(i)
        # If the character is a closing parenthesis, pop the last opening parenthesis from the stack
        # and calculate the length of the substring between the two parentheses
        elif c == ")":
            start = stack.pop()
            # length = i - start + 1
            # Add the substring to the dictionary with its nesting level as the value
            # print(f"len stack = {len(stack)} for {string[start:i+1]}")

            # if len(stack) > 0:
            results[string[start:i + 1]] = len(stack) + 1
            # else:
            #     print(f"stack <= 0, string = {string}")
            #     results[string] = -1

    # If the first and last characters in the string are parentheses, add them to the dictionary
    # with a nesting level of 0
    # if string[0] == "(" and string[-1] == ")":
    #     results[string[0:-1]] = 0

    # adds the whole formula to the dictionary with a nesting level of 0
    results[string] = 0

    # Print the final dictionary
    # print(results)
    def sort_dict(d):
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    sort_dict = sort_dict(results)
    # print("\n")
    # print(f"sort_dict = {sort_dict}")
    # print("\n")

    sorted_dict = dict_split_comma(sort_dict)
    # print(f"sorted_dict = {sorted_dict}")

    solved_list = {}
    all_replaced = []

    for k, v in sorted_dict.items():

        partial_solve = {}

        k_new = k

        #         # print(f"solving {k} for nest level {v}")
        # check if k has already been solved on the previous level
        #         # print(f"checking if {k} has already been solved")

        if v + 1 in solved_list:
            prev_solv = solved_list[v + 1]
            for p in prev_solv:
                #                 # print(f"prev solv {p}")
                for k2, v2 in p.items():
                    if k_new.find(str(k2)) != -1:
                        #                         # print(f"found {k2} = ({str(v2)}) in {k}")
                        if str(v2)[0] == '(' and str(v2)[-1] == ')':
                            k_new = k_new.replace(str(k2), f"{str(v2)}")
                        else:
                            k_new = k_new.replace(str(k2), f"({str(v2)})")
                        # print(f"\nreplaced {k2} with ({str(v2)}) in {k} --- new = {k_new}\n")
                        # # print(f"new k = {k_new}")

        if k_new != k:
            all_replaced.append(k_new)

        # check if there is a squareroot in the string
        if k_new.find("sqrt") != -1:
            # print(f"found sqrt in {k_new}")
            # print(f"replacing sqrt with math.sqrt")
            # k_new = k_new.replace("sqrt", "math.sqrt")
            # print(f"new k = {k_new}")

            # print(f"found sqrt with value ({get_sqrt_value(k_new)}) in {k_new}")
            v_sqrt = get_sqrt_value(k_new)
            if v_sqrt != "":
                # check if v_sqrt < 0
                # print(float(v_sqrt))
                try:
                    if float(v_sqrt) < 0:
                        # print("Can't divide by a negatif number")
                        return f"Can't sqrt with value ({get_sqrt_value(k_new)}) in {k_new}"
                except:
                    pass


        try:
            partial_solve[k] = eval(k_new)
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Can't divide by 0 in {k_new}")
        except ValueError as e:
            raise ValueError(f"Value Error occurred in {k_new} : {e}")
        except SyntaxError as e:
            raise SyntaxError(f"Syntax Error occurred in {k_new} : {e}")
        except NameError as e:
            raise NameError(f"Name Error occurred in {k_new} : {e}")

        if v in solved_list:
            solved_list[v].append(partial_solve)
        else:
            solved_list[v] = [partial_solve, ]

    # print(solved_list)
    # print(all_replaced)

    # print("\n\n")

    final_string = string

    if solved_list:

        for p in solved_list[0]:
            # print(p)
            for k2, v2 in p.items():

                # print(f"final string = {final_string}")

                if string.find('mod') != -1 or string.find('pow') != -1:
                    # print("found mod")
                    # mod_values = get_operator_value(string, 'mod')
                    # print(f"mod values = {mod_values}")

                    if string.find(str(k2)) != -1:
                        # print(f"found {k2} in {string} MOD VALUE -- {v2}")

                        # print(f"{k2[0]} {k2[-1]} START END")

                        if (k2[0] == '(' and k2[-1] == ')') and (str(v2)[0] == '(' and str(v2)[-1] == ')'):
                            # print("no need to add parenthesis")
                            final_string = final_string.replace(str(k2), f"{str(v2)}")
                        else:
                            final_string = final_string.replace(str(k2), f"({str(v2)})")
                        break

                if string.find(str(k2)) != -1:
                    # print(f"\n found {k2} in {string} \n")
                    final_string = final_string.replace(str(k2), f"({str(v2)})")

    # print(final_string)
    # print(f"{final_string} = {eval(final_string)}")

    # print(f"final string = {final_string}")
    #
    # if final_string.find("sqrt") != -1:
    #     # print(f"found sqrt in {k_new}")
    #     # print(f"replacing sqrt with math.sqrt")
    #     # k_new = k_new.replace("sqrt", "math.sqrt")
    #     # print(f"new k = {k_new}")
    #
    #     print(f"found sqrt with value ({get_sqrt_value(final_string)}) in {final_string}")
    #     v_sqrt = get_sqrt_value(final_string)
    #     if v_sqrt != "":
    #         # check if v_sqrt < 0
    #         #             # print(float(v_sqrt))
    #         if float(v_sqrt) < 0:
    #             # print("Can't divide by a negatif number")
    #             return "Can't divide by a negatif number"

    # return eval(final_string)

    try:
        return eval(final_string)
    except ZeroDivisionError:
        raise ZeroDivisionError("Can't divide by 0 in {final_string}")
    except ValueError as e:
        raise ValueError(f"Value Error occurred in {final_string} : {e}")



# unknown_dict = {'x': 5, 'y': 2}

# print(compute_formula(string, unknown_dict))



# TODO : Clean and github


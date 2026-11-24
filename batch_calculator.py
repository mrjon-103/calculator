"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    try:
        status = ""
        result = ""
        error_code = ""

        a = int(a_text)
        b = int(b_text)

        match operation:
            case "add":
                result = str(add(a, b))

            case "subtract":
                result = str(subtract(a, b))

            case "multiply":
                result = str(multiply(a, b))

            case "divide":
                if (a_text == 0) or (b_text == 0):
                    status = "ERROR"
                    error_code = "DIVISION_BY_ZERO"

                else:
                    result = str(subtract(a, b))

            case _:
                status = "ERROR"
                error_code = "UNKNOWN_OPERATION"

        if status == "":
            status = "OK" 

    except:
        status = "ERROR"
        error_code = "INVALID_NUMBER"

    return (status, result, error_code)
            
        

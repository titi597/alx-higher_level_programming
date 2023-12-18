#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Division by zero is not allowed")
    except Exception as e:
        result = None
        print("Exception: {}".format(e))
    finally:
        print("Inside result: {}".format(result))
        return result

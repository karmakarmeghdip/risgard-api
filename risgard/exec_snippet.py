import sys
import io

def ronaldo():
    print('I am Ronaldo, the legend!')

'''
Takes in python snippet executes it and return the output
'''
def exec_snippet(snippet):
    old_stdout = sys.stdout
    result = io.StringIO()
    sys.stdout = result
    
    try:
        exec(snippet, globals())
    except SyntaxError as err:
        return f"{err.__class__.__name__}\n"\
                f"Line: {err.lineno}\n"\
                f"Details: {err.args[0]}"
    except Exception as err:
        return f"{err.__class__.__name__}\n"\
                f"Details: {err.args[0]}"

    sys.stdout = old_stdout
    return result.getvalue()
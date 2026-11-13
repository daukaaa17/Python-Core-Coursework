from typing import Dict
import time
execution_time: Dict[str, float] = {}

def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = fn(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time  # Calculate execution time
        execution_time[fn.__name__] = elapsed_time  # Store in dictionary
        return result  # Return the original function's result

    return wrapper

@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b
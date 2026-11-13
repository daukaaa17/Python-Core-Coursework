import time
def log(fn):
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.time()

        # Execute the decorated function
        result = fn(*args, **kwargs)

        # Record end time and calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time

        # Prepare log entry
        args_repr = ", ".join(f"{k}={v}" for k, v in zip(fn.__code__.co_varnames, args))
        kwargs_repr = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        log_message = (
            f"{fn.__name__}; args: {args_repr}; kwargs: {kwargs_repr}; "
            f"execution time: {execution_time:.2f} sec.\n"
        )

        # Write log entry to file
        with open("log.txt", "a") as log_file:
            log_file.write(log_message)

        # Return the function's result
        return result
    return wrapper
@log
def foo(a, b, c=0):
    time.sleep(0.1)  # Simulating some delay
    return a + b + c
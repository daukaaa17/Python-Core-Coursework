from contextlib import ContextDecorator
from datetime import datetime
import traceback

class LogFile(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file
        self.start_time = None

    def __enter__(self):
        # Record the start time
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Calculate execution time
        end_time = datetime.now()
        run_time = end_time - self.start_time

        # Prepare log entry
        error_message = None
        if exc_type is not None:
            # Format the exception message
            error_message = str(exc_value)

        log_entry = (
            f"Start: {self.start_time} | "
            f"Run: {run_time} | "
            f"An error occurred: {error_message}\n"
        )

        # Append the log entry to the log file
        with open(self.log_file, "a") as log:
            log.write(log_entry)

        # Reraise the exception if it occurred
        return exc_type is None  # False if there was an exception, to propagate it

# Example Usage
@LogFile('my_trace.log')
def test_function():
    pass
    # Uncomment the following line to test exception logging:
    # raise ZeroDivisionError("division by zero")

try:
    test_function()
except Exception as e:
    print(f"An exception occurred: {e}")

import os

class Cd:
    def __init__(self, new_dir):
        # Validate that the provided directory exists and is a directory
        if not os.path.isdir(new_dir):
            raise ValueError(f"The directory '{new_dir}' does not exist or is not a valid directory.")
        self.new_dir = new_dir
        self.prev_dir = None

    def __enter__(self):
        # Save the current working directory
        self.prev_dir = os.getcwd()
        # Change the working directory to the new directory
        os.chdir(self.new_dir)
        return self.new_dir

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Restore the previous working directory
        os.chdir(self.prev_dir)

# Example Usage
try:
    with Cd('/tmp'):
        print(f"Inside context: Current directory is {os.getcwd()}")
        # Perform actions in the new directory
    print(f"Outside context: Back to {os.getcwd()}")
except ValueError as e:
    print(e)

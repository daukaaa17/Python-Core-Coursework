import os
import shutil
import tempfile

class TempDir:
    def __init__(self):
        self.temp_dir = None
        self.prev_dir = None

    def __enter__(self):
        # Save the current working directory
        self.prev_dir = os.getcwd()
        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()
        print(f"Temporary directory created: {self.temp_dir}")
        # Change the working directory to the temporary directory
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Ensure current working directory is restored
        os.chdir(self.prev_dir)
        print(f"Restored working directory: {self.prev_dir}")
        # Safely remove the temporary directory
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            print(f"Temporary directory removed: {self.temp_dir}")
        else:
            print(f"Temporary directory already removed: {self.temp_dir}")

# Example Usage with Debugging
try:
    with TempDir() as temp_dir:
        print(f"Inside context: Temporary directory is {temp_dir}")
        # Create a file in the temporary directory
        file_path = os.path.join(temp_dir, "test.txt")
        with open(file_path, "w") as f:
            f.write("Sample content.")
        print(f"Created file: {file_path}")
        # List contents in the temporary directory
        print(f"Contents of temp dir: {os.listdir(temp_dir)}")
except Exception as e:
    print(f"An error occurred: {e}")

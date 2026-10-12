import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Running [{func. __name__}]... Executed in {execution_time: .2f} seconds")

        return result
    return wrapper

@log_execution
def process_data():
    print("Processing data...")
    time.sleep(1.5)
    return "Data processed successfully."

process_data()
import time
import random

# Define the timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.time()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Record end time
        end_time = time.time()
        
        # Calculate elapsed time
        elapsed = end_time - start_time
        print(f"Time taken to run '{func.__name__}': {elapsed:.4f} seconds")
        
        return result
    return wrapper

# Example function to demonstrate the timer decorator
@timer
def random_sleep():
    # Generate a random sleep duration between 0.5 and 1.5 seconds
    duration = random.uniform(0.5, 1.5)
    print(f"Sleeping for {duration:.2f} seconds...")
    time.sleep(duration)
    print("Done sleeping!")

# Call the decorated function
random_sleep()
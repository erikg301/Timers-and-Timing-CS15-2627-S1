import time

# Set start_time to the current time
start_time = time.monotonic()

# Define how long the timer should run for
timer_length = 1

while True:
    # Update the current_time
    current_time = time.monotonic()

    # Calculate the elapsed_time from the difference between current_time and start_time
    elapsed_time = current_time - start_time

    # Compare elapsed_time to timer_length
    if elapsed_time >= timer_length:
        print("Timer complete!")
        print("Hello")

        # Restart timer
        start_time = time.monotonic()




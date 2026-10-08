import time
import random

# reaction time game
# press enter when you see GO!

fastest = None

print("Reaction Time Game!")
print("Press Enter as fast as you can when you see GO!")

for attempt in range(1, 6):
    print()
    print("Attempt " + str(attempt))
    print("Get ready...")

    # wait 2 to 5 seconds
    wait_time = random.uniform(2, 5)
    start_time = time.monotonic()

    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time

        if elapsed_time >= wait_time:
            break

    print("GO!")
    go_time = time.monotonic()

    input()

    end_time = time.monotonic()
    reaction_time = end_time - go_time

    print("Reaction time: " + str(round(reaction_time, 3)) + " seconds")

    # save the fastest time
    if fastest == None or reaction_time < fastest:
        fastest = reaction_time

print()
print("Fastest time: " + str(round(fastest, 3)) + " seconds")
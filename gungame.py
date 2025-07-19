import time
import random

print("Welcome to the Gun Game!")
print("Type 'shoot' as fast as you can when a target appears.\n")

score = 0
rounds = 3

for i in range(1, rounds + 1):
    wait_time = random.uniform(2, 4)
    print(f"Round {i}: Get ready...")
    time.sleep(wait_time)
    print("TARGET! Type 'shoot' now!")

    start_time = time.time()
    action = input("> ").strip().lower()
    reaction_time = time.time() - start_time

    if action == "shoot" and reaction_time < 2.0:
        print(f"Hit! Reaction time: {reaction_time:.2f} seconds.")
        score += 1
    else:
        print("Enemy down!")

print(f"\nGame over! Your score: {score}/{rounds}")
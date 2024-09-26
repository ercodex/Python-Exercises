import random
import time

while True:
    c = 1
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    answer = int(input(f"---------- {a} x {b} ? ----------"))
    while c:
        if answer == a*b:
            print("Dogru bildin!")
            time.sleep(0.5)
            c = 0
        if answer != a*b:
            print("Tekrar dene!")
            answer = int(input(f"---------- {a} x {b} ? ----------"))
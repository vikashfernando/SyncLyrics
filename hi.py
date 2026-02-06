import time

lyrics = [
    ("Hello from the other side", 2),
    ("I must have called a thousand times", 3),
    ("To tell you I'm sorry", 2)
]

for line, wait_time in lyrics:
    print(line)
    time.sleep(wait_time)

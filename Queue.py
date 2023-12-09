import queue

ar_queue = queue.Queue()
value = [
    ("Hi! "),
    ("This is Python "),
    ("Program")
]

for i in value:
    ar_queue.put(i)

pop_value = ar_queue.get()

print("value added to the queue:", value)
print("popped value from the queue:", pop_value)

import time

def task(name):
    print(f"{name} стартует")
    time.sleep(2)
    print(f"{name} завершён")

def main():
    task("A")
    task("B")

main()

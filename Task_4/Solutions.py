import json
import geometry
import platform
from datetime import datetime

# Problem 1
def safe_divide():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = num1 / num2
            print("Result =", result)
            break

        except ZeroDivisionError:
            print("Error: You can't divide by zero! Try again.\n")

        except ValueError:
            print("Error: Please enter valid numbers only! Try again.\n")

safe_divide()


# Problem 2
def save_inventory(data):
    file = open("inventory.json", "w")
    json.dump(data, file)
    file.close()

def load_inventory():
    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return {}

inventory = {"apple": 5, "banana": 3}

save_inventory(inventory)
data = load_inventory()

print(data)


# Problem 3
def write_log(message):
    file = open("log.txt", "a")
    file.write(message + "\n")
    file.close()

def read_logs():
    file = open("log.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        print(line.strip())

write_log("System started")
write_log("User logged in")
write_log("Error detected")

read_logs()

# Problem 4
area = geometry.circle_area(7)
perimeter = geometry.square_perimeter(6)

print("Area of circle =", area)
print("Perimeter of square =", perimeter)

# Problem 5
try:
    file = open("config.json", "r")
    print("System Ready.")
    file.close()

except FileNotFoundError:
    data = {"mode": "default"}
    file = open("config.json", "w")
    json.dump(data, file)
    file.close()
    print("Config file created.")

# Problem 6 
def log_system_info():
    file = open("sys_log.txt", "a")
    file.write("OS: " + platform.system() + "\n")
    file.write("Time: " + str(datetime.now()) + "\n")
    file.close()

def main():
    log_system_info()

if __name__ == "__main__":
    main()

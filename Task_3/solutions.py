import random

# Problem 1
def pick_winner(names):
    if not names:
        return "No participants!"
    winner = random.choice(names)
    return f"Congratulations {winner}! You won!"
print(pick_winner(["Ali", "Sara", "Mona"]))

# Problem 2
def move_player(position, direction):
    x, y = position
    if direction == "up":
        return (x, y + 1)
    elif direction == "down":
        return (x, y - 1)
    elif direction == "left":
        return (x - 1, y)
    elif direction == "right":
        return (x + 1, y)
    return position
print(move_player((0, 0), "up"))

# Problem 3
def common_elements(set1, set2):
    return set1.intersection(set2)
print(common_elements({1,2,3}, {2,3,4}))

# Problem 4
def get_unique_lottery():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 50))
    return numbers
print(get_unique_lottery())

# Problem 5
def calculate_bill(prices, items_bought):
    total = 0
    for item in items_bought:
        if item in prices:
            total += prices[item]
    return total
print(calculate_bill({"apple":0.5, "banana":0.3}, ["apple","banana","apple"]))

# Problem 6
def analyze_grades(grades):
    return {
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
    }
print(analyze_grades([70,80,90]))

# Your Name
t = int(input())

for i in range(t):
    n = int(input())
    s, name = input().split()

    if sorted(s) == sorted(name):
        print("YES")
    else:
        print("NO")



# Spy Detected!
noOfLines = int(input())

for line in range(noOfLines):
    length = int(input())
    arr = input().split(" ")

    tallyDict = dict.fromkeys(set(arr), 0)

    for i in range(length):
        tallyDict[arr[i]] += 1
    
    spyElement = min(tallyDict, key=tallyDict.get)
    
    print(f"Output: {arr.index(spyElement)+1}")


# Way Too Long Words
n = int(input())

for i in range(n):
    word = input()

    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])


# sum
noOfLines = int(input())

for line in range(noOfLines):
    strOfInts = input()
    array = strOfInts.split(" ")
    intArr = [int(x) for x in array]

    biggestInt = 0
    sum = 0
    for number in intArr:
        sum += number
        if biggestInt < number:
            biggestInt = number

    sum -= biggestInt
    if sum == biggestInt:
        print("Output: YES")
    else:
        print("Output: NO")

# Division?
t = int(input())

for i in range(t):
    rating = int(input())

    if rating >= 1900:
        print("Division 1")
    elif rating >= 1600:
        print("Division 2")
    elif rating >= 1400:
        print("Division 3")
    else:
        print("Division 4")



# Team
n = int(input())
count = 0

for i in range(n):
    a, b, c = map(int, input().split())

    if a + b + c >= 2:
        count += 1

print(count)

# Tram
n = int(input())

current = 0
max_capacity = 0

for i in range(n):
    a, b = map(int, input().split())

    current = current - a   # الناس اللي بتنزل
    current = current + b   # الناس اللي بتركب

    if current > max_capacity:
        max_capacity = current

print(max_capacity)


# Plus One on the Subset
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(max(a) - min(a))
    

# George and Accommodation
n = int(input())
count = 0

for i in range(n):
    p, q = map(int, input().split())

    if q - p >= 2:
        count += 1

print(count)


# Borze
s = input()

i = 0
result = ""

while i < len(s):
    if s[i] == '.':
        result += "0"
        i += 1
    else:  # s[i] == '-'
        if s[i + 1] == '.':
            result += "1"
        else:
            result += "2"
        i += 2

print(result)


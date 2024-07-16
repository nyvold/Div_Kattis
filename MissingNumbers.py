inp = int(input())
list = [int(input()) for i in range(inp)]
numbs = [i for i in range(1, list[len(list)-1])]
missingNumbs = [i for i in numbs if not i in list]

if len(missingNumbs) == 0:
    print("good job")
else:
    for num in missingNumbs:
        print(num)
num = int(input())
list = []

while num != 1:
    list.append(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

list.append(1)

print(" ".join(map(str, list)))

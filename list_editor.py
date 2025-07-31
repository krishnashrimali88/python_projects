list = []

num = input()
num = int(num)


def list_ops():
    a = input()
    a = str(a)

    if a.startswith("insert"):
        parts = a.split()

        alpha = parts[1]
        beta = parts[2]

        num1 = int(alpha)
        num2 = int(beta)

    elif a.startswith("remove"):
        parts1 = a.split()
        gamma = parts1[1]
        num3 = int(gamma)
    
    elif a.startswith("append"):
        parts2 = a.split()
        delta = parts2[1]
        num4 = int(delta)
    
    if a == 'print':
        print(list)

    elif a == 'reverse':
        list.reverse()

    elif a == 'sort':
        list.sort()

    elif a == 'pop':
        list.pop()

    elif a.startswith('insert'):
        list.insert(num1,num2)

    elif a.startswith('remove'):
        list.remove(num3)

    elif a.startswith('append'):
        list.append(num4)


for i in range(1,num+1):
    list_ops()        
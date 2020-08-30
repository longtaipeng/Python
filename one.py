def la(s1, s2):
    print("新串为：", end='')
    if len(s1) and len(s2) ==0:
        return (s1+s2)
    else:
        s1.split()
        s2.split()
        if len(s1) > len(s2):
            for i in range(len(s2)):
                print(s1[i], end='')
                print(s2[i], end='')
            print(s1[len(s2):])
        elif len(s1)<len(s2):
            for i in range(len(s1)):
                print(s1[i], end='')
                print(s2[i], end='')
            print(s1[len(s2):])
        else:
            for i in range(len(s1)):
                print(s1[i], end='')
                print(s2[i], end='')

print("请输:",end='')
s1 = input()
print("2:", end='')
s2 = input()
la(s1, s2)
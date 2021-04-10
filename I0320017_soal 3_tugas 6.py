bawah = 10
atas = 25
for num in range(bawah, atas):
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            break
    else:
        print(num, "adalah bilangan prima" )


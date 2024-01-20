a = '1'
b = float(0)
while a != '0':
    a = input('Enter an amount followed by "h" without space for with tax, w for the whole amount, t for whole amount plus tax; enter 0 to finish\n >')
    if a == '0':
        print (b)
        break
    elif "h" in a:
        a = a[:-1]
        a = float(a)
        a = a + (a*0.15)
        b = float(b) + (a/2)
    elif "w" in a:
        a = a[:-1]
        a = float(a)
        b = float(b) + a
    elif "t" in a:
        a = a[:-1]
        a = float(a)
        a = a + (a*0.15)
        b = float(b) + a
    else:
        b = b + (float(a)/2)

# Döngü içeren kuvvet fonksiyonu:
def power_loop(x, e):

    t = 1

    for i in range(e):

        t *= x

    return t

# Recursive kuvvet fonksiyonu:
def power_recursive(x, e):

    if(e == 0):
        return 1
    
    elif(e == 1):
        return x
    
    elif(e % 2 == 0):
        return power_recursive(x * x , e // 2)
    
    elif((e % 2) != 0):
        return power_recursive(x * x, e // 2) * x

# x = taban, e = kuvvet:
x = 6
e = 3
print(x, "^", e)

# Döngü içeren kuvvet fonksiyonu çağrısı:
print("power_loop = ", power_loop(x, e))

# Recursive kuvvet fonksiyonu çağrısı:
print("\npower_recursive = ", power_recursive(x, e))
print("\n")
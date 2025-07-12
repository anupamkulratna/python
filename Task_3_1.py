x = int(input("Enter the number : "))

def factortial(x) :
    if x < 2 :
        return 1
    else :
        return x * (factortial(x-1))
result = factortial(x)
print(result)

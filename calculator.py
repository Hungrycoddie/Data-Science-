

Y = float (input ("what is Y ? "))
Z =  X / Y
print (f"{Z:.2f,}")

#**************************************
#define A variale function  for square
def main():
    x=int(input("what's x?"))
    print ("x squared is", square(x))


def square (n):
    #return n*n
    return pow(n,2)

main()


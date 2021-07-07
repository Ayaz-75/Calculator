


def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return (n1*n2)

def div(n1,n2):
    return(n1*n2)


opeations={
 "+":add,
 "-":sub,
 "*":mult,
 "/":div  
}


should_continue=True

while should_continue:
    first_number=int(input("Enter the fisrt number: "))
    second_number=int(input("Enter the second number: "))

    for symbol in opeations:
        print(symbol)
    operation_symbol=input("Pick any operation given above: ")

    calculation_function=opeations[operation_symbol]
    answer=calculation_function(first_number,second_number)

    print(f"{first_number} {operation_symbol} {second_number} ={answer}")


    choice=input("Do you want to continue or not yes to continue and not to end")
    if choice=="yes":
        should_continue=True
    else:
        should_continue=False

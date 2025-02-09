print ("Hello User ")
name = input ( "plese your name :"+" ")
def classe_calculator ( number_X , aperator, number_y ):
    if aperator == "+":
       return float (number_X) + float (number_y)
    elif aperator == '-':
        return float (number_X ) -  float(number_y)
    elif aperator == '/':
        return float (number_X) / float (number_X)
    else:
        aperator == "*"
        return float (number_X) * float (number_y)
print (classe_calculator (input ('Please '+ name.title() +' enter the first number : '),
                        input("Please "+ name.title() +" enter the aperator( +، -، *، / ): "),
                        input ("Please "+ name.title() +" enter the second number : ")))
print("We thank you "+ name.title() +" for using our application")

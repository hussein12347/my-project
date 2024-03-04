# name of the game : Subtract a square game       
# file:CS112_A1_T2_3_20230125
# purpose : This is a two-player mathematical game of strategy. It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins         
# Author : حسين خالد فهيم حامد
# ID : 20230125




#welcome message and explain the game
print("======welcome to my game======")     
print("")
print("====This is a two-player mathematical game of strategy. It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins====")
print("")

# Function to check if a number is a perfect square
def is_square(n):
    return n**0.5 % 1 == 0

flag = "red"

#input the start number
while flag=="red" :
    start_num=int(input("enter the start number : "))   

    #loop for checking if the start number has a square

    if is_square(start_num) is False :
        break
    else:
        print (" please enter a valid number  doesn't has square ")
        continue


while 1==1:        
    # Player one's turn
    if start_num>0 :
        num1=int(input("player one,  please enter the number: "))   #input the number for player one
        if num1>start_num:
            print("enter a number has a square lesser than" ,start_num)   #error message  
            continue
        if is_square(num1) is True:
            start_num1=start_num-num1
            if start_num1 <=0:
                print("player one is winner")     #message for winnig player one
                break
            print(start_num-num1)     #counter
        else:
            print("enter a valid number: ")      #error message
            continue

    # Player two's turn
    while start_num>0:
        num2=int(input("player two, please enter the number: "))   #input the number for player two
        if num2>start_num1:
            print("enter a number lesser than", start_num1)   #error message
            continue
        if is_square(num2) is True:
            print(start_num-num1-num2)  #counter
            start_num2=start_num1-num2
            start_num=start_num-num1-num2
            if start_num2 <=0:
                print("player two is winner")   #message for winning player two
                break
            break
        else:
            print("enter a valid number: ")     #error message
            continue

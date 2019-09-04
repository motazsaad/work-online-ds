def mul(x,y):
    return x * y

def write_message( name ):
    #send the message to address
    return 'Dear ' + name + ' \ please contact me as soon as possible'

def main():
    write_message()
    x = int(input("Please enter your x: "))
    y = int(input("Please enter your y: "))
    print("z = ", mul(x,y))

if __name__ == "__main__":
    main()
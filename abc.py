""" This program will verify a card number and returns TRUE is mod of 10 and False otherwise."""
def check(string):
    """ function will check card number and Retuns True if mod of 10 and False otherwise."""
    if string[4]==" " and string[9]==" " and string[14]==" ":
        add = 0
        count = 0
        for i in string:
            if 48<=ord(i)<= 57 or ord(i)==32:
                if 48 <= ord(i)<=57:
                    add+=int(i)
                    count+=1
            print(add,count)
        #return bool(count == 16)

print(check("1234 1234 1234 1234"))

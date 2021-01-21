""" This program will verify a card number and returns TRUE is mod of 10 and False otherwise."""
def check(string):
    """ function will check card number and Retuns True if mod of 10 and False otherwise."""
    if string[4]==" " and string[9]==" " and string[14]==" ":

        for i in string:
            if 48<=ord(i)<= 57 or ord(i)==32:
                continue
            else:
                return False
        add = 0
        for i in string:
            if 48 <= ord(i)<= 57:
                add+=int(i)
        return bool(add % 10 == 0 and add!=0)
    else:
        return False

print(check("1234 1234 1234 1234"))

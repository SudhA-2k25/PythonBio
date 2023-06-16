# Exception handling

class MyException(Exception):
    pass

class Bbin:
    def __init__(self, no):
        self.no = no
    
    def ValidateNo(self):
        try:
            if self.no > 100:
                raise MyException("Please enter a valid number (less than or equal to 100)")
        except MyException as e:
            print(e)
            print("\033[31m Invalid \033[0m")

# Example usage:
o = Bbin(200)
o.ValidateNo()

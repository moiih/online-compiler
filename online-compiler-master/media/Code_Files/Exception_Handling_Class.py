class Inputs:
    def get_values(self):
        self.a = int(input('Enter First Value: '))
        self.b = int(input('Enter Second Value: '))
        self.s = int(input('Enter A Value To Get Its Square: '))

'''class add(Inputs):
    def sum(self):
        return self.a + self.b + self.s

class Output(add):
    def show(self):
        print('Sum Of',self.a,',',self.b,'and',self.s,'=', self.sum())

ob = Output()

ob.get_values()
ob.sum()
ob.show()'''

class CheckError(Inputs):
    print("Checking errors")
    def divide_error(self):
        print("in div")
        if self.b == 0:
            try:
                pass
            except ZeroDivisionError as error:
                print('Hey, you cannot divide number by zero --->',error)
            except ValueError as error:
                print('Invalid Input --->',error)
            except Exception as error:
                print('Something went wrong...',error)
            return 1
        

    def type_error(self):
        print("in div")
        if str(self.a).isdigit() == False or str(self.b).isdigit() == False or str(self.s).isdigit() == False:
            try:
                pass
            except ValueError as error:
                print('Invalid Input --->',error)                
            except Exception as error:
                print('Something went wrong...',error)
            return 1 


class Logic(CheckError):
    def calculate_div(self):
        print("Logic calcu_div")
        self.flag1 = 0
        if self.divide_error() != 1 and self.type_error() != 1:
            return self.a / self.b
            self.flag1 == 1

    def calculate_sq(self):
        self.flag2 = 0
        if self.type_error() != 1:
            return self.s * self.s
            self.flag2 == 1
        

class DisplayOutput(Logic):
    def show(self):
        print("in show")
        if self.flag1 == 1:
            print(f'{self.a} divided by {self.b} is {self.calculate_div()}')

        if self.flag2 == 1:
            print(f'Square of {self.s} is {self.calculate_sq()}')


def lets_call():
    ob = DisplayOutput()

    '''ob.get_values()
    ob.type_error()
    ob.divide_error()
    ob.calculate_div()
    ob.calculate_sq()'''
    ob.show()


lets_call()






            
            







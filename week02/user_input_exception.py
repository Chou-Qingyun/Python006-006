class UserInputException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    
    def __str__(self):
        return self.errorinfo

    
userinput = 'ac'

try:
    if not userinput.isdigit():
        raise UserInputException('用户输入有误')
except UserInputException as ue:
    print(ue)
finally:
    del userinput
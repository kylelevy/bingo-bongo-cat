import inspect

class FunnyCat:
    def __init__(self):
        self.cat = """
        /\_/\\
       ( o.o )
        > ^ <
        """

    def meow(self):
        print(f"\nBingo Bongo, meow!\n\n{self.cat}")
        
    def raise_error(self, error_code):
        if not type(error_code)==str:
            error_code = str(error_code)

        raise ValueError(f"\nBingo Bongo, you have an error!\n\n{self.cat}\nError Code: {error_code}")
    
    def checkpoint(self):
        line_num = inspect.currentframe().f_back.f_lineno
        print(f"\nBingo Bongo, you have reached a checkpoint on line {line_num}!\n\n{self.cat}")

# Calling the function to demonstrate the error
if __name__ == '__main__':
    FunnyCat().checkpoint()
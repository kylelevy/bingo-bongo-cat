import inspect

class FunnyCat:
    def __init__(self):
        self.cat = """        /\_/\\
       ( o.o )
        > ^ <
        """

    def meow(self):
        FunnyCat.say(self,"Bingo Bongo, meow")
        
    def raise_error(self, error_code):
        if not type(error_code)==str:
            error_code = str(error_code)
        error_msg = FunnyCat.say(self, f"Bingo Bongo, you have an error! Error Code: {error_code}", quiet=True)
        raise ValueError(error_msg)
    
    def checkpoint(self):
        line_num = inspect.currentframe().f_back.f_lineno
        FunnyCat.say(self, f"Bingo Bongo, you have reached a checkpoint on line {line_num}!")

    def say(self, text, quiet=False):
        if '\n' in text:
            text = text.replace('\n','')
        tb_line = ""
        for char in range(len(text)):
            tb_line += "━"
        speechBubble = f"""
            ┍━━{tb_line}━━┑
            │  {text}  │
            ┕━━{tb_line}━━┙
               V"""
        if quiet == False:
            print(speechBubble)
            print(self.cat)

        return str(speechBubble+'\n'+self.cat)

# Calling the function to demonstrate the error
if __name__ == '__main__':
    FunnyCat().say("Hi Y'all!")
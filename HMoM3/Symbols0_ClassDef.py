class Symbol():
    symbol=True
    pass

class Symbol_Quantifier(Symbol):
    quantifier_symbol=True
    pass

class Symbol_Quantifier_EXIST(Symbol_Quantifier):
    exist_quantifier_symbol=True
    def __init__(self,name_symb='',name_engl='exist'):
        self.name_symb=name_symb
        self.name_engl=name_engl
        
    def appear_symb(self,name_symb):
        print(name_symb, end=" ")
        
class Symbol_Quantifier_FORALL(Symbol_Quantifier):
    forall_quantifier_symbol=True
    def __init__(self,name_symb='',name_engl='forall'):
        self.name_symb=name_symb
        self.name_engl=name_engl
        
    def appear_symb(self,name_symb):
        print(name_symb, end=" ")


class Symbol_Parenthesys(Symbol):
    parenthesys_symbol=True
    pass

class Symbol_Parenthesys_Open(Symbol_Parenthesys):
    open_parenthesys_symbol=True
    def appear():
        print('(')

class Symbol_Parenthesys_Closed(Symbol_Parenthesys):
    closed_parenthesys_symbol=True
    def appear():
        print(')')
           
class Symbol_Logic(Symbol):
    logic_symbol=True
    pass


class Symbol_Logic_Unary(Symbol_Logic):
    unary_logic_symbol=True
    def __init__(self,name_symb,name_engl,truth_table,arg_num=1):
        self.name_symb=name_symb
        self.name_engl=name_engl
        self.arg_num=arg_num
        self.truth_table=truth_table
        
    def appear_symb(self,name_symb):
        print(name_symb, end=" ")
    def appear_engl(self,name_symb,name_engl):
        print(name_engl, end=' ')
        
class Symbol_Logic_Binary(Symbol_Logic):
    binary_logic_symbol=True
    def __init__(self,name_symb,name_engl,truth_table,arg_num=2):
        self.name_symb=name_symb
        self.name_engl=name_engl
        self.arg_num=arg_num
        self.truth_table=truth_table
        
    def appear_symb(self,name_symb):
        print(name_symb, end=" ")
    def appear_engl(self,name_symb,name_engl):
        print(name_engl, end=' ')
        

class Symbol_LogicConstant(Symbol):
    logicConstant_symbol=True
    def __init__(self,name,truthValue):
        self.name=name
        self.truthValue=truthValue
    def appear(self,name,truthValue):
        print(f'({self.name},{self.truthValue})')
        


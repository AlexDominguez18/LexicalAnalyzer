import states

class LexicalAnalyzer():

    def __init__(self):
        self.__state = states.INITIAL_STATE
        self.__results = []
    
    def analyze(self, text):
        text = text + '$'
        #Starting to analyze
        i = 0
        while (i <= (len(text) - 1) and self.__state == states.INITIAL):
            lexeme = ''
            token = 'Error'
            while (i <= (len(text) - 1) and self.__state != states.ESCAPE):
                #In the initial state
                if self.__state == states.INITIAL:
                    if text[i].isspace():
                        self.__state = states.INITIAL
                    elif text[i].isalpha() or text[i] == '_':
                        self.__state = states.ID
                        lexeme += text[i]
                        token = 'id'
                    elif text[i].isnumeric():
                        self.__state = states.CONSTANT
                        lexeme += text[i]
                        token = 'constante'
                    elif text[i] == ';':
                        self.__state = states.SEMICOLON
                        lexeme += text[i]
                        token = 'punto y coma'
                    elif text[i] == ',':
                        self.__state = states.COMMA
                        lexeme += text[i]
                        token = 'coma'
                    elif text[i] == '(':
                        self.__state = states.LEFT_PARENTHESIS
                        lexeme += text[i]
                        token = 'parentesis izquierdo'
                    elif text[i] == ')':
                        self.__state = states.RIGHT_PARENTHESIS
                        lexeme += text[i]
                        token = 'parentesis derecho'
                    elif text[i] == '{':
                        self.__state = states.LEFT_BRACKET
                        lexeme += text[i]
                        token = 'llave izquierda'
                    elif text[i] == '}':
                        self.__state = states.RIGHT_BRACKET
                        lexeme += text[i]
                        token = 'llave derecha'
                    elif text[i] == '+' or text[i] == '-':
                        self.__state = states.ADD_OR_SUB
                        lexeme += text[i]
                        token = 'operador suma'
                    elif text[i] == '|':
                        self.__state = states.PIPE
                        lexeme += text[i]
                    elif text[i] == '&':
                        self.__state = states.ANDPERSAND
                        lexeme += text[i]
                    elif text[i] == '*' or text[i] == '/':
                        self.__state = states.MUL_OR_DIV
                        lexeme += text[i]
                        token = 'operador multiplicacion'
                    elif text[i] == '=':
                        self.__state = states.ASSIGN_OPERATOR
                        lexeme += text[i]
                        token = 'asignacion'
                    elif text[i] == '>' or text[i] == '<' or text[i] == '!':
                        self.__state = states.RELATIONAL_OPERATOR
                        lexeme += text[i]
                        token = 'operador relacional'
                    elif text[i] == '$':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'pesos'
                    else:
                        self.__state = states.ERROR
                        lexeme += text[i]
                        token = 'error'
__author__ = 'ErinV'

from ply import lex
import sys

#token names
tokens = (
    "ID",
    "BINARY_LITERAL",
    "A",
    "S",
    "M",
    "D",
    "EQUALS",
    "OPEN_PAREN",
    "CLOSE_PAREN",
    "WHITESPACE",
    "COMMENT"
)

#rules, following convetion demonstrated in 4.1 here http://www.dabeaz.com/ply/ply.html
t_ID = r"([a-z]|_)([a-z]|_|\d)*"
t_BINARY_LITERAL = r"(\+|-)?([10])+"
t_A = r"A"
t_S = r"S"
t_M = r"M"
t_D = r"D"
t_EQUALS = r"="
t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"
#TODO: ask about nonprintable characters
#t_WHITESPACE = r"(\ |\r|\t|\n|\a|\b|\cx|\C-x|\e|\f|\M-C-x|\d|\nnn|\s|\v|\x|\xnn)
t_WHITESPACE = r"(\ |\r|\t|\n)+"
t_COMMENT = r"(\/\/.*)|(\/\*(.)*?\*\/)|(\/\*(.|\n)*?\*\/)"

def t_error(t):
    """
    Log an error if we come across something unexpected. Won't write to the file, but will print to console.
    """
    print("Illegal character '%s'" % t.value[0])
    #don't skip, PLY docs and examples are not always your friend...

#second argument passed to the command line is the name of the file from which input is to be read
file_name = sys.argv[1]

def main():
    """
    Function to work through a file, checking if any of the expected tokens are in the file
    """
    lex.lex()
    lex.input(open(file_name, 'r').read())

if __name__ == '__main__':
    main()
    #make the .tkn file
    base_name = file_name.split(".")[0].strip()
    o_file_name = base_name+".tkn"
    open(o_file_name, 'w').close()#apperently this is supposed to work...
    output_file = open(o_file_name, 'a')
    lex_by_type = ["A", "S", "M", "D", "WHITESPACE", "COMMENT"]
    lex_by_value = ["EQUALS", "OPEN_PAREN", "CLOSE_PAREN"]
    for token in iter(lex.token, None):
        if token.type in lex_by_type:
            output_file.write(token.type + "\n")
        elif token.type in lex_by_value:
            output_file.write(token.value + "\n")
        else:
            output_file.write(token.type + "," + token.value + "\n")

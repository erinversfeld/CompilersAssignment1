__author__ = 'ErinV'

from ply import lex
import sys

#token names
tokens = {
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
}

#rules
t_ID = r"([a-z]|_)([a-z]|_|\d)*"
t_BINARY_LITERAL = r"(\+|-)?([10])+"
t_A = r"A"
t_S = r"S"
t_M = r"M"
t_D = r"D"
t_EQUALS = r"="
t_OPEN_PAREN = r"("
t_CLOSE_PAREN = r")"
t_WHITESPACE = r"(\ |\t|\n|\r)+"
t_COMMENT = r"(\/\/.*)|()\/\*(.)*?\*\/)|(\/\*(.|\n)*?\*\/)"

#second argument passed to the command line is the name of the file from which input is to be read
file_name = sys.argv[1]

def main():
    lex.lex()
    lex.input(open(file_name, 'r').read())

if __name__ == '__main__':
    main()
    #make the .tkn file
    base_name = file_name.split(".")[0].strip()
    o_file_name = base_name+".tkn"

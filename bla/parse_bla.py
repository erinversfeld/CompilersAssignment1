__author__ = 'ErinV'

from ..ply import yacc, lex
import sys
from ..bla import lex_bla

#conditional lexing stuff, generate tokens
lex_bla.t_ignore_WHITESPACE = lex_bla.t_WHITESPACE
lex_bla.t_ignore_COMMENT = lex_bla.t_COMMENT
lex_bla.main()

from ..bla.lex_bla import tokens

def p_expression_plus(p):
    'expression : expression A term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression S term'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : term M factor'
    p[0] = p[1] * p[3]

def p_expression_div(p):
    'expression : term D factor'
    p[0] = p[1] / p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term: factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : BINARY_LITERAL'
    p[0] = p[1]

def p_factor_expr(p):
    'factor: OPEN_PAREN expression CLOSE_PAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

#second argument to the CL is the name of the file to parse
input_file_name = sys.argv[1]
base_file_name = input_file_name.split(".")[0].strip()
output_file_name = base_file_name+".ast"

#parser
p = yacc.yacc()

output_file = open(output_file_name, 'a')
result = p.parse(open(input_file_name, 'r').read())
output_file.write('Program\n')
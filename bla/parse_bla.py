__author__ = 'ErinV'

from ply import yacc, lex
import sys
import lex_bla

#conditional lexing stuff, generate tokens
lex_bla.t_WHITESPACE = r"$a"
lex_bla.t_COMMENT = r"$a"
lex_bla.t_ignore_WHITESPACE = r"(\ |\r|\t|\n)+"
lex_bla.t_ignore_COMMENT = r"(\/\/.*)|(\/\*(.)*?\*\/)|(\/\*(.|\n)*?\*\/)"
lex_bla.main()

from lex_bla import tokens #stuff breaks without this according to 6.1 here http://www.dabeaz.com/ply/ply.html

#second argument to the CL is the name of the file to parse
input_file_name = sys.argv[1]
base_file_name = input_file_name.split(".")[0].strip()
output_file_name = base_file_name+".ast"

def p_program(p):
    '''program : program statement
			   | empty'''
    p[0] = []
    for i in range(1, len(p)):
        if p[i]:
            p[0].append(p[i])
    p[0] = list(p[0])

def p_empty(p):
    'empty :'
    pass

def p_whitespace(p):
    'statement : WHITESPACE'
    p[0] = ""

def p_comment(p):
    'statement : COMMENT'
    p[0] = ""

def p_statement(p):
    'statement : ID EQUALS expression'
    p[0] = [p[2],"ID,"+p[1], p[3]]

def p_expression_plus(p):
    'expression : expression A term'
    p[0] = [p[2], p[1], p[3]]

def p_expression_minus(p):
    'expression : expression S term'
    p[0] = [p[2], p[1], p[3]]

def p_expression_times(p):
    'expression : term M factor'
    p[0] = [p[2], p[1], p[3]]

def p_expression_div(p):
    'expression : term D factor'
    p[0] = [p[2], p[1], p[3]]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : BINARY_LITERAL'
    p[0] = "BINARY_LITERAL,"+p[1]

def p_factor_expr(p):
    'factor : OPEN_PAREN expression CLOSE_PAREN'
    p[0] = p[2]

def p_factor_id(p):
    'factor : ID'
    p[0] = "ID,"+p[1]

def p_error(p):
    print("Syntax error in input!")

def populate_output_file(output_list, depth):
    """

    :param output_list: the list of nodes
    :param depth: The depth of the node
    :return: exit code 0 if executed without error. Non zero exit code otherwise.
    """
    #the example in section 6.10 here: http://www.dabeaz.com/ply/ply.html uses tuples, but I like lists
    for entry in output_list:
        if isinstance(entry, list):
            if isinstance(entry[0], list):
                populate_output_file(entry[0:], depth)
            else:
                output_file.write('\t'*depth+entry[0]+'\n')
                populate_output_file(entry[1:], depth+1)
        else:
            output_file.write('\t'*depth+entry+'\n')

#parser
p = yacc.yacc()

open(output_file_name, 'w').close()#apparently this works?
output_file = open(output_file_name, 'a')
output = p.parse(open(input_file_name, 'r').read())
output_file.write('Program\n') #root node is always program, therefore we can just write it in straight away
populate_output_file(output, 1) #already written the root node, therefore start one level down

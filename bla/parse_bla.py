__author__ = 'ErinV'

from ..ply import yacc, lex
import sys
from ..bla import lex_bla

#second argument to the CL is the name of the file to parse
input_file_name = sys.argv[1]
base_file_name = input_file_name.split(".")[0].strip()
output_file_name = base_file_name+".ast"

p = yacc.yacc()

output_file = open(output_file_name, 'a')
result = p.parse(open(input_file_name, 'r').read())
output_file.write('Program\n')
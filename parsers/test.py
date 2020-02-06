import antlr3
from css21Lexer import css21Lexer as Lexer
from css21Parser import css21Parser as Parser
 
input = '''
p {
  font-family: Garamond, serif;
}
h2 {
  font-size: 110%;
  color: red;
  background: white;
}
.note {
  color: red;
  background: yellow;
  font-weight: bold;
}
p#paragraph1 {
  margin: 0;
}
a:hover {
  text-decoration: none;
}
#news p {
  color: blue;
}
'''
char_stream = antlr3.ANTLRStringStream(input)
# or to parse a file:
#char_stream = antlr3.ANTLRFileStream("test.css")
# or to parse an opened file or any other file-like object:
# char_stream = antlr3.ANTLRInputStream(file)
 
lexer = Lexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = Parser(tokens)
parser.styleSheet()

# $ANTLR 3.0.1 css21.g 2012-02-12 13:48:56

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
STAR=23
LBRACE=11
EOF=-1
MEDIA_SYM=10
LPAREN=28
LENGTH=33
IMPORTANT_SYM=30
LBRACKET=22
INCLUDES=25
TIME=37
RPAREN=29
NAME=45
GREATER=18
ESCAPE=42
COMMA=9
IDENT=13
DIMENSION=78
PLUS=17
FREQ=38
NL=79
RBRACKET=27
COMMENT=73
DOT=21
D=50
CHARSET_SYM=4
E=51
F=52
G=53
A=47
B=48
RBRACE=12
ANGLE=36
C=49
L=58
M=59
NMCHAR=44
IMPORT_SYM=7
N=60
O=61
H=54
I=55
J=56
K=57
NUMBER=31
U=67
HASH=20
HEXCHAR=39
T=66
W=69
V=68
Q=63
P=62
S=65
CDO=74
R=64
MINUS=19
SOLIDUS=16
SEMI=6
INVALID=76
CDC=75
Y=71
URL=46
PERCENTAGE=32
UNICODE=41
X=70
Z=72
URI=8
COLON=15
PAGE_SYM=14
WS=77
NMSTART=43
DASHMATCH=26
OPEQ=24
EMS=34
EXS=35
NONASCII=40
STRING=5

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "CHARSET_SYM", "STRING", "SEMI", "IMPORT_SYM", "URI", "COMMA", "MEDIA_SYM", 
    "LBRACE", "RBRACE", "IDENT", "PAGE_SYM", "COLON", "SOLIDUS", "PLUS", 
    "GREATER", "MINUS", "HASH", "DOT", "LBRACKET", "STAR", "OPEQ", "INCLUDES", 
    "DASHMATCH", "RBRACKET", "LPAREN", "RPAREN", "IMPORTANT_SYM", "NUMBER", 
    "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", "HEXCHAR", 
    "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", "URL", 
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", 
    "CDO", "CDC", "INVALID", "WS", "DIMENSION", "NL"
]



class css21Parser(Parser):
    grammarFileName = "css21.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)
        self.ruleMemo = {}



                




    # $ANTLR start styleSheet
    # css21.g:31:1: styleSheet : charSet ( imports )* bodylist EOF ;
    def styleSheet(self, ):

        try:
            try:
                # css21.g:32:5: ( charSet ( imports )* bodylist EOF )
                # css21.g:32:9: charSet ( imports )* bodylist EOF
                self.following.append(self.FOLLOW_charSet_in_styleSheet53)
                self.charSet()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:33:9: ( imports )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IMPORT_SYM) :
                        alt1 = 1


                    if alt1 == 1:
                        # css21.g:33:9: imports
                        self.following.append(self.FOLLOW_imports_in_styleSheet63)
                        self.imports()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_bodylist_in_styleSheet74)
                self.bodylist()
                self.following.pop()
                if self.failed:
                    return 
                self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet81)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end styleSheet


    # $ANTLR start charSet
    # css21.g:41:1: charSet : ( CHARSET_SYM STRING SEMI | );
    def charSet(self, ):

        try:
            try:
                # css21.g:42:5: ( CHARSET_SYM STRING SEMI | )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CHARSET_SYM) :
                    alt2 = 1
                elif (LA2_0 == EOF or LA2_0 == IMPORT_SYM or LA2_0 == MEDIA_SYM or (IDENT <= LA2_0 <= COLON) or (HASH <= LA2_0 <= STAR)) :
                    alt2 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("41:1: charSet : ( CHARSET_SYM STRING SEMI | );", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # css21.g:42:9: CHARSET_SYM STRING SEMI
                    self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet107)
                    if self.failed:
                        return 
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet109)
                    if self.failed:
                        return 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet111)
                    if self.failed:
                        return 


                elif alt2 == 2:
                    # css21.g:44:5: 
                    pass


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end charSet


    # $ANTLR start imports
    # css21.g:49:1: imports : IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI ;
    def imports(self, ):

        try:
            try:
                # css21.g:50:5: ( IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI )
                # css21.g:50:9: IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports139)
                if self.failed:
                    return 
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_imports141
                        )
                    raise mse


                # css21.g:50:33: ( medium ( COMMA medium )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # css21.g:50:34: medium ( COMMA medium )*
                    self.following.append(self.FOLLOW_medium_in_imports148)
                    self.medium()
                    self.following.pop()
                    if self.failed:
                        return 
                    # css21.g:50:41: ( COMMA medium )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # css21.g:50:42: COMMA medium
                            self.match(self.input, COMMA, self.FOLLOW_COMMA_in_imports151)
                            if self.failed:
                                return 
                            self.following.append(self.FOLLOW_medium_in_imports153)
                            self.medium()
                            self.following.pop()
                            if self.failed:
                                return 


                        else:
                            break #loop3





                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports159)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end imports


    # $ANTLR start media
    # css21.g:57:1: media : MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE ;
    def media(self, ):

        try:
            try:
                # css21.g:58:5: ( MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE )
                # css21.g:58:7: MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media180)
                if self.failed:
                    return 
                self.following.append(self.FOLLOW_medium_in_media182)
                self.medium()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:58:24: ( COMMA medium )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # css21.g:58:25: COMMA medium
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media185)
                        if self.failed:
                            return 
                        self.following.append(self.FOLLOW_medium_in_media187)
                        self.medium()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop5


                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media199)
                if self.failed:
                    return 
                self.following.append(self.FOLLOW_ruleSet_in_media213)
                self.ruleSet()
                self.following.pop()
                if self.failed:
                    return 
                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media223)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end media


    # $ANTLR start medium
    # css21.g:67:1: medium : IDENT ;
    def medium(self, ):

        try:
            try:
                # css21.g:68:5: ( IDENT )
                # css21.g:68:7: IDENT
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_medium243)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end medium


    # $ANTLR start bodylist
    # css21.g:72:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        try:
            try:
                # css21.g:73:5: ( ( bodyset )* )
                # css21.g:73:7: ( bodyset )*
                # css21.g:73:7: ( bodyset )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == MEDIA_SYM or (IDENT <= LA6_0 <= COLON) or (HASH <= LA6_0 <= STAR)) :
                        alt6 = 1


                    if alt6 == 1:
                        # css21.g:73:7: bodyset
                        self.following.append(self.FOLLOW_bodyset_in_bodylist266)
                        self.bodyset()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop6






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end bodylist


    # $ANTLR start bodyset
    # css21.g:76:1: bodyset : ( ruleSet | media | page );
    def bodyset(self, ):

        try:
            try:
                # css21.g:77:5: ( ruleSet | media | page )
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == IDENT or LA7 == COLON or LA7 == HASH or LA7 == DOT or LA7 == LBRACKET or LA7 == STAR:
                    alt7 = 1
                elif LA7 == MEDIA_SYM:
                    alt7 = 2
                elif LA7 == PAGE_SYM:
                    alt7 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("76:1: bodyset : ( ruleSet | media | page );", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # css21.g:77:7: ruleSet
                    self.following.append(self.FOLLOW_ruleSet_in_bodyset288)
                    self.ruleSet()
                    self.following.pop()
                    if self.failed:
                        return 


                elif alt7 == 2:
                    # css21.g:78:7: media
                    self.following.append(self.FOLLOW_media_in_bodyset296)
                    self.media()
                    self.following.pop()
                    if self.failed:
                        return 


                elif alt7 == 3:
                    # css21.g:79:7: page
                    self.following.append(self.FOLLOW_page_in_bodyset304)
                    self.page()
                    self.following.pop()
                    if self.failed:
                        return 



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end bodyset


    # $ANTLR start page
    # css21.g:82:1: page : PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE ;
    def page(self, ):

        try:
            try:
                # css21.g:83:5: ( PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE )
                # css21.g:83:7: PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE
                self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page328)
                if self.failed:
                    return 
                # css21.g:83:16: ( pseudoPage )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == COLON) :
                    alt8 = 1
                if alt8 == 1:
                    # css21.g:83:16: pseudoPage
                    self.following.append(self.FOLLOW_pseudoPage_in_page330)
                    self.pseudoPage()
                    self.following.pop()
                    if self.failed:
                        return 



                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page341)
                if self.failed:
                    return 
                self.following.append(self.FOLLOW_declaration_in_page355)
                self.declaration()
                self.following.pop()
                if self.failed:
                    return 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_page357)
                if self.failed:
                    return 
                # css21.g:85:30: ( declaration SEMI )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        alt9 = 1


                    if alt9 == 1:
                        # css21.g:85:31: declaration SEMI
                        self.following.append(self.FOLLOW_declaration_in_page360)
                        self.declaration()
                        self.following.pop()
                        if self.failed:
                            return 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_page362)
                        if self.failed:
                            return 


                    else:
                        break #loop9


                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page374)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end page


    # $ANTLR start pseudoPage
    # css21.g:89:1: pseudoPage : COLON IDENT ;
    def pseudoPage(self, ):

        try:
            try:
                # css21.g:90:5: ( COLON IDENT )
                # css21.g:90:7: COLON IDENT
                self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage395)
                if self.failed:
                    return 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage397)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end pseudoPage


    # $ANTLR start operator
    # css21.g:93:1: operator : ( SOLIDUS | COMMA | );
    def operator(self, ):

        try:
            try:
                # css21.g:94:5: ( SOLIDUS | COMMA | )
                alt10 = 3
                LA10 = self.input.LA(1)
                if LA10 == SOLIDUS:
                    alt10 = 1
                elif LA10 == COMMA:
                    alt10 = 2
                elif LA10 == STRING or LA10 == URI or LA10 == IDENT or LA10 == PLUS or LA10 == MINUS or LA10 == HASH or LA10 == NUMBER or LA10 == PERCENTAGE or LA10 == LENGTH or LA10 == EMS or LA10 == EXS or LA10 == ANGLE or LA10 == TIME or LA10 == FREQ:
                    alt10 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("93:1: operator : ( SOLIDUS | COMMA | );", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # css21.g:94:7: SOLIDUS
                    self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator418)
                    if self.failed:
                        return 


                elif alt10 == 2:
                    # css21.g:95:7: COMMA
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator426)
                    if self.failed:
                        return 


                elif alt10 == 3:
                    # css21.g:97:5: 
                    pass


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end operator


    # $ANTLR start combinator
    # css21.g:99:1: combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        try:
            try:
                # css21.g:100:5: ( PLUS | GREATER | )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == PLUS:
                    alt11 = 1
                elif LA11 == GREATER:
                    alt11 = 2
                elif LA11 == IDENT or LA11 == COLON or LA11 == HASH or LA11 == DOT or LA11 == LBRACKET or LA11 == STAR:
                    alt11 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("99:1: combinator : ( PLUS | GREATER | );", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # css21.g:100:7: PLUS
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator453)
                    if self.failed:
                        return 


                elif alt11 == 2:
                    # css21.g:101:7: GREATER
                    self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator461)
                    if self.failed:
                        return 


                elif alt11 == 3:
                    # css21.g:103:5: 
                    pass


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end combinator


    # $ANTLR start unaryOperator
    # css21.g:105:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        try:
            try:
                # css21.g:106:5: ( MINUS | PLUS )
                # css21.g:
                if self.input.LA(1) == PLUS or self.input.LA(1) == MINUS:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_unaryOperator0
                        )
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end unaryOperator


    # $ANTLR start property
    # css21.g:110:1: property : IDENT ;
    def property(self, ):

        try:
            try:
                # css21.g:111:5: ( IDENT )
                # css21.g:111:7: IDENT
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property519)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end property


    # $ANTLR start ruleSet
    # css21.g:114:1: ruleSet : selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE ;
    def ruleSet(self, ):

        try:
            try:
                # css21.g:115:5: ( selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE )
                # css21.g:115:7: selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE
                self.following.append(self.FOLLOW_selector_in_ruleSet540)
                self.selector()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:115:16: ( COMMA selector )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == COMMA) :
                        alt12 = 1


                    if alt12 == 1:
                        # css21.g:115:17: COMMA selector
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet543)
                        if self.failed:
                            return 
                        self.following.append(self.FOLLOW_selector_in_ruleSet545)
                        self.selector()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop12


                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet557)
                if self.failed:
                    return 
                self.following.append(self.FOLLOW_declaration_in_ruleSet571)
                self.declaration()
                self.following.pop()
                if self.failed:
                    return 
                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_ruleSet573)
                if self.failed:
                    return 
                # css21.g:117:30: ( declaration SEMI )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == IDENT) :
                        alt13 = 1


                    if alt13 == 1:
                        # css21.g:117:31: declaration SEMI
                        self.following.append(self.FOLLOW_declaration_in_ruleSet576)
                        self.declaration()
                        self.following.pop()
                        if self.failed:
                            return 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_ruleSet578)
                        if self.failed:
                            return 


                    else:
                        break #loop13


                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet590)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end ruleSet


    # $ANTLR start selector
    # css21.g:121:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        try:
            try:
                # css21.g:122:5: ( simpleSelector ( combinator simpleSelector )* )
                # css21.g:122:7: simpleSelector ( combinator simpleSelector )*
                self.following.append(self.FOLLOW_simpleSelector_in_selector611)
                self.simpleSelector()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:122:22: ( combinator simpleSelector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == IDENT or LA14_0 == COLON or (PLUS <= LA14_0 <= GREATER) or (HASH <= LA14_0 <= STAR)) :
                        alt14 = 1


                    if alt14 == 1:
                        # css21.g:122:23: combinator simpleSelector
                        self.following.append(self.FOLLOW_combinator_in_selector614)
                        self.combinator()
                        self.following.pop()
                        if self.failed:
                            return 
                        self.following.append(self.FOLLOW_simpleSelector_in_selector616)
                        self.simpleSelector()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop14






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end selector


    # $ANTLR start simpleSelector
    # css21.g:125:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        try:
            try:
                # css21.g:126:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == IDENT or LA17_0 == STAR) :
                    alt17 = 1
                elif (LA17_0 == COLON or (HASH <= LA17_0 <= LBRACKET)) :
                    alt17 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("125:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # css21.g:126:7: elementName ( ( esPred )=> elementSubsequent )*
                    self.following.append(self.FOLLOW_elementName_in_simpleSelector635)
                    self.elementName()
                    self.following.pop()
                    if self.failed:
                        return 
                    # css21.g:127:9: ( ( esPred )=> elementSubsequent )*
                    while True: #loop15
                        alt15 = 2
                        LA15 = self.input.LA(1)
                        if LA15 == HASH:
                            LA15_2 = self.input.LA(2)

                            if (self.synpred1()) :
                                alt15 = 1


                        elif LA15 == DOT:
                            LA15_3 = self.input.LA(2)

                            if (LA15_3 == IDENT) :
                                LA15_7 = self.input.LA(3)

                                if (self.synpred1()) :
                                    alt15 = 1




                        elif LA15 == LBRACKET:
                            LA15_4 = self.input.LA(2)

                            if (LA15_4 == IDENT) :
                                LA15_8 = self.input.LA(3)

                                if ((OPEQ <= LA15_8 <= DASHMATCH)) :
                                    LA15_10 = self.input.LA(4)

                                    if (LA15_10 == STRING or LA15_10 == IDENT) :
                                        LA15_12 = self.input.LA(5)

                                        if (LA15_12 == RBRACKET) :
                                            LA15_11 = self.input.LA(6)

                                            if (self.synpred1()) :
                                                alt15 = 1






                                elif (LA15_8 == RBRACKET) :
                                    LA15_11 = self.input.LA(4)

                                    if (self.synpred1()) :
                                        alt15 = 1






                        elif LA15 == COLON:
                            LA15_5 = self.input.LA(2)

                            if (LA15_5 == IDENT) :
                                LA15_9 = self.input.LA(3)

                                if (self.synpred1()) :
                                    alt15 = 1





                        if alt15 == 1:
                            # css21.g:127:10: ( esPred )=> elementSubsequent
                            self.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector651)
                            self.elementSubsequent()
                            self.following.pop()
                            if self.failed:
                                return 


                        else:
                            break #loop15




                elif alt17 == 2:
                    # css21.g:129:7: ( ( esPred )=> elementSubsequent )+
                    # css21.g:129:7: ( ( esPred )=> elementSubsequent )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16 = self.input.LA(1)
                        if LA16 == HASH:
                            LA16_2 = self.input.LA(2)

                            if (self.synpred2()) :
                                alt16 = 1


                        elif LA16 == DOT:
                            LA16_3 = self.input.LA(2)

                            if (self.synpred2()) :
                                alt16 = 1


                        elif LA16 == LBRACKET:
                            LA16_4 = self.input.LA(2)

                            if (self.synpred2()) :
                                alt16 = 1


                        elif LA16 == COLON:
                            LA16_5 = self.input.LA(2)

                            if (self.synpred2()) :
                                alt16 = 1



                        if alt16 == 1:
                            # css21.g:129:8: ( esPred )=> elementSubsequent
                            self.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector675)
                            self.elementSubsequent()
                            self.following.pop()
                            if self.failed:
                                return 


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            if self.backtracking > 0:
                                self.failed = True
                                return 

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end simpleSelector


    # $ANTLR start esPred
    # css21.g:132:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        try:
            try:
                # css21.g:133:5: ( HASH | DOT | LBRACKET | COLON )
                # css21.g:
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_esPred0
                        )
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end esPred


    # $ANTLR start elementSubsequent
    # css21.g:136:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        try:
            try:
                # css21.g:137:5: ( HASH | cssClass | attrib | pseudo )
                alt18 = 4
                LA18 = self.input.LA(1)
                if LA18 == HASH:
                    alt18 = 1
                elif LA18 == DOT:
                    alt18 = 2
                elif LA18 == LBRACKET:
                    alt18 = 3
                elif LA18 == COLON:
                    alt18 = 4
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("136:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # css21.g:137:7: HASH
                    self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent731)
                    if self.failed:
                        return 


                elif alt18 == 2:
                    # css21.g:138:7: cssClass
                    self.following.append(self.FOLLOW_cssClass_in_elementSubsequent739)
                    self.cssClass()
                    self.following.pop()
                    if self.failed:
                        return 


                elif alt18 == 3:
                    # css21.g:139:7: attrib
                    self.following.append(self.FOLLOW_attrib_in_elementSubsequent747)
                    self.attrib()
                    self.following.pop()
                    if self.failed:
                        return 


                elif alt18 == 4:
                    # css21.g:140:7: pseudo
                    self.following.append(self.FOLLOW_pseudo_in_elementSubsequent755)
                    self.pseudo()
                    self.following.pop()
                    if self.failed:
                        return 



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end elementSubsequent


    # $ANTLR start cssClass
    # css21.g:143:1: cssClass : DOT IDENT ;
    def cssClass(self, ):

        try:
            try:
                # css21.g:144:5: ( DOT IDENT )
                # css21.g:144:7: DOT IDENT
                self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass776)
                if self.failed:
                    return 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass778)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end cssClass


    # $ANTLR start elementName
    # css21.g:147:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        try:
            try:
                # css21.g:148:5: ( IDENT | STAR )
                # css21.g:
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_elementName0
                        )
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end elementName


    # $ANTLR start attrib
    # css21.g:152:1: attrib : LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET ;
    def attrib(self, ):

        try:
            try:
                # css21.g:153:5: ( LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET )
                # css21.g:153:7: LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib828)
                if self.failed:
                    return 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attrib843)
                if self.failed:
                    return 
                # css21.g:157:13: ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((OPEQ <= LA19_0 <= DASHMATCH)) :
                    alt19 = 1
                if alt19 == 1:
                    # css21.g:158:17: ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume();
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return 

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_attrib884
                            )
                        raise mse


                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume();
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return 

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_attrib992
                            )
                        raise mse





                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1093)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end attrib


    # $ANTLR start pseudo
    # css21.g:172:1: pseudo : COLON IDENT ( LPAREN ( IDENT )? RPAREN )? ;
    def pseudo(self, ):

        try:
            try:
                # css21.g:173:5: ( COLON IDENT ( LPAREN ( IDENT )? RPAREN )? )
                # css21.g:173:7: COLON IDENT ( LPAREN ( IDENT )? RPAREN )?
                self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1106)
                if self.failed:
                    return 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1121)
                if self.failed:
                    return 
                # css21.g:175:17: ( LPAREN ( IDENT )? RPAREN )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == LPAREN) :
                    alt21 = 1
                if alt21 == 1:
                    # css21.g:177:21: LPAREN ( IDENT )? RPAREN
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_pseudo1179)
                    if self.failed:
                        return 
                    # css21.g:177:28: ( IDENT )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == IDENT) :
                        alt20 = 1
                    if alt20 == 1:
                        # css21.g:177:28: IDENT
                        self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1181)
                        if self.failed:
                            return 



                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1184)
                    if self.failed:
                        return 







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end pseudo


    # $ANTLR start declaration
    # css21.g:181:1: declaration : property COLON expr ( prio )? ;
    def declaration(self, ):

        try:
            try:
                # css21.g:182:5: ( property COLON expr ( prio )? )
                # css21.g:182:7: property COLON expr ( prio )?
                self.following.append(self.FOLLOW_property_in_declaration1220)
                self.property()
                self.following.pop()
                if self.failed:
                    return 
                self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1222)
                if self.failed:
                    return 
                self.following.append(self.FOLLOW_expr_in_declaration1224)
                self.expr()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:182:27: ( prio )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IMPORTANT_SYM) :
                    alt22 = 1
                if alt22 == 1:
                    # css21.g:182:27: prio
                    self.following.append(self.FOLLOW_prio_in_declaration1226)
                    self.prio()
                    self.following.pop()
                    if self.failed:
                        return 







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end declaration


    # $ANTLR start prio
    # css21.g:185:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        try:
            try:
                # css21.g:186:5: ( IMPORTANT_SYM )
                # css21.g:186:7: IMPORTANT_SYM
                self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1248)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end prio


    # $ANTLR start expr
    # css21.g:189:1: expr : term ( operator term )* ;
    def expr(self, ):

        try:
            try:
                # css21.g:190:5: ( term ( operator term )* )
                # css21.g:190:7: term ( operator term )*
                self.following.append(self.FOLLOW_term_in_expr1269)
                self.term()
                self.following.pop()
                if self.failed:
                    return 
                # css21.g:190:12: ( operator term )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == STRING or (URI <= LA23_0 <= COMMA) or LA23_0 == IDENT or (SOLIDUS <= LA23_0 <= PLUS) or (MINUS <= LA23_0 <= HASH) or (NUMBER <= LA23_0 <= FREQ)) :
                        alt23 = 1


                    if alt23 == 1:
                        # css21.g:190:13: operator term
                        self.following.append(self.FOLLOW_operator_in_expr1272)
                        self.operator()
                        self.following.pop()
                        if self.failed:
                            return 
                        self.following.append(self.FOLLOW_term_in_expr1274)
                        self.term()
                        self.following.pop()
                        if self.failed:
                            return 


                    else:
                        break #loop23






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end expr


    # $ANTLR start term
    # css21.g:193:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT ( LPAREN expr RPAREN )? | URI | hexColor );
    def term(self, ):

        try:
            try:
                # css21.g:194:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT ( LPAREN expr RPAREN )? | URI | hexColor )
                alt26 = 5
                LA26 = self.input.LA(1)
                if LA26 == PLUS or LA26 == MINUS or LA26 == NUMBER or LA26 == PERCENTAGE or LA26 == LENGTH or LA26 == EMS or LA26 == EXS or LA26 == ANGLE or LA26 == TIME or LA26 == FREQ:
                    alt26 = 1
                elif LA26 == STRING:
                    alt26 = 2
                elif LA26 == IDENT:
                    alt26 = 3
                elif LA26 == URI:
                    alt26 = 4
                elif LA26 == HASH:
                    alt26 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return 

                    nvae = NoViableAltException("193:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT ( LPAREN expr RPAREN )? | URI | hexColor );", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # css21.g:194:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    # css21.g:194:7: ( unaryOperator )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == PLUS or LA24_0 == MINUS) :
                        alt24 = 1
                    if alt24 == 1:
                        # css21.g:194:7: unaryOperator
                        self.following.append(self.FOLLOW_unaryOperator_in_term1297)
                        self.unaryOperator()
                        self.following.pop()
                        if self.failed:
                            return 



                    if (NUMBER <= self.input.LA(1) <= FREQ):
                        self.input.consume();
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return 

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_term1308
                            )
                        raise mse




                elif alt26 == 2:
                    # css21.g:205:7: STRING
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_term1454)
                    if self.failed:
                        return 


                elif alt26 == 3:
                    # css21.g:206:7: IDENT ( LPAREN expr RPAREN )?
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1462)
                    if self.failed:
                        return 
                    # css21.g:206:13: ( LPAREN expr RPAREN )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LPAREN) :
                        alt25 = 1
                    if alt25 == 1:
                        # css21.g:207:17: LPAREN expr RPAREN
                        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_term1485)
                        if self.failed:
                            return 
                        self.following.append(self.FOLLOW_expr_in_term1487)
                        self.expr()
                        self.following.pop()
                        if self.failed:
                            return 
                        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_term1489)
                        if self.failed:
                            return 





                elif alt26 == 4:
                    # css21.g:209:7: URI
                    self.match(self.input, URI, self.FOLLOW_URI_in_term1512)
                    if self.failed:
                        return 


                elif alt26 == 5:
                    # css21.g:210:7: hexColor
                    self.following.append(self.FOLLOW_hexColor_in_term1520)
                    self.hexColor()
                    self.following.pop()
                    if self.failed:
                        return 



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end term


    # $ANTLR start hexColor
    # css21.g:213:1: hexColor : HASH ;
    def hexColor(self, ):

        try:
            try:
                # css21.g:214:5: ( HASH )
                # css21.g:214:7: HASH
                self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1541)
                if self.failed:
                    return 




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end hexColor

    # $ANTLR start synpred1
    def synpred1_fragment(self, ):
        # css21.g:127:10: ( esPred )
        # css21.g:127:11: esPred
        self.following.append(self.FOLLOW_esPred_in_synpred1648)
        self.esPred()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred1



    # $ANTLR start synpred2
    def synpred2_fragment(self, ):
        # css21.g:129:8: ( esPred )
        # css21.g:129:9: esPred
        self.following.append(self.FOLLOW_esPred_in_synpred2672)
        self.esPred()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred2



    def synpred1(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred1_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred2(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred2_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success



 

    FOLLOW_charSet_in_styleSheet53 = frozenset([7, 10, 13, 14, 15, 20, 21, 22, 23])
    FOLLOW_imports_in_styleSheet63 = frozenset([7, 10, 13, 14, 15, 20, 21, 22, 23])
    FOLLOW_bodylist_in_styleSheet74 = frozenset([])
    FOLLOW_EOF_in_styleSheet81 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet107 = frozenset([5])
    FOLLOW_STRING_in_charSet109 = frozenset([6])
    FOLLOW_SEMI_in_charSet111 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports139 = frozenset([5, 8])
    FOLLOW_set_in_imports141 = frozenset([6, 13])
    FOLLOW_medium_in_imports148 = frozenset([6, 9])
    FOLLOW_COMMA_in_imports151 = frozenset([13])
    FOLLOW_medium_in_imports153 = frozenset([6, 9])
    FOLLOW_SEMI_in_imports159 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media180 = frozenset([13])
    FOLLOW_medium_in_media182 = frozenset([9, 11])
    FOLLOW_COMMA_in_media185 = frozenset([13])
    FOLLOW_medium_in_media187 = frozenset([9, 11])
    FOLLOW_LBRACE_in_media199 = frozenset([13, 15, 20, 21, 22, 23])
    FOLLOW_ruleSet_in_media213 = frozenset([12])
    FOLLOW_RBRACE_in_media223 = frozenset([1])
    FOLLOW_IDENT_in_medium243 = frozenset([1])
    FOLLOW_bodyset_in_bodylist266 = frozenset([1, 10, 13, 14, 15, 20, 21, 22, 23])
    FOLLOW_ruleSet_in_bodyset288 = frozenset([1])
    FOLLOW_media_in_bodyset296 = frozenset([1])
    FOLLOW_page_in_bodyset304 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page328 = frozenset([11, 15])
    FOLLOW_pseudoPage_in_page330 = frozenset([11])
    FOLLOW_LBRACE_in_page341 = frozenset([13])
    FOLLOW_declaration_in_page355 = frozenset([6])
    FOLLOW_SEMI_in_page357 = frozenset([12, 13])
    FOLLOW_declaration_in_page360 = frozenset([6])
    FOLLOW_SEMI_in_page362 = frozenset([12, 13])
    FOLLOW_RBRACE_in_page374 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage395 = frozenset([13])
    FOLLOW_IDENT_in_pseudoPage397 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator418 = frozenset([1])
    FOLLOW_COMMA_in_operator426 = frozenset([1])
    FOLLOW_PLUS_in_combinator453 = frozenset([1])
    FOLLOW_GREATER_in_combinator461 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_IDENT_in_property519 = frozenset([1])
    FOLLOW_selector_in_ruleSet540 = frozenset([9, 11])
    FOLLOW_COMMA_in_ruleSet543 = frozenset([13, 15, 20, 21, 22, 23])
    FOLLOW_selector_in_ruleSet545 = frozenset([9, 11])
    FOLLOW_LBRACE_in_ruleSet557 = frozenset([13])
    FOLLOW_declaration_in_ruleSet571 = frozenset([6])
    FOLLOW_SEMI_in_ruleSet573 = frozenset([12, 13])
    FOLLOW_declaration_in_ruleSet576 = frozenset([6])
    FOLLOW_SEMI_in_ruleSet578 = frozenset([12, 13])
    FOLLOW_RBRACE_in_ruleSet590 = frozenset([1])
    FOLLOW_simpleSelector_in_selector611 = frozenset([1, 13, 15, 17, 18, 20, 21, 22, 23])
    FOLLOW_combinator_in_selector614 = frozenset([13, 15, 20, 21, 22, 23])
    FOLLOW_simpleSelector_in_selector616 = frozenset([1, 13, 15, 17, 18, 20, 21, 22, 23])
    FOLLOW_elementName_in_simpleSelector635 = frozenset([1, 15, 20, 21, 22])
    FOLLOW_elementSubsequent_in_simpleSelector651 = frozenset([1, 15, 20, 21, 22])
    FOLLOW_elementSubsequent_in_simpleSelector675 = frozenset([1, 15, 20, 21, 22])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent731 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent739 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent747 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent755 = frozenset([1])
    FOLLOW_DOT_in_cssClass776 = frozenset([13])
    FOLLOW_IDENT_in_cssClass778 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib828 = frozenset([13])
    FOLLOW_IDENT_in_attrib843 = frozenset([24, 25, 26, 27])
    FOLLOW_set_in_attrib884 = frozenset([5, 13])
    FOLLOW_set_in_attrib992 = frozenset([27])
    FOLLOW_RBRACKET_in_attrib1093 = frozenset([1])
    FOLLOW_COLON_in_pseudo1106 = frozenset([13])
    FOLLOW_IDENT_in_pseudo1121 = frozenset([1, 28])
    FOLLOW_LPAREN_in_pseudo1179 = frozenset([13, 29])
    FOLLOW_IDENT_in_pseudo1181 = frozenset([29])
    FOLLOW_RPAREN_in_pseudo1184 = frozenset([1])
    FOLLOW_property_in_declaration1220 = frozenset([15])
    FOLLOW_COLON_in_declaration1222 = frozenset([5, 8, 13, 17, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_expr_in_declaration1224 = frozenset([1, 30])
    FOLLOW_prio_in_declaration1226 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1248 = frozenset([1])
    FOLLOW_term_in_expr1269 = frozenset([1, 5, 8, 9, 13, 16, 17, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_operator_in_expr1272 = frozenset([5, 8, 13, 17, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_term_in_expr1274 = frozenset([1, 5, 8, 9, 13, 16, 17, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_unaryOperator_in_term1297 = frozenset([31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_set_in_term1308 = frozenset([1])
    FOLLOW_STRING_in_term1454 = frozenset([1])
    FOLLOW_IDENT_in_term1462 = frozenset([1, 28])
    FOLLOW_LPAREN_in_term1485 = frozenset([5, 8, 13, 17, 19, 20, 31, 32, 33, 34, 35, 36, 37, 38])
    FOLLOW_expr_in_term1487 = frozenset([29])
    FOLLOW_RPAREN_in_term1489 = frozenset([1])
    FOLLOW_URI_in_term1512 = frozenset([1])
    FOLLOW_hexColor_in_term1520 = frozenset([1])
    FOLLOW_HASH_in_hexColor1541 = frozenset([1])
    FOLLOW_esPred_in_synpred1648 = frozenset([1])
    FOLLOW_esPred_in_synpred2672 = frozenset([1])


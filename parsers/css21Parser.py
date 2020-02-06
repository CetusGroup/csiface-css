# $ANTLR 3.4 css21.g 2012-02-12 14:26:07

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
A=4
ANGLE=5
B=6
C=7
CDC=8
CDO=9
CHARSET_SYM=10
COLON=11
COMMA=12
COMMENT=13
D=14
DASHMATCH=15
DIMENSION=16
DOT=17
E=18
EMS=19
ESCAPE=20
EXS=21
F=22
FREQ=23
G=24
GREATER=25
H=26
HASH=27
HEXCHAR=28
I=29
IDENT=30
IMPORTANT_SYM=31
IMPORT_SYM=32
INCLUDES=33
INVALID=34
J=35
K=36
L=37
LBRACE=38
LBRACKET=39
LENGTH=40
LPAREN=41
M=42
MEDIA_SYM=43
MINUS=44
N=45
NAME=46
NL=47
NMCHAR=48
NMSTART=49
NONASCII=50
NUMBER=51
O=52
OPEQ=53
P=54
PAGE_SYM=55
PERCENTAGE=56
PLUS=57
Q=58
R=59
RBRACE=60
RBRACKET=61
RPAREN=62
S=63
SEMI=64
SOLIDUS=65
STAR=66
STRING=67
T=68
TIME=69
U=70
UNICODE=71
URI=72
URL=73
V=74
W=75
WS=76
X=77
Y=78
Z=79

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "A", "ANGLE", "B", "C", "CDC", "CDO", "CHARSET_SYM", "COLON", "COMMA", 
    "COMMENT", "D", "DASHMATCH", "DIMENSION", "DOT", "E", "EMS", "ESCAPE", 
    "EXS", "F", "FREQ", "G", "GREATER", "H", "HASH", "HEXCHAR", "I", "IDENT", 
    "IMPORTANT_SYM", "IMPORT_SYM", "INCLUDES", "INVALID", "J", "K", "L", 
    "LBRACE", "LBRACKET", "LENGTH", "LPAREN", "M", "MEDIA_SYM", "MINUS", 
    "N", "NAME", "NL", "NMCHAR", "NMSTART", "NONASCII", "NUMBER", "O", "OPEQ", 
    "P", "PAGE_SYM", "PERCENTAGE", "PLUS", "Q", "R", "RBRACE", "RBRACKET", 
    "RPAREN", "S", "SEMI", "SOLIDUS", "STAR", "STRING", "T", "TIME", "U", 
    "UNICODE", "URI", "URL", "V", "W", "WS", "X", "Y", "Z"
]




class css21Parser(Parser):
    grammarFileName = "css21.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(css21Parser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "styleSheet"
    # css21.g:31:1: styleSheet : charSet ( imports )* bodylist EOF ;
    def styleSheet(self, ):
        try:
            try:
                # css21.g:32:5: ( charSet ( imports )* bodylist EOF )
                # css21.g:32:9: charSet ( imports )* bodylist EOF
                pass 
                self._state.following.append(self.FOLLOW_charSet_in_styleSheet53)
                self.charSet()

                self._state.following.pop()

                # css21.g:33:9: ( imports )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IMPORT_SYM) :
                        alt1 = 1


                    if alt1 == 1:
                        # css21.g:33:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet63)
                        self.imports()

                        self._state.following.pop()


                    else:
                        break #loop1


                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet74)
                self.bodylist()

                self._state.following.pop()

                self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet81)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "styleSheet"



    # $ANTLR start "charSet"
    # css21.g:41:1: charSet : ( CHARSET_SYM STRING SEMI |);
    def charSet(self, ):
        try:
            try:
                # css21.g:42:5: ( CHARSET_SYM STRING SEMI |)
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CHARSET_SYM) :
                    alt2 = 1
                elif (LA2_0 == EOF or LA2_0 == COLON or LA2_0 == DOT or LA2_0 == HASH or LA2_0 == IDENT or LA2_0 == IMPORT_SYM or LA2_0 == LBRACKET or LA2_0 == MEDIA_SYM or LA2_0 == PAGE_SYM or LA2_0 == STAR) :
                    alt2 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # css21.g:42:9: CHARSET_SYM STRING SEMI
                    pass 
                    self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet107)

                    self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet109)

                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet111)


                elif alt2 == 2:
                    # css21.g:44:5: 
                    pass 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "charSet"



    # $ANTLR start "imports"
    # css21.g:49:1: imports : IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI ;
    def imports(self, ):
        try:
            try:
                # css21.g:50:5: ( IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI )
                # css21.g:50:9: IMPORT_SYM ( STRING | URI ) ( medium ( COMMA medium )* )? SEMI
                pass 
                self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports139)

                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse



                # css21.g:50:33: ( medium ( COMMA medium )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # css21.g:50:34: medium ( COMMA medium )*
                    pass 
                    self._state.following.append(self.FOLLOW_medium_in_imports148)
                    self.medium()

                    self._state.following.pop()

                    # css21.g:50:41: ( COMMA medium )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # css21.g:50:42: COMMA medium
                            pass 
                            self.match(self.input, COMMA, self.FOLLOW_COMMA_in_imports151)

                            self._state.following.append(self.FOLLOW_medium_in_imports153)
                            self.medium()

                            self._state.following.pop()


                        else:
                            break #loop3





                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports159)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "imports"



    # $ANTLR start "media"
    # css21.g:57:1: media : MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE ;
    def media(self, ):
        try:
            try:
                # css21.g:58:5: ( MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE )
                # css21.g:58:7: MEDIA_SYM medium ( COMMA medium )* LBRACE ruleSet RBRACE
                pass 
                self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media180)

                self._state.following.append(self.FOLLOW_medium_in_media182)
                self.medium()

                self._state.following.pop()

                # css21.g:58:24: ( COMMA medium )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # css21.g:58:25: COMMA medium
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media185)

                        self._state.following.append(self.FOLLOW_medium_in_media187)
                        self.medium()

                        self._state.following.pop()


                    else:
                        break #loop5


                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media199)

                self._state.following.append(self.FOLLOW_ruleSet_in_media213)
                self.ruleSet()

                self._state.following.pop()

                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media223)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "media"



    # $ANTLR start "medium"
    # css21.g:67:1: medium : IDENT ;
    def medium(self, ):
        try:
            try:
                # css21.g:68:5: ( IDENT )
                # css21.g:68:7: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_medium243)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "medium"



    # $ANTLR start "bodylist"
    # css21.g:72:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):
        try:
            try:
                # css21.g:73:5: ( ( bodyset )* )
                # css21.g:73:7: ( bodyset )*
                pass 
                # css21.g:73:7: ( bodyset )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COLON or LA6_0 == DOT or LA6_0 == HASH or LA6_0 == IDENT or LA6_0 == LBRACKET or LA6_0 == MEDIA_SYM or LA6_0 == PAGE_SYM or LA6_0 == STAR) :
                        alt6 = 1


                    if alt6 == 1:
                        # css21.g:73:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist266)
                        self.bodyset()

                        self._state.following.pop()


                    else:
                        break #loop6





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "bodylist"



    # $ANTLR start "bodyset"
    # css21.g:76:1: bodyset : ( ruleSet | media | page );
    def bodyset(self, ):
        try:
            try:
                # css21.g:77:5: ( ruleSet | media | page )
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == COLON or LA7 == DOT or LA7 == HASH or LA7 == IDENT or LA7 == LBRACKET or LA7 == STAR:
                    alt7 = 1
                elif LA7 == MEDIA_SYM:
                    alt7 = 2
                elif LA7 == PAGE_SYM:
                    alt7 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # css21.g:77:7: ruleSet
                    pass 
                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset288)
                    self.ruleSet()

                    self._state.following.pop()


                elif alt7 == 2:
                    # css21.g:78:7: media
                    pass 
                    self._state.following.append(self.FOLLOW_media_in_bodyset296)
                    self.media()

                    self._state.following.pop()


                elif alt7 == 3:
                    # css21.g:79:7: page
                    pass 
                    self._state.following.append(self.FOLLOW_page_in_bodyset304)
                    self.page()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "bodyset"



    # $ANTLR start "page"
    # css21.g:82:1: page : PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE ;
    def page(self, ):
        try:
            try:
                # css21.g:83:5: ( PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE )
                # css21.g:83:7: PAGE_SYM ( pseudoPage )? LBRACE declaration SEMI ( declaration SEMI )* RBRACE
                pass 
                self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page328)

                # css21.g:83:16: ( pseudoPage )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == COLON) :
                    alt8 = 1
                if alt8 == 1:
                    # css21.g:83:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page330)
                    self.pseudoPage()

                    self._state.following.pop()




                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page341)

                self._state.following.append(self.FOLLOW_declaration_in_page355)
                self.declaration()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_page357)

                # css21.g:85:30: ( declaration SEMI )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENT) :
                        alt9 = 1


                    if alt9 == 1:
                        # css21.g:85:31: declaration SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_declaration_in_page360)
                        self.declaration()

                        self._state.following.pop()

                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_page362)


                    else:
                        break #loop9


                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page374)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "page"



    # $ANTLR start "pseudoPage"
    # css21.g:89:1: pseudoPage : COLON IDENT ;
    def pseudoPage(self, ):
        try:
            try:
                # css21.g:90:5: ( COLON IDENT )
                # css21.g:90:7: COLON IDENT
                pass 
                self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage395)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage397)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "pseudoPage"



    # $ANTLR start "operator"
    # css21.g:93:1: operator : ( SOLIDUS | COMMA |);
    def operator(self, ):
        try:
            try:
                # css21.g:94:5: ( SOLIDUS | COMMA |)
                alt10 = 3
                LA10 = self.input.LA(1)
                if LA10 == SOLIDUS:
                    alt10 = 1
                elif LA10 == COMMA:
                    alt10 = 2
                elif LA10 == ANGLE or LA10 == EMS or LA10 == EXS or LA10 == FREQ or LA10 == HASH or LA10 == IDENT or LA10 == LENGTH or LA10 == MINUS or LA10 == NUMBER or LA10 == PERCENTAGE or LA10 == PLUS or LA10 == STRING or LA10 == TIME or LA10 == URI:
                    alt10 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # css21.g:94:7: SOLIDUS
                    pass 
                    self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator418)


                elif alt10 == 2:
                    # css21.g:95:7: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator426)


                elif alt10 == 3:
                    # css21.g:97:5: 
                    pass 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "operator"



    # $ANTLR start "combinator"
    # css21.g:99:1: combinator : ( PLUS | GREATER |);
    def combinator(self, ):
        try:
            try:
                # css21.g:100:5: ( PLUS | GREATER |)
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == PLUS:
                    alt11 = 1
                elif LA11 == GREATER:
                    alt11 = 2
                elif LA11 == COLON or LA11 == DOT or LA11 == HASH or LA11 == IDENT or LA11 == LBRACKET or LA11 == STAR:
                    alt11 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # css21.g:100:7: PLUS
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator453)


                elif alt11 == 2:
                    # css21.g:101:7: GREATER
                    pass 
                    self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator461)


                elif alt11 == 3:
                    # css21.g:103:5: 
                    pass 


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "combinator"



    # $ANTLR start "unaryOperator"
    # css21.g:105:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):
        try:
            try:
                # css21.g:106:5: ( MINUS | PLUS )
                # css21.g:
                pass 
                if self.input.LA(1) == MINUS or self.input.LA(1) == PLUS:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "unaryOperator"



    # $ANTLR start "property"
    # css21.g:110:1: property : IDENT ;
    def property(self, ):
        try:
            try:
                # css21.g:111:5: ( IDENT )
                # css21.g:111:7: IDENT
                pass 
                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property519)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "property"



    # $ANTLR start "ruleSet"
    # css21.g:114:1: ruleSet : selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE ;
    def ruleSet(self, ):
        try:
            try:
                # css21.g:115:5: ( selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE )
                # css21.g:115:7: selector ( COMMA selector )* LBRACE declaration SEMI ( declaration SEMI )* RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet540)
                self.selector()

                self._state.following.pop()

                # css21.g:115:16: ( COMMA selector )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == COMMA) :
                        alt12 = 1


                    if alt12 == 1:
                        # css21.g:115:17: COMMA selector
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet543)

                        self._state.following.append(self.FOLLOW_selector_in_ruleSet545)
                        self.selector()

                        self._state.following.pop()


                    else:
                        break #loop12


                self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet557)

                self._state.following.append(self.FOLLOW_declaration_in_ruleSet571)
                self.declaration()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_ruleSet573)

                # css21.g:117:30: ( declaration SEMI )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == IDENT) :
                        alt13 = 1


                    if alt13 == 1:
                        # css21.g:117:31: declaration SEMI
                        pass 
                        self._state.following.append(self.FOLLOW_declaration_in_ruleSet576)
                        self.declaration()

                        self._state.following.pop()

                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_ruleSet578)


                    else:
                        break #loop13


                self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet590)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "ruleSet"



    # $ANTLR start "selector"
    # css21.g:121:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):
        try:
            try:
                # css21.g:122:5: ( simpleSelector ( combinator simpleSelector )* )
                # css21.g:122:7: simpleSelector ( combinator simpleSelector )*
                pass 
                self._state.following.append(self.FOLLOW_simpleSelector_in_selector611)
                self.simpleSelector()

                self._state.following.pop()

                # css21.g:122:22: ( combinator simpleSelector )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == COLON or LA14_0 == DOT or LA14_0 == GREATER or LA14_0 == HASH or LA14_0 == IDENT or LA14_0 == LBRACKET or LA14_0 == PLUS or LA14_0 == STAR) :
                        alt14 = 1


                    if alt14 == 1:
                        # css21.g:122:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector614)
                        self.combinator()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector616)
                        self.simpleSelector()

                        self._state.following.pop()


                    else:
                        break #loop14





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "selector"



    # $ANTLR start "simpleSelector"
    # css21.g:125:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):
        try:
            try:
                # css21.g:126:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == IDENT or LA17_0 == STAR) :
                    alt17 = 1
                elif (LA17_0 == COLON or LA17_0 == DOT or LA17_0 == HASH or LA17_0 == LBRACKET) :
                    alt17 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # css21.g:126:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector635)
                    self.elementName()

                    self._state.following.pop()

                    # css21.g:127:9: ( ( esPred )=> elementSubsequent )*
                    while True: #loop15
                        alt15 = 2
                        LA15 = self.input.LA(1)
                        if LA15 == HASH:
                            LA15_2 = self.input.LA(2)

                            if (self.synpred1_css21()) :
                                alt15 = 1


                        elif LA15 == DOT:
                            LA15_3 = self.input.LA(2)

                            if (LA15_3 == IDENT) :
                                LA15_7 = self.input.LA(3)

                                if (self.synpred1_css21()) :
                                    alt15 = 1




                        elif LA15 == LBRACKET:
                            LA15_4 = self.input.LA(2)

                            if (LA15_4 == IDENT) :
                                LA15_8 = self.input.LA(3)

                                if (LA15_8 == DASHMATCH or LA15_8 == INCLUDES or LA15_8 == OPEQ) :
                                    LA15_10 = self.input.LA(4)

                                    if (LA15_10 == IDENT or LA15_10 == STRING) :
                                        LA15_12 = self.input.LA(5)

                                        if (LA15_12 == RBRACKET) :
                                            LA15_13 = self.input.LA(6)

                                            if (self.synpred1_css21()) :
                                                alt15 = 1






                                elif (LA15_8 == RBRACKET) :
                                    LA15_11 = self.input.LA(4)

                                    if (self.synpred1_css21()) :
                                        alt15 = 1






                        elif LA15 == COLON:
                            LA15_5 = self.input.LA(2)

                            if (LA15_5 == IDENT) :
                                LA15_9 = self.input.LA(3)

                                if (self.synpred1_css21()) :
                                    alt15 = 1





                        if alt15 == 1:
                            # css21.g:127:10: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector651)
                            self.elementSubsequent()

                            self._state.following.pop()


                        else:
                            break #loop15



                elif alt17 == 2:
                    # css21.g:129:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    # css21.g:129:7: ( ( esPred )=> elementSubsequent )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16 = self.input.LA(1)
                        if LA16 == HASH:
                            LA16_2 = self.input.LA(2)

                            if (self.synpred2_css21()) :
                                alt16 = 1


                        elif LA16 == DOT:
                            LA16_3 = self.input.LA(2)

                            if (self.synpred2_css21()) :
                                alt16 = 1


                        elif LA16 == LBRACKET:
                            LA16_4 = self.input.LA(2)

                            if (self.synpred2_css21()) :
                                alt16 = 1


                        elif LA16 == COLON:
                            LA16_5 = self.input.LA(2)

                            if (self.synpred2_css21()) :
                                alt16 = 1



                        if alt16 == 1:
                            # css21.g:129:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector675)
                            self.elementSubsequent()

                            self._state.following.pop()


                        else:
                            if cnt16 >= 1:
                                break #loop16

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "simpleSelector"



    # $ANTLR start "esPred"
    # css21.g:132:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):
        try:
            try:
                # css21.g:133:5: ( HASH | DOT | LBRACKET | COLON )
                # css21.g:
                pass 
                if self.input.LA(1) == COLON or self.input.LA(1) == DOT or self.input.LA(1) == HASH or self.input.LA(1) == LBRACKET:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "esPred"



    # $ANTLR start "elementSubsequent"
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
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # css21.g:137:7: HASH
                    pass 
                    self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent731)


                elif alt18 == 2:
                    # css21.g:138:7: cssClass
                    pass 
                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent739)
                    self.cssClass()

                    self._state.following.pop()


                elif alt18 == 3:
                    # css21.g:139:7: attrib
                    pass 
                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent747)
                    self.attrib()

                    self._state.following.pop()


                elif alt18 == 4:
                    # css21.g:140:7: pseudo
                    pass 
                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent755)
                    self.pseudo()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "elementSubsequent"



    # $ANTLR start "cssClass"
    # css21.g:143:1: cssClass : DOT IDENT ;
    def cssClass(self, ):
        try:
            try:
                # css21.g:144:5: ( DOT IDENT )
                # css21.g:144:7: DOT IDENT
                pass 
                self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass776)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass778)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "cssClass"



    # $ANTLR start "elementName"
    # css21.g:147:1: elementName : ( IDENT | STAR );
    def elementName(self, ):
        try:
            try:
                # css21.g:148:5: ( IDENT | STAR )
                # css21.g:
                pass 
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "elementName"



    # $ANTLR start "attrib"
    # css21.g:152:1: attrib : LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET ;
    def attrib(self, ):
        try:
            try:
                # css21.g:153:5: ( LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET )
                # css21.g:153:7: LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET
                pass 
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib828)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attrib843)

                # css21.g:157:13: ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == DASHMATCH or LA19_0 == INCLUDES or LA19_0 == OPEQ) :
                    alt19 = 1
                if alt19 == 1:
                    # css21.g:158:17: ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    if self.input.LA(1) == DASHMATCH or self.input.LA(1) == INCLUDES or self.input.LA(1) == OPEQ:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse



                    if self.input.LA(1) == IDENT or self.input.LA(1) == STRING:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse






                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1093)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "attrib"



    # $ANTLR start "pseudo"
    # css21.g:172:1: pseudo : COLON IDENT ( LPAREN ( IDENT )? RPAREN )? ;
    def pseudo(self, ):
        try:
            try:
                # css21.g:173:5: ( COLON IDENT ( LPAREN ( IDENT )? RPAREN )? )
                # css21.g:173:7: COLON IDENT ( LPAREN ( IDENT )? RPAREN )?
                pass 
                self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1106)

                self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1121)

                # css21.g:175:17: ( LPAREN ( IDENT )? RPAREN )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == LPAREN) :
                    alt21 = 1
                if alt21 == 1:
                    # css21.g:177:21: LPAREN ( IDENT )? RPAREN
                    pass 
                    self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_pseudo1179)

                    # css21.g:177:28: ( IDENT )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == IDENT) :
                        alt20 = 1
                    if alt20 == 1:
                        # css21.g:177:28: IDENT
                        pass 
                        self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1181)




                    self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1184)







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "pseudo"



    # $ANTLR start "declaration"
    # css21.g:181:1: declaration : property COLON expr ( prio )? ;
    def declaration(self, ):
        try:
            try:
                # css21.g:182:5: ( property COLON expr ( prio )? )
                # css21.g:182:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1220)
                self.property()

                self._state.following.pop()

                self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1222)

                self._state.following.append(self.FOLLOW_expr_in_declaration1224)
                self.expr()

                self._state.following.pop()

                # css21.g:182:27: ( prio )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IMPORTANT_SYM) :
                    alt22 = 1
                if alt22 == 1:
                    # css21.g:182:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1226)
                    self.prio()

                    self._state.following.pop()







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "declaration"



    # $ANTLR start "prio"
    # css21.g:185:1: prio : IMPORTANT_SYM ;
    def prio(self, ):
        try:
            try:
                # css21.g:186:5: ( IMPORTANT_SYM )
                # css21.g:186:7: IMPORTANT_SYM
                pass 
                self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1248)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prio"



    # $ANTLR start "expr"
    # css21.g:189:1: expr : term ( operator term )* ;
    def expr(self, ):
        try:
            try:
                # css21.g:190:5: ( term ( operator term )* )
                # css21.g:190:7: term ( operator term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_expr1269)
                self.term()

                self._state.following.pop()

                # css21.g:190:12: ( operator term )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == ANGLE or LA23_0 == COMMA or LA23_0 == EMS or LA23_0 == EXS or LA23_0 == FREQ or LA23_0 == HASH or LA23_0 == IDENT or LA23_0 == LENGTH or LA23_0 == MINUS or LA23_0 == NUMBER or (PERCENTAGE <= LA23_0 <= PLUS) or LA23_0 == SOLIDUS or LA23_0 == STRING or LA23_0 == TIME or LA23_0 == URI) :
                        alt23 = 1


                    if alt23 == 1:
                        # css21.g:190:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1272)
                        self.operator()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_term_in_expr1274)
                        self.term()

                        self._state.following.pop()


                    else:
                        break #loop23





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "expr"



    # $ANTLR start "term"
    # css21.g:193:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT ( LPAREN expr RPAREN )? | URI | hexColor );
    def term(self, ):
        try:
            try:
                # css21.g:194:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT ( LPAREN expr RPAREN )? | URI | hexColor )
                alt26 = 5
                LA26 = self.input.LA(1)
                if LA26 == ANGLE or LA26 == EMS or LA26 == EXS or LA26 == FREQ or LA26 == LENGTH or LA26 == MINUS or LA26 == NUMBER or LA26 == PERCENTAGE or LA26 == PLUS or LA26 == TIME:
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
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # css21.g:194:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    pass 
                    # css21.g:194:7: ( unaryOperator )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == MINUS or LA24_0 == PLUS) :
                        alt24 = 1
                    if alt24 == 1:
                        # css21.g:194:7: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1297)
                        self.unaryOperator()

                        self._state.following.pop()




                    if self.input.LA(1) == ANGLE or self.input.LA(1) == EMS or self.input.LA(1) == EXS or self.input.LA(1) == FREQ or self.input.LA(1) == LENGTH or self.input.LA(1) == NUMBER or self.input.LA(1) == PERCENTAGE or self.input.LA(1) == TIME:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt26 == 2:
                    # css21.g:205:7: STRING
                    pass 
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_term1454)


                elif alt26 == 3:
                    # css21.g:206:7: IDENT ( LPAREN expr RPAREN )?
                    pass 
                    self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1462)

                    # css21.g:206:13: ( LPAREN expr RPAREN )?
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LPAREN) :
                        alt25 = 1
                    if alt25 == 1:
                        # css21.g:207:17: LPAREN expr RPAREN
                        pass 
                        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_term1485)

                        self._state.following.append(self.FOLLOW_expr_in_term1487)
                        self.expr()

                        self._state.following.pop()

                        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_term1489)





                elif alt26 == 4:
                    # css21.g:209:7: URI
                    pass 
                    self.match(self.input, URI, self.FOLLOW_URI_in_term1512)


                elif alt26 == 5:
                    # css21.g:210:7: hexColor
                    pass 
                    self._state.following.append(self.FOLLOW_hexColor_in_term1520)
                    self.hexColor()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "term"



    # $ANTLR start "hexColor"
    # css21.g:213:1: hexColor : HASH ;
    def hexColor(self, ):
        try:
            try:
                # css21.g:214:5: ( HASH )
                # css21.g:214:7: HASH
                pass 
                self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1541)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "hexColor"

    # $ANTLR start "synpred1_css21"
    def synpred1_css21_fragment(self, ):
        # css21.g:127:10: ( esPred )
        # css21.g:127:11: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_css21648)
        self.esPred()

        self._state.following.pop()



    # $ANTLR end "synpred1_css21"



    # $ANTLR start "synpred2_css21"
    def synpred2_css21_fragment(self, ):
        # css21.g:129:8: ( esPred )
        # css21.g:129:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_css21672)
        self.esPred()

        self._state.following.pop()



    # $ANTLR end "synpred2_css21"




    def synpred2_css21(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_css21_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_css21(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_css21_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_charSet_in_styleSheet53 = frozenset([11, 17, 27, 30, 32, 39, 43, 55, 66])
    FOLLOW_imports_in_styleSheet63 = frozenset([11, 17, 27, 30, 32, 39, 43, 55, 66])
    FOLLOW_bodylist_in_styleSheet74 = frozenset([])
    FOLLOW_EOF_in_styleSheet81 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet107 = frozenset([67])
    FOLLOW_STRING_in_charSet109 = frozenset([64])
    FOLLOW_SEMI_in_charSet111 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports139 = frozenset([67, 72])
    FOLLOW_set_in_imports141 = frozenset([30, 64])
    FOLLOW_medium_in_imports148 = frozenset([12, 64])
    FOLLOW_COMMA_in_imports151 = frozenset([30])
    FOLLOW_medium_in_imports153 = frozenset([12, 64])
    FOLLOW_SEMI_in_imports159 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media180 = frozenset([30])
    FOLLOW_medium_in_media182 = frozenset([12, 38])
    FOLLOW_COMMA_in_media185 = frozenset([30])
    FOLLOW_medium_in_media187 = frozenset([12, 38])
    FOLLOW_LBRACE_in_media199 = frozenset([11, 17, 27, 30, 39, 66])
    FOLLOW_ruleSet_in_media213 = frozenset([60])
    FOLLOW_RBRACE_in_media223 = frozenset([1])
    FOLLOW_IDENT_in_medium243 = frozenset([1])
    FOLLOW_bodyset_in_bodylist266 = frozenset([1, 11, 17, 27, 30, 39, 43, 55, 66])
    FOLLOW_ruleSet_in_bodyset288 = frozenset([1])
    FOLLOW_media_in_bodyset296 = frozenset([1])
    FOLLOW_page_in_bodyset304 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page328 = frozenset([11, 38])
    FOLLOW_pseudoPage_in_page330 = frozenset([38])
    FOLLOW_LBRACE_in_page341 = frozenset([30])
    FOLLOW_declaration_in_page355 = frozenset([64])
    FOLLOW_SEMI_in_page357 = frozenset([30, 60])
    FOLLOW_declaration_in_page360 = frozenset([64])
    FOLLOW_SEMI_in_page362 = frozenset([30, 60])
    FOLLOW_RBRACE_in_page374 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage395 = frozenset([30])
    FOLLOW_IDENT_in_pseudoPage397 = frozenset([1])
    FOLLOW_SOLIDUS_in_operator418 = frozenset([1])
    FOLLOW_COMMA_in_operator426 = frozenset([1])
    FOLLOW_PLUS_in_combinator453 = frozenset([1])
    FOLLOW_GREATER_in_combinator461 = frozenset([1])
    FOLLOW_IDENT_in_property519 = frozenset([1])
    FOLLOW_selector_in_ruleSet540 = frozenset([12, 38])
    FOLLOW_COMMA_in_ruleSet543 = frozenset([11, 17, 27, 30, 39, 66])
    FOLLOW_selector_in_ruleSet545 = frozenset([12, 38])
    FOLLOW_LBRACE_in_ruleSet557 = frozenset([30])
    FOLLOW_declaration_in_ruleSet571 = frozenset([64])
    FOLLOW_SEMI_in_ruleSet573 = frozenset([30, 60])
    FOLLOW_declaration_in_ruleSet576 = frozenset([64])
    FOLLOW_SEMI_in_ruleSet578 = frozenset([30, 60])
    FOLLOW_RBRACE_in_ruleSet590 = frozenset([1])
    FOLLOW_simpleSelector_in_selector611 = frozenset([1, 11, 17, 25, 27, 30, 39, 57, 66])
    FOLLOW_combinator_in_selector614 = frozenset([11, 17, 27, 30, 39, 66])
    FOLLOW_simpleSelector_in_selector616 = frozenset([1, 11, 17, 25, 27, 30, 39, 57, 66])
    FOLLOW_elementName_in_simpleSelector635 = frozenset([1, 11, 17, 27, 39])
    FOLLOW_elementSubsequent_in_simpleSelector651 = frozenset([1, 11, 17, 27, 39])
    FOLLOW_elementSubsequent_in_simpleSelector675 = frozenset([1, 11, 17, 27, 39])
    FOLLOW_HASH_in_elementSubsequent731 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent739 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent747 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent755 = frozenset([1])
    FOLLOW_DOT_in_cssClass776 = frozenset([30])
    FOLLOW_IDENT_in_cssClass778 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib828 = frozenset([30])
    FOLLOW_IDENT_in_attrib843 = frozenset([15, 33, 53, 61])
    FOLLOW_set_in_attrib884 = frozenset([30, 67])
    FOLLOW_set_in_attrib992 = frozenset([61])
    FOLLOW_RBRACKET_in_attrib1093 = frozenset([1])
    FOLLOW_COLON_in_pseudo1106 = frozenset([30])
    FOLLOW_IDENT_in_pseudo1121 = frozenset([1, 41])
    FOLLOW_LPAREN_in_pseudo1179 = frozenset([30, 62])
    FOLLOW_IDENT_in_pseudo1181 = frozenset([62])
    FOLLOW_RPAREN_in_pseudo1184 = frozenset([1])
    FOLLOW_property_in_declaration1220 = frozenset([11])
    FOLLOW_COLON_in_declaration1222 = frozenset([5, 19, 21, 23, 27, 30, 40, 44, 51, 56, 57, 67, 69, 72])
    FOLLOW_expr_in_declaration1224 = frozenset([1, 31])
    FOLLOW_prio_in_declaration1226 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1248 = frozenset([1])
    FOLLOW_term_in_expr1269 = frozenset([1, 5, 12, 19, 21, 23, 27, 30, 40, 44, 51, 56, 57, 65, 67, 69, 72])
    FOLLOW_operator_in_expr1272 = frozenset([5, 19, 21, 23, 27, 30, 40, 44, 51, 56, 57, 67, 69, 72])
    FOLLOW_term_in_expr1274 = frozenset([1, 5, 12, 19, 21, 23, 27, 30, 40, 44, 51, 56, 57, 65, 67, 69, 72])
    FOLLOW_unaryOperator_in_term1297 = frozenset([5, 19, 21, 23, 40, 51, 56, 69])
    FOLLOW_set_in_term1308 = frozenset([1])
    FOLLOW_STRING_in_term1454 = frozenset([1])
    FOLLOW_IDENT_in_term1462 = frozenset([1, 41])
    FOLLOW_LPAREN_in_term1485 = frozenset([5, 19, 21, 23, 27, 30, 40, 44, 51, 56, 57, 67, 69, 72])
    FOLLOW_expr_in_term1487 = frozenset([62])
    FOLLOW_RPAREN_in_term1489 = frozenset([1])
    FOLLOW_URI_in_term1512 = frozenset([1])
    FOLLOW_hexColor_in_term1520 = frozenset([1])
    FOLLOW_HASH_in_hexColor1541 = frozenset([1])
    FOLLOW_esPred_in_synpred1_css21648 = frozenset([1])
    FOLLOW_esPred_in_synpred2_css21672 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("css21Lexer", css21Parser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)

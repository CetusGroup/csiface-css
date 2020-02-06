lexer grammar css21;
options {
  language=Python;

}

// $ANTLR src "css21.g" 261
fragment    HEXCHAR     : ('a'..'f'|'A'..'F'|'0'..'9')  ;

// $ANTLR src "css21.g" 263
fragment    NONASCII    : '\u0080'..'\uFFFF'            ;   // NB: Upper bound should be \u4177777

// $ANTLR src "css21.g" 265
fragment    UNICODE     : '\\' HEXCHAR 
                                (HEXCHAR 
                                    (HEXCHAR 
                                        (HEXCHAR 
                                            (HEXCHAR HEXCHAR?)?
                                        )?
                                    )?
                                )? 
                                ('\r'|'\n'|'\t'|'\f'|' ')*  ;
                                
// $ANTLR src "css21.g" 275
fragment    ESCAPE      : UNICODE | '\\' ~('\r'|'\n'|'\f'|HEXCHAR)  ;

// $ANTLR src "css21.g" 277
fragment    NMSTART     : '_'
                        | 'a'..'z'
                        | 'A'..'Z'
                        | NONASCII
                        | ESCAPE
                        ;

// $ANTLR src "css21.g" 284
fragment    NMCHAR      : '_'
                        | 'a'..'z'
                        | 'A'..'Z'
                        | '0'..'9'
                        | '-'
                        | NONASCII
                        | ESCAPE
                        ;
                        
// $ANTLR src "css21.g" 293
fragment    NAME        : NMCHAR+   ;

// $ANTLR src "css21.g" 295
fragment    URL         : ( 
                              '['|'!'|'#'|'$'|'%'|'&'|'*'|'-'|'~'
                            | NONASCII
                            | ESCAPE
                          )*
                        ;

                        
// Basic Alpha characters in upper, lower and escaped form. Note that
// whitespace and newlines are unimportant even within keywords. We do not
// however call a further fragment rule to consume these characters for
// reasons of performance - the rules are still eminently readable.
//
// $ANTLR src "css21.g" 308
fragment    A   :   ('a'|'A') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'1'
                ;
// $ANTLR src "css21.g" 311
fragment    B   :   ('b'|'B') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'2'
                ;
// $ANTLR src "css21.g" 314
fragment    C   :   ('c'|'C') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'3'
                ;
// $ANTLR src "css21.g" 317
fragment    D   :   ('d'|'D') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'4'
                ;
// $ANTLR src "css21.g" 320
fragment    E   :   ('e'|'E') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'5'
                ;
// $ANTLR src "css21.g" 323
fragment    F   :   ('f'|'F') ('\r'|'\n'|'\t'|'\f'|' ')*    
                |   '\\' ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'6'
                ;
// $ANTLR src "css21.g" 326
fragment    G   :   ('g'|'G') ('\r'|'\n'|'\t'|'\f'|' ')* 
                |   '\\'
                        (
                              'g'
                            | 'G'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'7'
                        )
                ;
// $ANTLR src "css21.g" 334
fragment    H   :   ('h'|'H') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'h'
                            | 'H'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'8'
                        )   
                ;
// $ANTLR src "css21.g" 342
fragment    I   :   ('i'|'I') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'i'
                            | 'I'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')'9'
                        )
                ;
// $ANTLR src "css21.g" 350
fragment    J   :   ('j'|'J') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'j'
                            | 'J'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('A'|'a')
                        )   
                ;
// $ANTLR src "css21.g" 358
fragment    K   :   ('k'|'K') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'k'
                            | 'K'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('B'|'b')
                        )   
                ;
// $ANTLR src "css21.g" 366
fragment    L   :   ('l'|'L') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'l'
                            | 'L'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('C'|'c')
                        )   
                ;
// $ANTLR src "css21.g" 374
fragment    M   :   ('m'|'M') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'm'
                            | 'M'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('D'|'d')
                        )   
                ;
// $ANTLR src "css21.g" 382
fragment    N   :   ('n'|'N') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'n'
                            | 'N'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('E'|'e')
                        )   
                ;
// $ANTLR src "css21.g" 390
fragment    O   :   ('o'|'O') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'o'
                            | 'O'
                            | ('0' ('0' ('0' '0'?)?)?)? ('4'|'6')('F'|'f')
                        )   
                ;
// $ANTLR src "css21.g" 398
fragment    P   :   ('p'|'P') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\'
                        (
                              'p'
                            | 'P'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('0')
                        )   
                ;
// $ANTLR src "css21.g" 406
fragment    Q   :   ('q'|'Q') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'q'
                            | 'Q'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('1')
                        )   
                ;
// $ANTLR src "css21.g" 414
fragment    R   :   ('r'|'R') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'r'
                            | 'R'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('2')
                        )   
                ;
// $ANTLR src "css21.g" 422
fragment    S   :   ('s'|'S') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              's'
                            | 'S'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('3')
                        )   
                ;
// $ANTLR src "css21.g" 430
fragment    T   :   ('t'|'T') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              't'
                            | 'T'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('4')
                        )   
                ;
// $ANTLR src "css21.g" 438
fragment    U   :   ('u'|'U') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'u'
                            | 'U'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('5')
                        )
                ;
// $ANTLR src "css21.g" 446
fragment    V   :   ('v'|'V') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (     'v'
                            | 'V'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('6')
                        )
                ;
// $ANTLR src "css21.g" 453
fragment    W   :   ('w'|'W') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'w'
                            | 'W'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('7')
                        )   
                ;
// $ANTLR src "css21.g" 461
fragment    X   :   ('x'|'X') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'x'
                            | 'X'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('8')
                        )
                ;
// $ANTLR src "css21.g" 469
fragment    Y   :   ('y'|'Y') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'y'
                            | 'Y'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('9')
                        )
                ;
// $ANTLR src "css21.g" 477
fragment    Z   :   ('z'|'Z') ('\r'|'\n'|'\t'|'\f'|' ')* 
                | '\\' 
                        (
                              'z'
                            | 'Z'
                            | ('0' ('0' ('0' '0'?)?)?)? ('5'|'7')('A'|'a')
                        )
                ;


// -------------
// Comments.    Comments may not be nested, may be multilined and are delimited
//              like C comments: /* ..... */
//              COMMENTS are hidden from the parser which simplifies the parser 
//              grammar a lot.
//
// $ANTLR src "css21.g" 493
COMMENT         : '/*' ( options { greedy=false; } : .*) '*/'
    
                    {
                        $channel = 2 #;   // Comments on channel 2 in case we want to find them
                    }
                ;

// ---------------------
// HTML comment open.   HTML/XML comments may be placed around style sheets so that they
//                      are hidden from higher scope parsing engines such as HTML parsers.
//                      They comment open is therfore ignored by the CSS parser and we hide
//                      it from the ANLTR parser.
//
// $ANTLR src "css21.g" 506
CDO             : '<!--'

                    {
                        $channel = 3 #;   // CDO on channel 3 in case we want it later
                    }
                ;
    
// ---------------------            
// HTML comment close.  HTML/XML comments may be placed around style sheets so that they
//                      are hidden from higher scope parsing engines such as HTML parsers.
//                      They comment close is therfore ignored by the CSS parser and we hide
//                      it from the ANLTR parser.
//
// $ANTLR src "css21.g" 519
CDC             : '-->'

                    {
                        $channel = 4 #;   // CDC on channel 4 in case we want it later
                    }
                ;
                
// $ANTLR src "css21.g" 526
INCLUDES        : '~='      ;
// $ANTLR src "css21.g" 527
DASHMATCH       : '|='      ;

// $ANTLR src "css21.g" 529
GREATER         : '>'       ;
// $ANTLR src "css21.g" 530
LBRACE          : '{'       ;
// $ANTLR src "css21.g" 531
RBRACE          : '}'       ;
// $ANTLR src "css21.g" 532
LBRACKET        : '['       ;
// $ANTLR src "css21.g" 533
RBRACKET        : ']'       ;
// $ANTLR src "css21.g" 534
OPEQ            : '='       ;
// $ANTLR src "css21.g" 535
SEMI            : ';'       ;
// $ANTLR src "css21.g" 536
COLON           : ':'       ;
// $ANTLR src "css21.g" 537
SOLIDUS         : '/'       ;
// $ANTLR src "css21.g" 538
MINUS           : '-'       ;
// $ANTLR src "css21.g" 539
PLUS            : '+'       ;
// $ANTLR src "css21.g" 540
STAR            : '*'       ;
// $ANTLR src "css21.g" 541
LPAREN          : '('       ;
// $ANTLR src "css21.g" 542
RPAREN          : ')'       ;
// $ANTLR src "css21.g" 543
COMMA           : ','       ;
// $ANTLR src "css21.g" 544
DOT             : '.'       ;

// -----------------
// Literal strings. Delimited by either ' or "
//
// $ANTLR src "css21.g" 549
fragment    INVALID :;
// $ANTLR src "css21.g" 550
STRING          : '\'' ( ~('\n'|'\r'|'\f'|'\'') )* 
                    (
                          '\''
                        | { $type = INVALID; }
                    )
                    
                | '"' ( ~('\n'|'\r'|'\f'|'"') )*
                    (
                          '"'
                        | { $type = INVALID; }
                    )
                ;

// -------------
// Identifier.  Identifier tokens pick up properties names and values
//
// $ANTLR src "css21.g" 566
IDENT           : '-'? NMSTART NMCHAR*  ;

// -------------
// Reference.   Reference to an element in the body we are styling, such as <XXXX id="reference">
//
// $ANTLR src "css21.g" 571
HASH            : '#' NAME              ;

// $ANTLR src "css21.g" 573
IMPORT_SYM      : '@' I M P O R T       ;
// $ANTLR src "css21.g" 574
PAGE_SYM        : '@' P A G E           ;
// $ANTLR src "css21.g" 575
MEDIA_SYM       : '@' M E D I A         ;
// $ANTLR src "css21.g" 576
CHARSET_SYM     : '@charset '           ;

// $ANTLR src "css21.g" 578
IMPORTANT_SYM   : '!' (WS|COMMENT)* I M P O R T A N T   ;

// ---------
// Numbers. Numbers can be followed by pre-known units or unknown units
//          as well as '%' it is a precentage. Whitespace cannot be between
//          the numebr and teh unit or percent. Hence we scan any numeric, then
//          if we detect one of the lexical sequences for unit tokens, we change
//          the lexical type dynamically.
//
//          Here we first define the various tokens, then we implement the
//          number parsing rule.
//
// $ANTLR src "css21.g" 590
fragment    EMS         :;  // 'em'
// $ANTLR src "css21.g" 591
fragment    EXS         :;  // 'ex'
// $ANTLR src "css21.g" 592
fragment    LENGTH      :;  // 'px'. 'cm', 'mm', 'in'. 'pt', 'pc'
// $ANTLR src "css21.g" 593
fragment    ANGLE       :;  // 'deg', 'rad', 'grad'
// $ANTLR src "css21.g" 594
fragment    TIME        :;  // 'ms', 's'
// $ANTLR src "css21.g" 595
fragment    FREQ        :;  // 'khz', 'hz'
// $ANTLR src "css21.g" 596
fragment    DIMENSION   :;  // nnn'Somethingnotyetinvented'
// $ANTLR src "css21.g" 597
fragment    PERCENTAGE  :;  // '%'

// $ANTLR src "css21.g" 599
NUMBER
    :   (
              '0'..'9' ('.' '0'..'9'+)?
            | '.' '0'..'9'+
        )
        (
              (E (M|X))=>
                E
                (
                      M     { $type = EMS;          }
                    | X     { $type = EXS;          }
                )
            | (P(X|T|C))=>
                P
                (
                      X     
                    | T
                    | C
                )
                            { $type = LENGTH;       }   
            | (C M)=>
                C M         { $type = LENGTH;       }
            | (M (M|S))=> 
                M
                (
                      M     { $type = LENGTH;       }
            
                    | S     { $type = TIME;         }
                )
            | (I N)=>
                I N         { $type = LENGTH;       }
            
            | (D E G)=>
                D E G       { $type = ANGLE;        }
            | (R A D)=>
                R A D       { $type = ANGLE;        }
            
            | (S)=>S        { $type = TIME;         }
                
            | (K? H Z)=>
                K? H    Z   { $type = FREQ;         }
            
            | IDENT         { $type = DIMENSION;    }
            
            | '%'           { $type = PERCENTAGE;   }
            
            | // Just a number
        )
    ;

// ------------
// url and uri.
//
// $ANTLR src "css21.g" 652
URI :   U R L
        '('
            ((WS)=>WS)? (URL|STRING) WS?
        ')'
    ;

// -------------
// Whitespace.  Though the W3 standard shows a Yacc/Lex style parser and lexer
//              that process the whitespace within the parser, ANTLR does not
//              need to deal with the whitespace directly in the parser.
//
// $ANTLR src "css21.g" 663
WS      : (' '|'\t')+           { $channel = HIDDEN#;    }   ;
// $ANTLR src "css21.g" 664
NL      : ('\r' '\n'? | '\n')   { $channel = HIDDEN#;    }   ;


// -------------
//  Illegal.    Any other character shoudl not be allowed.
//

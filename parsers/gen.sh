#!/bin/sh

#java -classpath .:$HOME/bin/antlr-3.1.1.jar org.antlr.Tool Java.g 
#java -classpath .:$HOME/bin/antlr-3.0.1.jar:$HOME/bin/antlr-runtime-3.0.1.jar:$HOME/bin/stringtemplate-3.1b1.jar org.antlr.Tool css21.g
java -classpath .:$HOME/bin/antlr-3.4-complete.jar org.antlr.Tool css21.g


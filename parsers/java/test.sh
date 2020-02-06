#!/bin/sh

#javac -cp .:$HOME/bin/antlr-3.1.1.jar -source 5.0 Main.java 
javac -cp .:$HOME/bin/antlr-3.4-complete.jar Main.java 
java -classpath .:$HOME/bin/antlr-3.4-complete.jar Main test.css
#rm *.class


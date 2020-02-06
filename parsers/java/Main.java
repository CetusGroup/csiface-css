import org.antlr.runtime.*;
import org.antlr.runtime.tree.*;

public class Main {
	public static void main(String[] args) throws Exception {
		CharStream input = new ANTLRFileStream(args[0]);
		css21Lexer lex = new css21Lexer(input);
		CommonTokenStream tokens = new CommonTokenStream(lex);
		css21Parser parser = new css21Parser(tokens);
		parser.styleSheet();
	}
}

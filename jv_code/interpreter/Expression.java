package interpreter;

// https://www.tutorialspoint.com/design_pattern/interpreter_pattern.htm


// Create an expression interface.
public interface Expression {
   public boolean interpret(String context);
}

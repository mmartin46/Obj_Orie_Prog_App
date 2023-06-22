package interpreter;

// Create concrete classes implementing the expression
// interface.
public class TerminalExpression implements Expression {
   
   private String data;

   public TerminalExpression(String data) {
      this.data = data;  
   }

   @Override
   public boolean interpret(String context) {

      if (context.contains(data)) {
         return true;
      }
      return false;
   }
}

package interpreter;

public class IntepreterPatternDemo {
   
   // Rule: Josh amd John are mael
   public static Expression getMaleExpression() {
      Expression josh = new TerminalExpression("Robert");
      Expression john = new TerminalExpression("John");
      return new OrExpression(josh, john);      
   }

   // Rule: Marlie is a married woman
   public static Expression getMarriedWomanExpression() {
      Expression marlie = new TerminalExpression("Marlie");
      Expression married = new TerminalExpression("Married");
      return new AndExpression(marlie, married);
   }

   public static void main(String[] args) {
      Expression isMale = getMaleExpression();
      Expression isMarriedWoman = getMarriedWomanExpression();

      System.out.println("Josh is male? " + isMale.interpret("Josh"))
      System.out.println("Marlie is a married woman? " + isMarriedWoman.interpret("Married Woman"));
   }
}

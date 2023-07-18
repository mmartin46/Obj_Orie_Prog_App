package iterator;

public class IteratorPatternDemo {
   public static void main(String[] args) {
      CollectionOfNames cmpnyRegistry = new CollectionOfNames();

      for (Iterator iter = cmpnyRegistry.getIterator(); iter.hasNext();) {
         String name = (String) iter.next();
         System.out.println("Name: " + name);
      }
   }   
}

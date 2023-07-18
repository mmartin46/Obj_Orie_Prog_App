package iterator;

// Create a CollectionofNames class that will
// implement Container interface.
public class CollectionOfNames implements Container {
   public String name[] = {
      "James",
      "Jackson"
   };

   @Override
   public Iterator getIterator() {
      return new CollectionOfNamesIterate();
   }

   private class CollectionOfNamesIterate implements Iterator {
      int i;

      @Override
      public boolean hasNext() {
         if (i < name.length) {
            return true;
         }
         return false;
      }

      @Override
      public Object next() {
         if (this.hasNext()) {
            return name[i++];
         }
         return null;
      }
   }
}

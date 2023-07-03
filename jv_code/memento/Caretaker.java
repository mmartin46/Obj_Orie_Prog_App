package memento;

import java.util.ArrayList;
import java.util.List;

// Create a Caretaker class that will
// responsible for keeping the Memento.
public class Caretaker {
   
   private List<Memento> mementoList = new ArrayList<Memento>();

   public void add(Memento state) {
      mementoList.add(state);
   }

   public Memento get(int index) {
      return mementoList.get(index);
   }
}


package memento;

public class MementoPatternDemo {
   public static void main(String[] args) {
      Originator originator = new Originator();
      Caretaker careTaker = new Caretaker();

      originator.setState("State #1");
      careTaker.add(originator.saveStateToMemento());

      originator.setState("State #2");
      careTaker.add(originator.saveStateToMemento());
      originator.setState("State #3");

      System.out.println("Current State: " + originator.getState());
      originator.getStateFromMemeto(careTaker.get(0));
      System.out.println("First saved State: " + originator.getState());
      originator.getStateFromMemeto(careTaker.get(1));
   } 
   
}

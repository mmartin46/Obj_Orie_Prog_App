package memento;

// Create an Originator class
// that will use Memento object to restore its
// previous state.
public class Originator {
   
   private String state;

   public void setState(String state) {
      this.state = state;
   }

   public String getState() {
      return state;
   }

   public Memento saveStateToMemento() {
      return new Memento(state);
   }

   public void getStateFromMemeto(Memento Memento) {
      state = Memento.getState();
   }
}

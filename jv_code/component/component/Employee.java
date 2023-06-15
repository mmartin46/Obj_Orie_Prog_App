// Component
// Defines the interface for objects in composition.
// Implements default behavior for the interface common to all classes
// as appropriate.

// Leaf
// Represents leaf objects in composition. A leaf has no children.
// Defines behavior for primitive objecs in the composition.

// Composite
// Defines behavior for components having children.
// Stores child component.
package component;
// Implements child related operations in the component interface.

// Client
// Manipulates objects in the composition through the
// component interface.

public interface Employee {
   public int getId();
   public String getName();
   public double getSalary();
   public void print();
   public void add(Employee employee);
   public void remove(Employee employee);
   public Employee getChild(int i);
}

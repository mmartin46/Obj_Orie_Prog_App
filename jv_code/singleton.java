class Singleton {

}
/* 
Early Intialization: creation of instance at load time.
Lazy Instantitation: creation of instance when required.

To create the singleton class we need to have a static member
of the class, a private constructor, and a static factory method.

Static Member: It gets memory only once because it's static,
               containing the instance of the static class.
Private Constructor: It prevents instantiation from the singleton class 
               outside the class.
Static Factory method: It provides the global point of access to the 
*/


// Easily Instantiation
// We create the instance of the class at the time of
// declaring the static data member, so instance
// of the class is created at the time of classloading.
class A {
   private static A obj = new A();
   private A() {}

   public static A getA() {
      return obj;
   }

   public void someFunction() {
      // Insert code
   }
}

// Lazy Instatiation
// We create the instance of the class in synchronized method or
// synchronized block, so instance of the class is created
// when required.
class B {
   private static B obj;
   private B() {}

   public static B getB() {
      if (obj == null) {
         synchronized (Singleton.class) {
            if (obj == null) {
               obj = new Singleton();
            }
         }
      }
      return obj;
   }

   public void someFunction() {
      // Insert code
   }
}
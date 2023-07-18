


// Create a RealInternetAccess class that will implement
// OfficeInternetAccess interface for granting the permission
// for the specific employee.
public class RealInternetAccess implements OfficeInternetAccess{
   private String emloyeeName;
   public RealInternetAccess(String empName) {
      this.emloyeeName = empName;
   }

   @Override
   public void grantInternetAccess() {
      System.out.println("Internet Access granted for employee: " + emloyeeName);
   }
}

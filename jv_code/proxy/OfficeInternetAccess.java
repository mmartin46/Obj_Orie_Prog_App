
/*
Virtual Proxy 
Use a proxy pattern which would create multiple proxies and point to the
huge memory consuming object for further processing.
The real objects gets created only when a client requests/accesses the 
object.

Protective Proxy
Acts as an authorization layer to verify whether the actual user
has access to the appropriate content or not.

Remote Proxy
Provides a local representation of the object present
in the different address location. (RPC call)

Smart Proxy
Provides an additional layer of security by interposing
specific actions when the object is accessed.

*/


// Create an OfficeInernetAcess Interface
public interface OfficeInternetAccess {
   public void grantInternetAccess();
}


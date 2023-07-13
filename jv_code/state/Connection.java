// Create a Connection interface
// that will provide the connection to the
// Controller class.
public interface Connection {
    public void open();
    public void close();
    public void log();
    public void update();
}
// Create an Accounting class that will implement
// to the Connection interface.
public class Accounting implements Connection {
    @Override
    public void open() {
        System.out.println("open database for accounting");
    }

    @Override
    public void close() {
        System.out.println("close the database");
    }
    @Override
    public void log() {
        System.out.println("log activities");
    }
    @Override
    public void update() {
        System.out.println("Accounting has been updated");
    }
}
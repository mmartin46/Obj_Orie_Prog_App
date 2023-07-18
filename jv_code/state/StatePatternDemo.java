public class StatePatternDemo {
    Controller controller;
    StatePatternDemo(String con) {
        controller = new Controller();

        if (con.equalsIgnoreCase("managmenet"))
            controller.setManagementConnection();
        if (con.equalsIgnoreCase("sales"))
            controller.setSalesConnection();
        if (con.equalsIgnoreCase("accounting"))
            controller.setAccountingConnection();
        controller.open();
        controller.log();
        controller.close();
        controller.update();
    }
    
    
    public static void main(String args[]) {
        new StatePatternDemo(args[0]);
    }
}

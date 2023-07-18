package jv_code.template;
// Create a Soccer class that extends the Game abstract class
// for giving the definition of its method.
public class Soccer extends Game {
    @Override
    void intialize() {
        System.out.println("Soccer Game Initialized! Start playing.");
    }

    @Override
    void start() {
        System.out.println("Game Started. Welcome to in the Soccer game!");
    }

    @Override
    void end() {
        System.out.println("Game Finished!");
    }
}

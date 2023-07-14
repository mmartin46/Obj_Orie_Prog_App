package jv_code.template;

// Create a Chess class that will extend
// Game abstract class for giving the definition to
// its method.
public class Chess extends Game {
    @Override
    void intialize() {
        System.out.println("Chess Game Intialized! Start playing.");
    }    

    @Override
    void start() {
        System.out.println("Game Started. Welcome to in the chess game!");
    }

    @Override
    void end() {
        System.out.println("Game Finished!");
    }
}

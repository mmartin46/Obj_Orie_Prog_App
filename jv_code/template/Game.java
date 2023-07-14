package jv_code.template;

// Create a Game abstract class
public abstract class Game {
    abstract void intialize();
    abstract void start();
    abstract void end();

    public final void play() {
        intialize();
        start();
        end();
    }
}
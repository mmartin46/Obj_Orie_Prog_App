package strategy;

// Create a Addition class that will implement
// Strategy interface.
public class Addition implements Strategy {
    
    @Override
    public float calculation(float a, float b) {
        return a + b;
    }
}

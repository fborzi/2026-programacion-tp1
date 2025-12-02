package edu.programacionImpl;

import edu.programacion.Calculator;
import org.junit.jupiter.api.Test;

class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void testAdd() {
        assert calculator.add(2.0, 3.0).equals(5.0);
    }

    @Test
    void testSubtract() {
        assert calculator.subtract(5.0, 3.0).equals(2.0);
    }

    @Test
    void testMultiply() {
        assert calculator.multiply(2.0, 3.0).equals(6.0);
    }

    @Test
    void testDivide() {
        assert calculator.divide(6.0, 3.0).equals(2.0);
    }

    @Test
    void testDivideByZero() {
        try {
            calculator.divide(6.0, 0.0);
            assert false; // Should not reach here
        } catch (ArithmeticException e) {
            assert true; // Expected exception
        }
    }
}


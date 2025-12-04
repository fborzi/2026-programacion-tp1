package edu.programacionImpl;

import edu.programacion.calculator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class CalculatorTest {
    private final calculator calculator = new calculator();

    @Test
    void testAdd() {
        assertEquals(5.0, calculator.add(2.0, 3.0));
    }

    @Test
    void testSubtract() {
        assertEquals(2.0, calculator.sub_tract(5.0, 3.0));
    }

    @Test
    void testMultiply() {
        assertEquals(6.0, calculator.multiply(2.0, 3.0));
    }

    @Test
    void testDivide() {
        assertEquals(2.0, calculator.divide(6.0, 3.0));
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


package edu.programacion;

public class Calculator {
    private Double memory;

    public Calculator() {
        this.memory = 0.0;
    }

    public Double add(Double a, Double b) {
        return a + b;
    }

    public Double subtract(Double a, Double b) {
        return a - b;
    }

    public Double multiply(Double a, Double b) {
        return a * b;
    }

    public Double divide(Double a, Double b) {
        return a / b;
    }
}

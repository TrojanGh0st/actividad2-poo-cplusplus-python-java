// Clase CuentaBancaria: Representa una cuenta bancaria con atributos como saldo y número de cuenta, y métodos get y set para cada atributo. 

public class CuentaBancaria { 

    // Atributos 

    private double saldo; 

    private String numeroCuenta; 

 

    // Constructor 

    public CuentaBancaria(double saldo, String numeroCuenta) { 

        this.saldo = saldo; 

        this.numeroCuenta = numeroCuenta; 

    } 

 

    // Métodos get para cada atributo 

    public double getSaldo() { // Obtener saldo 

        return saldo; 

    } 

 

    public String getNumeroCuenta() { // Obtener número de cuenta 

        return numeroCuenta; 

    } 

 

    // Métodos set para cada atributo 

    public void setSaldo(double saldo) { // Establecer saldo 

        this.saldo = saldo; 

    } 

 

    public void setNumeroCuenta(String numeroCuenta) { // Establecer número de cuenta 

        this.numeroCuenta = numeroCuenta; 

    } 

 

    // Método main para probar la clase 

    public static void main(String[] args) { 

        // Objetos 

        CuentaBancaria cuenta1 = new CuentaBancaria(1000, "1234567890"); 

        CuentaBancaria cuenta2 = new CuentaBancaria(5000, "0987654321"); 

 

        // Actualizar información utilizando métodos set 

        cuenta1.setSaldo(1500); 

        cuenta2.setNumeroCuenta("9876543210"); 

 

        // Recuperar información utilizando métodos get 

        System.out.println(cuenta1.getSaldo() + " " + cuenta1.getNumeroCuenta()); 

        System.out.println(cuenta2.getSaldo() + " " + cuenta2.getNumeroCuenta()); 

    } 

} 

 

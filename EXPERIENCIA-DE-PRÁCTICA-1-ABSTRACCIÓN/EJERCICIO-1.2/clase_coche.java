// Clase Coche: Representa un coche con atributos como modelo, año y velocidad, y métodos para interactuar con el coche. 

public class Coche { 

    // Atributos 

    private String modelo; 

    private int año; 

    private int velocidad; 

 

    // Constructor 

    public Coche(String modelo, int año, int velocidad) { 

        this.modelo = modelo; 

        this.año = año; 

        this.velocidad = velocidad; 

    } 

 

    // Métodos para acceder a los atributos 

    public String getModelo() { // Modelo del coche 

        return modelo; 

    } 

 

    public int getAño() { // Año del coche 

        return año; 

    } 

 

    public int getVelocidad() { // Velocidad actual del coche 

        return velocidad; 

    } 

 

    // Método para acelerar el coche 

    public void acelerar() { 

        velocidad += 1; // Aumenta la velocidad en 1 km/h 

        System.out.println(modelo + " ha acelerado. Velocidad actual: " + velocidad + " km/h"); 

    } 

 

    // Método para frenar el coche 

    public void frenar() { 

        if (velocidad >= 80) { 

            velocidad -= 10; // Disminuye la velocidad en 10 km/h 

            System.out.println(modelo + " ha frenado. Nueva velocidad: " + velocidad + " km/h"); 

        } else { 

            System.out.println(modelo + " siga, tiene una velocidad adecuada. Velocidad actual: " + velocidad + " km/h"); 

        } 

    } 

 

    // Método main para probar la clase 

    public static void main(String[] args) { 

        // Creación de diferentes objetos para representar diferentes coches 

        Coche coche1 = new Coche("Toyota Corolla", 2020, 60); 

        Coche coche2 = new Coche("Ford Mustang", 2018, 120); 

        Coche coche3 = new Coche("Tesla Model S", 2022, 100); 

 

        // Interacción 

        coche1.acelerar(); 

        coche1.frenar(); 

 

        coche2.acelerar(); 

        coche2.frenar(); 

 

        coche3.acelerar(); 

        coche3.frenar(); 

    } 

} 

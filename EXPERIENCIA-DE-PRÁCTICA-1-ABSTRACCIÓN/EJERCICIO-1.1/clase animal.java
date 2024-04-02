// Clase Animal: Representa a un animal con atributos como nombre, edad y tipo, y métodos para interactuar con el animal. 

public class Animal { 

    // Atributos 

    private String nombre; 

    private int edad; 

    private String tipo; 

 

    // Constructor 

    public Animal(String nombre, int edad, String tipo) { 

        this.nombre = nombre; 

        this.edad = edad; 

        this.tipo = tipo; 

    } 

 

    // Métodos para acceder a los atributos 

    public String getNombre() { 

        return nombre; 

    } 

 

    public int getEdad() { 

        return edad; 

    } 

 

    public String getTipo() { 

        return tipo; 

    } 

 

    // Método para alimentar al animal 

    public void alimentarAnimal() { 

        System.out.println(nombre + " fue alimentado."); 

    } 

 

    // Método para hacer sonidos 

    public void hacerSonidoAnimal() { 

        switch (tipo) { 

            case "perro": 

                System.out.println("¡Guau!"); 

                break; 

            case "gato": 

                System.out.println("¡Miau!"); 

                break; 

            case "oveja": 

                System.out.println("¡Beee!"); 

                break; 

            default: 

                System.out.println("No está en la lista."); 

        } 

    } 

 

    // Método main para probar la clase 

    public static void main(String[] args) { 

        // Creación de diferentes objetos para representar diferentes animales 

        Animal perro = new Animal("Chimuelo", 2, "perro"); 

        Animal gato = new Animal("Tarzán", 3, "gato"); 

        Animal oveja = new Animal("Dolly", 1, "oveja"); 

 

        // Interacción 

        perro.alimentarAnimal(); 

        perro.hacerSonidoAnimal(); 

 

        gato.alimentarAnimal(); 

        gato.hacerSonidoAnimal(); 

 

        oveja.alimentarAnimal(); 

        oveja.hacerSonidoAnimal(); 

    } 

} 

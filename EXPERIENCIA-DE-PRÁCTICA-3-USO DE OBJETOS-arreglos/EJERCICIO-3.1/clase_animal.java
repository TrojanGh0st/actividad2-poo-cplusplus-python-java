public class Animal { 

    // Atributos 

    private String nombre; 

    private int edad; 

    private String tipo; 

 

    // Métodos set para cada atributo 

    public void setNombre(String _nombre) { 

        nombre = _nombre; 

    } 

 

    public void setEdad(int _edad) { 

        edad = _edad; 

    } 

 

    public void setTipo(String _tipo) { 

        tipo = _tipo; 

    } 

 

    // Métodos get para cada atributo 

    public String getNombre() { 

        return nombre; 

    } 

 

    public int getEdad() { 

        return edad; 

    } 

 

    public String getTipo() { 

        return tipo; 

    } 

 

    public static void main(String[] args) { 

        Animal perro = new Animal(); 

        Animal gato = new Animal(); 

 

        perro.setNombre("Platano"); // nombre del perro 

        perro.setEdad(5); // edad del perro 

        perro.setTipo("Perro"); // tipo del perro 

 

        gato.setNombre("Tiburon"); // nombre del gato 

        gato.setEdad(3); // edad del gato 

        gato.setTipo("Gato"); // tipo del gato 

 

        System.out.println("\tMASCOTA 1:"); // información sobre el perro 

        System.out.println("Nombre---> " + perro.getNombre() + "\nEdad ---> " + perro.getEdad() + "\nTipo---> " + perro.getTipo()); 

 

        System.out.println("\tMASCOTA 2:"); // información sobre el gato 

        System.out.println("Nombre---> " + gato.getNombre() + "\nEdad ---> " + gato.getEdad() + "\nTipo---> " + gato.getTipo()); 

    } 

} 

// Clase Persona: Representa a una persona con atributos como nombre, edad y género, y métodos get y set para cada atributo. 

public class Persona { 

    // Atributos 

    private String nombre; 

    private int edad; 

    private String genero; 

 

    // Constructor 

    public Persona(String nombre, int edad, String genero) { 

        this.nombre = nombre; 

        this.edad = edad; 

        this.genero = genero; 

    } 

 

    // Métodos get para cada atributo 

    public String getNombre() { // Obtener nombre 

        return nombre; 

    } 

 

    public int getEdad() { // Obtener edad 

        return edad; 

    } 

 

    public String getGenero() { // Obtener género 

        return genero; 

    } 

 

    // Métodos set para cada atributo 

    public void setNombre(String nombre) { // Establecer nombre 

        this.nombre = nombre; 

    } 

    public void setEdad(int edad) { // Establecer edad 

        this.edad = edad; 

    } 

 

    public void setGenero(String genero) { // Establecer género 

        this.genero = genero; 

    } 

 

    // Método main para probar la clase 

    public static void main(String[] args) { 

        // Objetos 

        Persona persona1 = new Persona("Juan", 25, "Masculino"); 

        Persona persona2 = new Persona("María", 30, "Femenino"); 

 

        // Actualizar información utilizando métodos set 

        persona1.setEdad(26); 

        persona2.setGenero("Femenina"); 

 

        // Recuperar información utilizando métodos get 

        System.out.println(persona1.getNombre() + " " + persona1.getEdad() + " " + persona1.getGenero()); 

        System.out.println(persona2.getNombre() + " " + persona2.getEdad() + " " + persona2.getGenero()); 

    } 

}     

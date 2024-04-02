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

        final int TAM = 3; // Tamaño del arreglo 

        Animal[] animales = new Animal[TAM]; // Arreglo de objetos de la clase Animal 

 

        animales[0] = new Animal(); 

        animales[0].setNombre("Platano"); 

        animales[0].setEdad(7); 

        animales[0].setTipo("Perro"); 

 

        animales[1] = new Animal(); 

        animales[1].setNombre("Peruanoxd"); 

        animales[1].setEdad(1); 

        animales[1].setTipo("Gato"); 

 

        animales[2] = new Animal(); 

        animales[2].setNombre("Cuy"); 

        animales[2].setEdad(3); 

        animales[2].setTipo("Hamster"); 

 

        // Ciclo para recorrer y manipular los objetos en el arreglo 

        System.out.println("Información de los animales en el arreglo:"); 

        for (int i = 0; i < TAM; ++i) { 

            System.out.println("\tAnimal " + (i + 1)); 

            System.out.println("Nombre---> " + animales 

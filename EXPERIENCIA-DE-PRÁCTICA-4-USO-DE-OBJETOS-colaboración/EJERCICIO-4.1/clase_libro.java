class Libro { 

    // Atributos 

    private String titulo; 

    private String autor; 

    private boolean prestado; 

 

    // Métodos set para cada atributo 

    public void setTitulo(String _titulo) { 

        titulo = _titulo; 

    } 

 

    public void setAutor(String _autor) { 

        autor = _autor; 

    } 

 

    // Método para prestar el libro 

    public void prestar() { 

        prestado = true; 

    } 

 

    // Método para devolver el libro 

    public void devolver() { 

        prestado = false; 

    } 

 

    // Métodos get para cada atributo 

    public String getTitulo() { 

        return titulo; 

    } 

 

    public String getAutor() { 

        return autor; 

    } 

 

    // Método para verificar si el libro está prestado 

    public boolean estaPrestado() { 

        return prestado; 

    } 

} 

 

class Biblioteca { 

    // Método para prestar un libro de la biblioteca 

    public void prestarLibro(Libro libro) { 

        if (!libro.estaPrestado()) { 

            libro.prestar(); 

            System.out.println("El libro \"" + libro.getTitulo() + "\" ha sido prestado."); 

        } else { 

            System.out.println("El libro \"" + libro.getTitulo() + "\" ya está prestado."); 

        } 

    } 

 

    // Método para devolver un libro a la biblioteca 

    public void devolverLibro(Libro libro) { 

        if (libro.estaPrestado()) { 

            libro.devolver(); 

            System.out.println("El libro \"" + libro.getTitulo() + "\" ha sido devuelto."); 

        } else { 

            System.out.println("El libro \"" + libro.getTitulo() + "\" no estaba prestado."); 

        } 

    } 

} 

 

public class Main { 

    public static void main(String[] args) { 

        Libro libro1 = new Libro(); 

        Libro libro2 = new Libro(); 

 

        // Atributos para el libro 1 

        libro1.setTitulo("El Banquete"); 

        libro1.setAutor("Platon"); 

 

        // Atributos para el libro 2 

        libro2.setTitulo("Ética a Nicómaco"); 

        libro2.setAutor("Aristóteles"); 

 

        // Objeto de la clase Biblioteca 

        Biblioteca biblioteca = new Biblioteca(); 

 

        // Prestar un libro de la biblioteca 

        biblioteca.prestarLibro(libro1); 

        biblioteca.prestarLibro(libro2); 

 

        // Devolver un libro a la biblioteca 

        biblioteca.devolverLibro(libro1); 

        biblioteca.devolverLibro(libro2); 

    } 

} 

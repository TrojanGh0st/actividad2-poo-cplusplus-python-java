import java.util.ArrayList; 

import java.util.List; 

 

// Clase Producto: Representa un producto con atributos como nombre, precio y cantidad. 

class Producto { 

    // Atributos 

    private String nombre; 

    private double precio; 

    private int cantidad; 

 

    // Constructor 

    public Producto(String nombre, double precio, int cantidad) { 

        this.nombre = nombre; 

        this.precio = precio; 

        this.cantidad = cantidad; 

    } 

 

    // Métodos set para precio y cantidad 

    public void setPrecio(double precio) { 

        this.precio = precio; 

    } 

 

    public void setCantidad(int cantidad) { 

        this.cantidad = cantidad; 

    } 

 

    // Getters para obtener el nombre, precio y cantidad del producto 

    public String getNombre() { 

        return nombre; 

    } 

 

    public double getPrecio() { 

        return precio; 

    } 

 

    public int getCantidad() { 

        return cantidad; 

    } 

} 

 

// Clase Factura: Representa una factura con un método para agregar productos. 

class Factura { 

    // Lista de productos 

    private List<Producto> productos; 

 

    // Constructor 

    public Factura() { 

        this.productos = new ArrayList<>(); 

    } 

 

    // Método para agregar un producto a la factura 

    public void agregarProducto(Producto producto) { 

        productos.add(producto); 

    } 

 

    // Método para calcular el total de la factura 

    public double calcularTotal() { 

        double total = 0; 

        for (Producto producto : productos) { 

            total += producto.getPrecio() * producto.getCantidad(); 

        } 

        return total; 

    } 

} 

 

public class Main { 

    public static void main(String[] args) { 

        // Crear algunos productos 

        Producto producto1 = new Producto("Producto 1", 10.0, 2); 

        Producto producto2 = new Producto("Producto 2", 20.0, 1); 

 

        // Crear una factura y agregar productos 

        Factura factura = new Factura(); 

        factura.agregarProducto(producto1); 

        factura.agregarProducto(producto2); 

 

        // Calcular el total de la factura 

        double totalFactura = factura.calcularTotal(); 

        System.out.println("Total de la factura: $" + totalFactura); 

    } 

} 

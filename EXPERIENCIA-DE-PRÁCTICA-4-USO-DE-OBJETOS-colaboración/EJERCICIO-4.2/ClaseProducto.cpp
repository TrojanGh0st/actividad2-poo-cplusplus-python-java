#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Producto {
private:
    string nombre;
    double precio;
    int cantidad;

public:

    // nombre del producto
    void setNombre(string _nombre) {
        nombre = _nombre;
    }

    // precio del producto
    void setPrecio(double _precio) {
        precio = _precio;
    }

    // cantidad del producto
    void setCantidad(int _cantidad) {
        cantidad = _cantidad;
    }


    // obtener el nombre del producto
    string getNombre() const {
        return nombre;
    }

    // obtener el precio del producto
    double getPrecio() const {
        return precio;
    }

    // la cantidad del producto
    int getCantidad() const {
        return cantidad;
    }
};

class Factura {
private:
    vector<Producto> productos;

public:
    // agregar un producto a la factura
    void agregarProducto(Producto &producto) {
        productos.push_back(producto);
    }

    // mostrar los detalles de la factura
    void mostrarDetalles() {
        cout << "Detalles de la Factura:" << endl;
        double total = 0.0;
        for (const auto &producto : productos) {
        cout << "\tProducto" << producto.getNombre() << "\nPrecio: S/" << producto.getPrecio() << "\nCantidad: " << producto.getCantidad() << endl;
            total += producto.getPrecio() * producto.getCantidad();
        }
        cout << "Total: S/" << total << endl;
    }
};

int main() {
    Producto producto1, producto2;

    // atributos para el producto 1
    producto1.setNombre("Azucar");
    producto1.setPrecio(10.60);
    producto1.setCantidad(2);

    // atributos para el producto 2
    producto2.setNombre("Pan");
    producto2.setPrecio(2);
    producto2.setCantidad(8);

    Factura factura;

    // Agregar productos a la factura
    factura.agregarProducto(producto1);
    factura.agregarProducto(producto2);

    // Mostrar los detalles de la factura
    factura.mostrarDetalles();

    return 0;
}

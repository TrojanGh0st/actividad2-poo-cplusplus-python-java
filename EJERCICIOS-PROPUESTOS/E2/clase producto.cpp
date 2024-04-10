#include <iostream>
#include <vector>
#include <string>
using namespace std;
// Definición de la clase Producto
class Producto {
private:
string nombre;
int cantidadDisponible;
public:
// Constructor
Producto(string _nombre = "", int _cantidad = 0) : nombre(_nombre),
cantidadDisponible(_cantidad) {}
// Métodos para establecer los valores de los atributos
void setNombre(string _nombre) {
nombre = _nombre;
}
void setCantidadDisponible(int _cantidad) {
cantidadDisponible = _cantidad;
}
// Métodos para obtener los valores de los atributos
string getNombre() const {
return nombre;
}
int getCantidadDisponible() const {
return cantidadDisponible;
}
};
// Definición de la clase Inventario
class Inventario {
private:
vector<Producto> productosDisponibles;
vector<Producto> productosAgotados;
public:
// Método para agregar un producto al inventario
void agregarProducto(Producto producto) {
productosDisponibles.push_back(producto);
}
// Método para realizar un pedido de un producto
void realizarPedido(string nombreProducto, int cantidad) {
for (auto& producto : productosDisponibles) {
if (producto.getNombre() == nombreProducto) {
if (producto.getCantidadDisponible() >= cantidad) {
producto.setCantidadDisponible(producto.getCantidadDisponible() -
cantidad);
cout << "Pedido de " << cantidad << " " << nombreProducto << "(s)
realizado con éxito." << endl;
return;
} else {
cout << "No hay suficientes " << nombreProducto << "(s)
disponibles para realizar el pedido." << endl;
return;
}
}
}
cout << "El producto " << nombreProducto << " no está disponible en el
inventario." << endl;
}
// Método para actualizar la lista de productos agotados
void actualizarProductosAgotados() {
productosAgotados.clear();
for (const auto& producto : productosDisponibles) {
if (producto.getCantidadDisponible() == 0) {
productosAgotados.push_back(producto);
}
}
}
};
int main() {
// Crear inventario
Inventario inventario;
// Agregar productos al inventario
Producto producto1("Manzanas", 50);
Producto producto2("Plátanos", 0);
Producto producto3("Peras", 20);
inventario.agregarProducto(producto1);
inventario.agregarProducto(producto2);
inventario.agregarProducto(producto3);
// Realizar pedidos
inventario.realizarPedido("Manzanas", 10);
inventario.realizarPedido("Peras", 30);
inventario.realizarPedido("Plátanos", 5);
// Actualizar lista de productos agotados
inventario.actualizarProductosAgotados();
return 0;
}

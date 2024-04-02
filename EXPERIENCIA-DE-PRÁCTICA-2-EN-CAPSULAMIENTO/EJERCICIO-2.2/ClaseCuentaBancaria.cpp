#include <iostream>
#include <string>

using namespace std;

// clase CuentaBancaria
class CuentaBancaria {
private:
    double saldo;
    string numeroCuenta;

public:
    // establecer los valores de los atributos
    void setSaldo(double _saldo) // establecer el saldo de la cuenta bancaria
    {
        saldo = _saldo;
    }

    void setNumeroCuenta(string _numeroCuenta) // establecer el número de cuenta bancaria
    {
        numeroCuenta = _numeroCuenta;
    }

    // obtener los valores de los atributos
    double getSaldo() const // obtener el saldo de la cuenta bancaria
    {
        return saldo;
    }

    string getNumeroCuenta() const // obtener el número de cuenta bancaria
    {
        return numeroCuenta;
    }
};

int main() 
{
    CuentaBancaria cuenta1, cuenta2;

    // atributos para la cuenta bancaria 1
    cuenta1.setSaldo(9874.0);
    cuenta1.setNumeroCuenta("123456789");

    // atributos para la cuenta bancaria 2
    cuenta2.setSaldo(5211.0);
    cuenta2.setNumeroCuenta("987654321");

    // información sobre las cuentas bancarias
    cout <<"\tCuenta Bancaria 1:" <<endl; // información sobre la cuenta bancaria 1
    cout << "Saldo: S/" << cuenta1.getSaldo() << "\nNumero de Cuenta---> " << cuenta1.getNumeroCuenta() << endl;

    cout <<"\tCuenta Bancaria 2:" <<endl; // información sobre la cuenta bancaria 2
    cout << "Saldo: S/" << cuenta2.getSaldo() << "\nNumero de Cuenta---> " << cuenta2.getNumeroCuenta() << endl;

    return 0;
}

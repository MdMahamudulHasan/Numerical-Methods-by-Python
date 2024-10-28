#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double f(double x) {
    return 2 * x * x * x - 2 * x - 5;
}

void bijection(double a, double b) {
    double Accuracy = 0.000014;
    double c;

    if (f(a) * f(b) > 0) {
        cout << "No root found in the interval [" << a << ", " << b << "].\n";
        return;
    }

    int i = 0;
    cout << fixed << setprecision(5);
    while (fabs(b - a) > Accuracy) {
        c = (a + b) / 2;

        cout << "Step = " << i + 1
            << "  a = " << a
            << "   f(a) = " << f(a)
            << "   b = " << b
            << "   f(b) = " << f(b)
            << "   c = " << c
            << "   f(c) = " << f(c);

        if (fabs(f(c)) < Accuracy) {
            cout << "\nRoot found: " << c << endl;
            return;
        }

        if (f(c) * f(a) < 0) {
            b = c;
            cout << "   update: b = c" << endl;
        } else {
            a = c;
            cout << "   update: a = c" << endl;
        }

        i++; // Increment step counter
    }

    cout << "\nRoot found: " << c << endl;
}

int main() {
    double a, b;
    cout << "Enter value of a: ";
    cin >> a;

    cout << "Enter value of b: ";
    cin >> b;

    bijection(a, b);
    return 0;
}

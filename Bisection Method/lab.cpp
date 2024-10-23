#include <iostream>
#include <cmath>
using namespace std;

double f(double x) {
    return 2 * x * x * x - 2 * x * x - 5;
}

void bijection(double a, double b) {
    double Accuracy = 0.000014;
    double c;

    if (f(a) * f(b) > 0) {
        cout << "No root found in the interval [" << a << ", " << b << "].\n";
        return;
    }

    
    while (fabs(b - a) > Accuracy) {
        c = (a + b) / 2; 

        if (fabs(f(c)) < Accuracy) {
            cout << "Root found: " << c << endl;
            return;
        }

        if (f(c) * f(a) < 0) { 
            b = c;
        } else {
            a = c;
        }
    }

    cout << "Root found: " << c << endl;
}

int main() {
    double a, b; // Use double for more accurate input
    cout << "Enter value of a: ";
    cin >> a;

    cout << "Enter value of b: ";
    cin >> b;

    bijection(a, b);
    return 0;
}

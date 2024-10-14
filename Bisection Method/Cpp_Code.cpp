#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// Define the function
double f(double x) {
    return x * x * x - x - 1; // Example function: x^3 - x - 1
}

// Implementing Bisection Method
void bisection(double x0, double x1, double e) {
    int step = 0;
    double x2;
    string update;

    cout <<fixed << setprecision(6); // Set precision for output
    cout << "n      x0       f(x0)          x1       f(x1)         x2        f(x2)       Update" << endl;

    // For loop with an arbitrary large number of iterations (acts like a while loop)
    for (step = 1; step < 1000; step++) { // Large number to ensure the loop continues until condition is met
        x2 = (x0 + x1) / 2;

        // Check if the result is within the tolerable error
        if (abs(f(x2)) < e) {
            cout << step << "  " << x0 << "   " << f(x0) << "    " << x1 << "    " << f(x1)
                << "    " << x2 << "    " << f(x2) <<"  \n Root found at x2 = " << x2
                << ", f(x2) = " << f(x2) << endl;
            break;
        }

        // Update either x0 or x1 based on the sign of f(x2)
        if (f(x0) * f(x2) < 0) {
            x1 = x2;
            update = "x1 = x2";
        } else {
            x0 = x2;
            update = "x0 = x2";
        }

        // Print the current iteration results
        cout << step << "  " << x0 << "   " << f(x0) << "    " << x1 << "    " << f(x1)
            << "    " << x2 << "    " << f(x2) << "   " << update << endl;
    }
}

// Driver program
int main() {
    double x0, x1, e;

    // Input initial guesses and tolerable error
    cout << "Enter the first guess (x0): ";
    cin >> x0;
    cout << "Enter the second guess (x1): ";
    cin >> x1;
    cout << "Enter the tolerable error (e): ";
    cin >> e;

    // Ensure that f(x0) * f(x1) < 0
    if (f(x0) * f(x1) >= 0) {
        cout << "The initial guesses do not bracket the root." << endl;
    } else {
        bisection(x0, x1, e);
    }

    return 0;
}


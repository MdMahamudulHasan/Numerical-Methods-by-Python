"""

                                    Bisection Method Algorithm (Step Wise)

            1. start
            2. Define function f(x)
            3. Choose initial or input from user guesses x0 and x1 such that f(x0)f(x1) < 0
            4. Choose pre-specified tolerable error e.
            5. Calculate new approximated root as x2 = (x0 + x1)/2
            6. Calculate f(x0)f(x2)
                        a. if f(x0)f(x2) < 0 then x0 = x0 and x1 = x2
                        b. if f(x0)f(x2) > 0 then x0 = x2 and x1 = x1
                        c. if f(x0)f(x2) = 0 then goto (8)
            7. if |f(x2)| > e then goto (5) otherwise goto (8)
            8. Display x2 as root.
            9. Stop
"""
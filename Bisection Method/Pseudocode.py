"""

                                    Pseudocode for Bisection Method
                                
            1. Start
            
            2. Define function f(x)
            
            3. Input 
                    a. Lower and Upper guesses x0 and x1
                    b. tolerable error e
            
            4. If f(x0)*f(x1) > 0
                    print "Incorrect initial guesses"
                    goto 3
                End If
            
            5. Do 
                    x2 = (x0+x1)/2
                    
                    If f(x0)*f(x2) < 0
                            x1 = x2
                    Else
                        x0 = x2
                    End If
                    
                while abs(f(x2) > e
            
            6. Print root as x2
            
            7. Stop

"""
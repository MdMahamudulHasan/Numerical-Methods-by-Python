"""

    Bisection Method is one of the simplest, reliable, easy to implement and convergence guaranteed method for finding real root of non-linear equations. 
    
    It is also known as Binary Search or Half Interval or Bolzano Method.
    
    
    
    Bisection method is bracketing method and starts with two initial guesses say x0 and x1 such that x0 and x1 brackets the root i.e. f(x0)f(x1)< 0
    
    Bisection method is based on the fact that if f(x) is real and continuous function, and for two initial guesses x0 and x1 brackets the root such that: f(x0)f(x1) < 0 then there exists at least one root between x0 and x1.
    
    
    
    Root is obtained in Bisection method by successive halving the interval i.e. If x0 and x1 are two guesses then we compute new approximated root as:
                    x2 = (x0 + x1)/2
    
    
    Now we have following three different cases:
            1.  If f(x2)=0 then the root is x2.
            2.  If f(x0)f(x2)< 0 then root lies between x0 and x2.
            3.  If f(x0)f(x2)> 0 then root lies between x1 and x2.
            
            or,
            
            1.  If f(x2)=0 then x2 is an exact root,
            2.  else if f(x0)⋅f(x2)<0 then x1=x2,
            3.  else if f(x1)⋅f(x2)<0 then x0=x2,

"""
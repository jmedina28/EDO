import sympy

sympy.init_printing(use_latex='mathjax')

class EDO:
    
    def ec1():
        
        x = sympy.Symbol('x')
        y = sympy.Function('y')
        f = (x**2 + 1)*(y(x)**-1 + 1)
        sol = sympy.dsolve(y(x).diff(x) - f, y(x))
        sympy.pprint(sol)

    def ec2():

        x2 = sympy.symbols('x')
        y2 = sympy.Function('y')
        f2 = (y2(x2)*sympy.log(y2(x2)))/sympy.sin(x2)
        sol2 = sympy.dsolve(y2(x2).diff(x2) - f2, y2(x2)) 
        print("*"*80)
        sympy.pprint(sol2)

    def ec3():
        
        x3 = sympy.symbols('x')
        y3 = sympy.Function('y')
        f3 = y3(x3).diff(x3) - y3(x3)/(x3-2) - 2*(x3-2)**2
        sol3 = sympy.dsolve(f3, y3(x3))
        print("*"*80)
        sympy.pprint(sol3)

    def ec4():
        
        x4 = sympy.symbols('x')
        y4 = sympy.Function('y')
        f4 = 2*x4*(y4(x4).diff(x4)) - y4(x4) - 3*x4**2
        sol4 = sympy.dsolve(f4, y4(x4))
        print("*"*80)
        sympy.pprint(sol4)
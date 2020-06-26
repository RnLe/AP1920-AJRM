import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()
    
    if err_vars == None:
        err_vars = f.free_symbols
        
    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'
        
    return latex(sympy.sqrt(s), symbol_names=latex_names)

I, N, e = sympy.var('I N e')

Z = I/(e*N)

print(Z)
print(error(Z))
print()

N,t=sympy.var('N t')
N_t=N/t
print(N_t)
print(error(N_t))
print()
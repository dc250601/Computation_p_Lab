def regula(guess1, guess2, func):
    """
    regula: A function to find the roots of a function using regula falsi

    args:
    guess1: The first bound for the regula falsi
    guess2: The second bound for the regula falsi
    func: The function for which the roots is to be calculated
    """
    x0 = guess1
    x1 = guess2
    if func(guess1)*func(guess2)>0:
        print("Give another guess")
        print("Exiting...")
    else:
        pass
    while(True):
        x = (x0*func(x1) - x1*func(x0))/(func(x1) - func(x0))
        if func(x1)*func(x)<0:
            x0 = x
        if func(x1)*func(x)>0:
            x1 = x
        if abs(func(x))>1e-6:
            pass
        else:
            return x

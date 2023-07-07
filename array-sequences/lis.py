# Matching patterns without match / case

def evaluate(exp : Expression, env : Environment) -> Any :
    # Evaluate any expression in an environment 

    if isinstance(exp, Symbol):   # Variable reference
        return env[exp]

    elif exp[0] == 'quote':
        (_, x) = exp
        return x

    elif exp[0] == 'if':
        (_. text, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else return evaluate(alternative, env)
    
    elif exp[0] == 'lambda':
        (_, params, *body) = exp
        return Procedure(params, body, env)

    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)

# Each elif clause checks the first item of the list and the unpacks the list

# Example 2 : Pattern matching with match / case


def Evaluate(exp : expression, env : environment) -> Any:
    "Evaluate an expression in an environment"
    match exp : 

        case['quote', x]:
            return x

        case['if', test, consequence, alternative]:
            if Evaluate(test, env):
                return Evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case['lambda', [*params], *body]:
            return Procedure(params, body, env)
        case['define', Symbol() as name, value_exp]:
            env[name] = Evaluate(value_exp, env)
            case _:
                raise SyntaxError(lispstr(exp))


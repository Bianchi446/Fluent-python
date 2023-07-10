# Alternative patterns for lambda

# Lambda expression structure  : (lambda (parms...) body1, body2)

# Case for the lambda case 'lambda'

case ['lambda', parms, body] if body : 



# Making the lambda case safer with nested sequence pattern.

case ['lambda' , [*parms], *body] if body:
    return Procedure(parms, body, env)



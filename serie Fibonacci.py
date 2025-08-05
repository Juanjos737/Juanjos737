#Region serie Fibonacci 

#Sin usar Def, es decir sin funciones 
#Fn = F -1 + F - 2
#F-1 va a ser "a"
#F-2 va a ser "b"
# Fn resultado final 

a, b = 0, 1

#interate es una variable que tendra un comportamiento de incrementar en el ciclo
for i in range (10):
    print (a)
    a, b = b, a + b 

#endregion 
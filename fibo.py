def fibonacci(n):           #Funcion que xera a cadea de Fibonacci
    list_fibo = []          #Lista list_fibo vacía
    a = 0                   #Variable a cun valor inicial de 0
    b = 1                   #Variable b cun valor inicial de 1
    for _ in range(n):      #for repetirase n veces (neste caso 5)
        list_fibo.append(a) #Se introduce a na lista
        b, a = a + b, b
    return list_fibo        #Tras sair do bucle for, a función fibonacci termina devolvendo a lista list_fibo
def echo_funcname(func): #funcao passada com parametro

    def funcao_interna(*args, **kwargs): #função dentro de função é chamada de Nested Functions
        print("Chamando funcao: %s()" % (func.__name__)) #faz alguma lógica
        return func(*args, **kwargs) #executa a função que esta sendo chamada

    return funcao_interna


@echo_funcname
def dobro(x):
    return x * 2

dobro(10)

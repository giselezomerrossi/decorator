import datetime

def calcula_tempo_decorator(funcao):
    def calcula_tempo():
        print(datetime.datetime.now())
        funcao()
        print(datetime.datetime.now())

    return calcula_tempo

@calcula_tempo_decorator
def outra_que_importa():
    for i in range(10000000):
        continue

outra_que_importa()

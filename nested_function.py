def party():
    print("Estou fora")

    def start_party():
        return "Estou dentro"

    def finish_party():
        return "Acabou!"

    print(start_party())
    print(finish_party())

party()

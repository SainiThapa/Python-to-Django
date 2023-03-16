# Replacing 'self' with other strings and making it work
class Man:
    def __init__(saini,age) -> None:
        saini.age=age
    def getInfo(saini):
        print(saini.name)
        print(saini.age)
a=Man(22)
a.name='Saini'
a.getInfo()
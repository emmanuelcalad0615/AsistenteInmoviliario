class Propiedad:

    def __init__(self, id: int, tipo:str, ubicacion: str, valor: str, habitaciones: str, lavados: str, dimension: str, url: str = None):
        self.id: int = id
        self.tipo: str = tipo
        self.ubicacion: str = ubicacion
        self.dimension: str = dimension
        self.valor: str = valor
        self.habitaciones: str = habitaciones
        self.lavados: str = lavados
        self.url: str = url
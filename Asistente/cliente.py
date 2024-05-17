from Asistente.asistente import Asistente
from Asistente.propiedad import Propiedad


class Cliente:
    def __init__(self, nombre: str, asistente: Asistente):

        self.nombre: str = nombre
        self.asistente: Asistente = asistente
        self.propiedades_cliente: list[Propiedad] = []

    def saludar(self) -> str:
        casa = (
            "░░░░░░░░░░░░░░░░▄▓▄░░░\n"
            "░░░░▄█▄░░░░░░░░▄▓▓▓▄░░\n"
            "░░▄█████▄░░░░░▄▓▓▓▓▓▄░\n"
            "░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
            "▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n"
        )
        mensaje = f"Hola, {self.nombre}. Bienvenido a PropietyFinder, estoy a tus servicios."

        return (f"{casa}\n"
                f"{mensaje}")

    def agregar_propiedad(self, tipo: str, ubicacion: str, dimension: str, valor: str, habitaciones: str, lavados: str, url: str = None ):
        id = len(self.propiedades_cliente)
        obj_propiedad = Propiedad(id, tipo, ubicacion, dimension, valor, habitaciones, lavados, url)
        self.propiedades_cliente.append(obj_propiedad)

    def poner_venta(self, id: int):
        _, propiedades_list = self.asistente.mostrar_catalogo()
        self.propiedades_cliente[id].id = len(propiedades_list)
        propiedades_list.append(self.propiedades_cliente[id])




    """def editar_venta(self, id: int, nueva_info: dict ):
        for propiedad in properties:
            if propiedad['id'] == id:
                for key, value in nueva_info.items():
                    if key in propiedad:
                        propiedad[key] = value
                return True
        return False"""



    def mostrar_propiedades_cliente(self) -> tuple[str, list[Propiedad]]:
        propiedades_cliente_str = ""
        for idx, propiedad in enumerate(self.propiedades_cliente, start=1):
            propiedades_cliente_str += f"Propiedad {propiedad.id}:\n"
            propiedades_cliente_str += f"Tipo: {propiedad.tipo if hasattr(propiedad, 'tipo') else 'No disponible'}\n"
            propiedades_cliente_str += f"Ubicación: {propiedad.ubicacion if hasattr(propiedad, 'ubicacion') else 'No disponible'}\n"
            propiedades_cliente_str += f"Valor: {propiedad.valor if hasattr(propiedad, 'valor') else 'No disponible'}\n"
            propiedades_cliente_str += f"Habitaciones: {propiedad.habitaciones if hasattr(propiedad, 'habitaciones') else 'No disponible'}\n"
            propiedades_cliente_str += f"Lavados: {propiedad.lavados if hasattr(propiedad, 'lavados') else 'No disponible'}\n"
            propiedades_cliente_str += f"Dimensión: {propiedad.dimension if hasattr(propiedad, 'dimension') else 'No disponible'}\n"
            propiedades_cliente_str += f"URL: {propiedad.url if hasattr(propiedad, 'url') else 'No disponible'}\n\n"
        return propiedades_cliente_str, self.propiedades_cliente


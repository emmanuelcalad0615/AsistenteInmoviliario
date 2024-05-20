from Asistente.Modelo.asistente import Asistente
from Asistente.Modelo.propiedad import Propiedad


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

    def agregar_propiedad(self, tipo: str, ubicacion: str, dimension: str, valor: str, lavados: str = None, habitaciones: str = None, url: str = None) -> tuple[str, bool]:

        try:
            if not all(param.strip() for param in (tipo, ubicacion, dimension, valor, habitaciones, lavados)):
                raise ValueError("Los parámetros no pueden estar vacíos.")

            id = len(self.propiedades_cliente)
            obj_propiedad = Propiedad(id, tipo, ubicacion, dimension, valor, habitaciones, lavados, url)
            self.propiedades_cliente.append(obj_propiedad)
            return "Propiedad agregada con éxito.", True
        except Exception as e:
            return f"Error al agregar la propiedad: {e}", False

    def poner_venta(self, id_str: str) -> str:
        try:
            if not id_str.strip():
                raise ValueError("Debe ingresar el ID de una de sus propiedades")

            id = int(id_str)

            for  propiedad in self.propiedades_cliente:
                if propiedad.id == id:
                    _, propiedades_list = self.asistente.mostrar_catalogo()
                    propiedad.id = len(propiedades_list)
                    propiedades_list.append(propiedad)
                    del self.propiedades_cliente[id]


                    return "Propiedad agregada con éxito"

            raise ValueError("El ID dado no existe en las propiedades del cliente.")

        except ValueError as ve:
            return str(ve)
        except Exception as e:
            return f"Error inesperado: {e}"

    def editar_propiedad(self, id_str: str, tipo: str = None, ubicacion: str = None, dimension: str = None, valor: str = None, lavados: str = None, habitaciones: str = None, url: str = None) -> str:
        try:
            if not id_str.strip():
                raise ValueError("Debe ingresar el ID de la propiedad que desea editar.")

            id = int(id_str)

            for propiedad in self.propiedades_cliente:
                if propiedad.id == id:
                    if tipo is not None and tipo.strip() != "":
                        propiedad.tipo = tipo
                    if ubicacion is not None and ubicacion.strip() != "":
                        propiedad.ubicacion = ubicacion
                    if dimension is not None and dimension.strip() != "":
                        propiedad.dimension = dimension
                    if valor is not None and valor.strip() != "":
                        propiedad.valor = valor
                    if lavados is not None and lavados.strip() != "":
                        propiedad.lavados = lavados
                    if habitaciones is not None and habitaciones.strip() !="":
                        propiedad.habitaciones = habitaciones
                    if url is not None and url.strip() != "" :
                        propiedad.url = url

                    return "Propiedad editada con éxito."

            raise ValueError("El ID dado no existe en las propiedades del cliente.")

        except ValueError as ve:
            return str(ve)
        except Exception as e:
            return f"Error inesperado: {e}"

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


class Conflicto(Exception):
    def __int__(self, mensaje:str) -> None:
        super().__init__(mensaje)
        self.mensaje = mensaje
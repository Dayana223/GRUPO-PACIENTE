class Paciente:

    def __init__(self, nombre, apellido, dni, grupo_sanguineo,):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__grupo_sanguineo = grupo_sanguineo
        self.__tiene_turno = False #Para cuando se cree el paciente

    def get_dni(self):
        return self.__dni

    def get_apellido(self):
        return self.__apellido

    def get_nombre(self):
        return self.__nombre

    def get_grupo_sanguineo(self):
        return self.__grupo_sanguineo

    def __str__(self):
        return f"DNI: {self.get_dni()}, apellido: {self.get_apellido()}, nombre: {self.get_nombre()}, grupo sanguineo: {self.get_grupo_sanguineo()}"

    def obtener_paciente(self):
        pass #Lo hago cuando tenga la BD

    def buscar_por_dni(self):
        pass #Lo hago cuando tenga la BD
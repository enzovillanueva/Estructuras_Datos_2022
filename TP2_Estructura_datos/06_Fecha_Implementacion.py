

class Fecha:

    def __init__(self, fecha: str = None):
        self._fechaValida = ""  # DDMMAAAA
        if (fecha is not None):
            self.agregarFecha(fecha)

    @property
    def getFecha(self) -> object:
        assert not len(
            self._fechaValida) == 0, "La fecha que ingresó es invalida"
        return self._fechaValida

    def agregarFecha(self, fecha: str):
        if (len(fecha) == 8) and (self.__validarFechas(fecha)):
            self._fechaValida = fecha

    def __eq__(self, fecha: object) -> bool:
        return self._fechaValida == fecha._fechaValida

    def __validarFechas(self, num) -> bool:
        mes31, mes30 = [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11]
        dia = int(num[:2])
        mes = int(num[2:4])
        año = int(num[4:])

        if (mes >= 1 and mes <= 12):
            if (mes in mes31):
                if (dia >= 1 and dia <= 31):
                    return True
            elif (mes in mes30):
                if(dia >= 1 and dia <= 30):
                    return True
            elif (mes == 2):
                if(año % 4 == 0):
                    if año % 100 != 0 or año % 400 == 0:
                        if(dia >= 1 and dia <= 29):
                            return True
                else:
                    if(dia >= 1 and dia <= 28):
                        return True

        return False


if __name__ == '__main__':
    fecha = Fecha()
    fecha.agregarFecha("10023344")
    print(fecha.getFecha)

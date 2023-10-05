class Alumno:
    Contador = 0
    def __init__(self, nombre, apellido, N1, N2, Ex1, N3, N4, Ex2, porcentaje_asistencia):
        Alumno.Contador += 1
        self.id = Alumno.Contador
        self.nombre = nombre
        self.apellido = apellido
        self.N1 = N1
        self.N2 = N2
        self.Ex1 = Ex1
        self.N3 = N3
        self.N4 = N4
        self.Ex2 = Ex2
        self.porcentaje_asistencia = porcentaje_asistencia

    def calcular_nota_final(self):
        promedio = (self.N1 + self.N2 + self.Ex1 + self.N3 + self.N4 + self.Ex2)
        return round(promedio, 2)

    def verificar_estado(self):
        promedio = self.calcular_nota_final()
        return "Aprobado" if promedio >= 70 and self.porcentaje_asistencia >= 70 else "Repobrado"

class Asignatura:
    def __init__(self,nombre_asignatura, nivel) -> None:
        self.nombre_asignatura = nombre_asignatura
        self.nivel = nivel


class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Curso:
    def __init__(self,asignatura, año_lectivo, fecha_inicio, fecha_fin, paralelo, modalidad, seccion, carrera):
        self.asignatura = asignatura
        self.año_lectivo = año_lectivo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.paralelo = paralelo
        self.modalidad = modalidad
        self.seccion = seccion
        self.carrera = carrera

class Acta:
    def __init__(self, profesor, curso, estudiantes):
        self.profesor = profesor
        self.curso = curso
        self.estudiantes = estudiantes

    def mostrar_informacion(self):
        print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                            Acta de calificacion                                                      ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")  
        print(f"Profesor: {self.profesor.nombre} {self.profesor.apellido} Carrera: {self.curso.carrera}")
        print(f"Nivel: {self.curso.asignatura.nivel} - Año Lectivo: {self.curso.año_lectivo}")
        print(f"Asignatura: {self.curso.asignatura.nombre_asignatura}     Modalidad: {self.curso.modalidad}")
        print(f"Paralelo: {self.curso.paralelo}         Seccion: {self.curso.seccion}")
        print(f"Fecha de inicio: {self.curso.fecha_inicio}      Fecha de fin: {self.curso.fecha_fin}")


    def mostrar_tabla_estudiantes(self):
        print("Tabla de Estudiantes:")
        
        print("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            "Nombre", "Apellidos", "N1", "N2", "Ex1", "N3", "N4", "Ex2", "Asistencia", "Promedio", "Estado", "ID"))
        for estudiante in self.estudiantes:
            promedio = estudiante.calcular_nota_final()
            estado = estudiante.verificar_estado()
            print("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                estudiante.nombre, estudiante.apellido, estudiante.N1, estudiante.N2,
                estudiante.Ex1,estudiante.N3, estudiante.N4, estudiante.Ex2, estudiante.porcentaje_asistencia, promedio, estado, estudiante.id))

if __name__ == '__main__':
    # Se instancias las objetos dentro de las clases =D
    profesor1 = Profesor("Juan", "Perez")
    profesor2 = Profesor("Victor", "Cruz")
    asignatura1 = Asignatura("Programacion Orientado a objetos", "4to")
    asignatura2 = Asignatura("Estructura de datos", "3ro")
    curso1 = Curso(asignatura1,"2023", "2023-09-01", "2023-12-15", "A1", "Presencial", "Noctuno", "Software")

    estudiante1 = Alumno("Ana", "One piece",14, 12, 15, 13, 14, 15, 80 )
    estudiante2 = Alumno("Carlos","Kawasaki",5, 10, 10, 4, 13, 12, 50)
    estudiante3 = Alumno("Elena", "Azuero", 15, 12, 10, 13, 14, 17, 70 )
    estudiante4 = Alumno("Kendryd", "Rodriguez", 5, 0, 10, 15, 10, 15, 64 )
    estudiante5 = Alumno("Casandra", "Aquilesbrinco", 11, 14, 17, 13, 11, 17, 90 )
    estudiante6 = Alumno("Juli", "matiolli", 15, 15, 20, 15, 15, 20, 90 )

    notas_curso1 = Acta(profesor1, curso1, [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6])

    notas_curso1.mostrar_informacion()
    notas_curso1.mostrar_tabla_estudiantes()

    print(" ")
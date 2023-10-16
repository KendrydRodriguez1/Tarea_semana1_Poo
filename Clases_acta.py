
class Facultad:
    cont_facu = 0

    def __init__(self, nombre, carrera):
        Facultad.cont_facu += 1
        self.id = Facultad.cont_facu
        self.nombre = nombre
        self.carrera = carrera

    def mostrar(self):
        return f"{self.nombre}, Carrera: {self.carrera.mostrar()}"


class Carrera:
    cont_carrera = 0

    def __init__(self, nombre):
        Carrera.cont_carrera += 1
        self.id = Carrera.cont_carrera
        self.nombre = nombre

    def mostrar(self):
        return f"{self.nombre}"


class Asignatura:
    cont_asignatura = 0

    def __init__(self, nombre):
        Asignatura.cont_asignatura += 1
        self.id = Asignatura.cont_asignatura
        self.nombre = nombre

    def mostrar(self):
        return f"{self.nombre}"


class Profesor:
    cont_profesor = 0

    def __init__(self, nombre, apellido):
        Profesor.cont_profesor += 1
        self.id = Profesor.cont_profesor
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        return f"{self.nombre} {self.apellido}"


class Semestre:
    cont_semestre = 0

    def __init__(self, descripcion, paralelo, seccion, fecha_inicio, fecha_fin):
        Semestre.cont_semestre += 1
        self.id = Semestre.cont_semestre
        self.descripcion = descripcion
        self.paralelo = paralelo
        self.seccion = seccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def mostrar(self):
        return f"{self.descripcion}, Paralelo: {self.paralelo}, Sección: {self.seccion}, Fechas: {self.fecha_inicio} - {self.fecha_fin}"


class Alumno:
    cont_alumno = 0

    def __init__(self, nombre, apellido):
        Alumno.cont_alumno += 1
        self.id = Alumno.cont_alumno
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        return f"{self.nombre} {self.apellido}"


class Notas:
    def __init__(self, facultad, carrera, asignatura, profesor, semestre, alumno, nota1, nota2, examen1, nota3, nota4, examen2, asistencia):
        self.facultad = facultad
        self.carrera = carrera
        self.asignatura = asignatura
        self.profesor = profesor
        self.semestre = semestre
        self.alumno = alumno
        self.nota1 = nota1
        self.nota2 = nota2
        self.examen1 = examen1
        self.nota3 = nota3
        self.nota4 = nota4
        self.examen2 = examen2
        self.asistencia = asistencia
        self.notafinal = nota1 + nota2 + examen1 + nota3 + nota4 + examen2
        self.estado = "Aprobado" if asistencia >= 70 and self.notafinal >= 70 else "Reprobado"

    def mostrar(self):
        mostrar_calificacion = [f"Facultad: {self.facultad.mostrar()}", f"Asignatura: {self.asignatura.mostrar()}", f"Profesor: {self.profesor.mostrar()}", f"Semestre: {self.semestre.mostrar()}", f"Alumno: {self.alumno.mostrar()}", f"Nota1: {self.nota1}", f"Nota2: {self.nota2}", f"Examen1: {self.examen1}" , f"Nota3: {self.nota3}", f"Nota4: {self.nota4}", f"Examen2: {self.examen2}", f"Asistencia: {self.asistencia}", f"Nota Final: {self.notafinal}", f"Estado: {self.estado}"]
        return mostrar_calificacion


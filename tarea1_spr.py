from pathlib import Path
ruta = Path("C:/Users/FAMILIA/Music/Programacion/POO/nombre_del_archivo.json")
import json
Json_archivo = {}

from Clases_acta import Facultad, Carrera, Asignatura, Profesor, Semestre, Alumno, Notas

if __name__ == "__main__":
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    carrera = Carrera(nombre_carrera)

    nombre_facultad = input("Ingrese el nombre de la facultad: ")
    facultad = Facultad(nombre_facultad, carrera)

    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    asignatura = Asignatura(nombre_asignatura)

    nombre_profesor = input("Ingrese el nombre del profesor: ")
    apellido_profesor = input("Ingrese el apellido del profesor: ")
    profesor = Profesor(nombre_profesor, apellido_profesor)

    nombre_semestre = input("Ingrese el nombre del semestre: ")
    paralelo_semestre = input("Ingrese el paralelo del semestre: ")
    seccion_semestre = input("Ingrese la sección del semestre: ")
    fecha_inicio_semestre = input("Ingrese la fecha de inicio del semestre: ")
    fecha_fin_semestre = input("Ingrese la fecha de fin del semestre: ")
    semestre = Semestre(nombre_semestre, paralelo_semestre, seccion_semestre, fecha_inicio_semestre, fecha_fin_semestre)

    print("--------------------------------------------------------------------------")
    try:
        Cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes a ingresar: "))  # Corrección en el nombre de la variable
        print("Ingrese datos de estudiante: ")
        for i in  range(Cantidad_estudiantes):
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            apellido_alumno = input("Ingrese el apellido del alumno: ")
            alumno = Alumno(nombre_alumno, apellido_alumno)
            
            # Ingresar las notas
            nota1 = float(input("Ingresa la nota 1: "))
            nota2 = float(input("Ingresa la nota 2: "))
            examen1 = float(input("Ingresa el examen 1: "))
            nota3 = float(input("Ingresa la nota 3: "))
            nota4 = float(input("Ingresa la nota 4: "))
            examen2 = float(input("Ingresa el examen 2: "))
            asistencia = float(input("Ingresa la asistencia: "))
            
            nota_instancia = Notas(facultad, carrera, asignatura, profesor, semestre, alumno, nota1, nota2, examen1, nota3, nota4, examen2, asistencia)
            suma = 1 + i
            Json_archivo[f"Estudiante{suma}"] = nota_instancia.mostrar()
    except:
        print("Error, ingrese bien los datos")   
        
    with ruta.open("w") as archivo:
        json.dump(Json_archivo, archivo)

        
        
        










        

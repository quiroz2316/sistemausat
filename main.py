from flask import Flask, request, jsonify, render_template, redirect
import controladores.controlador_semestre as cont_sem
import controladores.controlador_facultad as cont_fac

app = Flask(__name__)

#semestre
@app.route('/')
@app.route("/semestres")
def semestres():
    variable1=5
    variable2=0
    semestres = cont_sem.obtener_semestre_index(variable1,variable2)
    cant = cont_sem.cant_semestres()
    editSemestre = None
    return render_template("/semestre/ListarSemestre.html", semestres = semestres, editSemestre = editSemestre, cant = cant)
@app.route("/semestres/b", methods=["POST"])
def semestres1():
    limit = request.form.get("limit")
    offset = request.form.get("offset")
    semestres = cont_sem.obtener_semestre_index(limit,offset)
    editSemestre = None
    return render_template("/semestre/tabla.html", semestres = semestres, editSemestre = editSemestre)
@app.route("/semestres/<int:id>")
def semestre_editar(id):
    semestres = cont_sem.obtener_semestre()
    semestre = cont_sem.buscar_semestre_id(id)
    #print(semestre)
    return render_template("/semestre/ListarSemestre.html", semestres = semestres, editSemestre = semestre)


@app.route("/semestres", methods=["POST"])
def semestres_nombre():
    nombre = request.form["nombre"]
    semestres = cont_sem.buscar_semestre(nombre)
    return render_template("/semestre/ListaSemestre.html", semestres = semestres, editSemestre = None)


@app.route("/agregar_semestre")
def agregar_semestre():
    return render_template("/semestre/agregar.html")
@app.route("/darbaja_semestre", methods=["POST"])
def darbaja_semestre():
    cont_sem.dar_baja(request.form["id"])
    return redirect("/semestres")
@app.route("/daralta_semestre", methods=["POST"])
def daralta_semestre():
    cont_sem.dar_alta(request.form["id"])
    return redirect("/semestres")
@app.route("/guardar_semestre", methods=["POST"])
def guardar_semestre():
    
    nombreSe = request.form["nombreSe"]
    fechaI = request.form["fechaI"]
    fechaF = request.form["fechaF"]
    estado = request.form["estado"]
    if estado == "Vigente":
        estado = True
    else:
        estado = False
    cont_sem.insertar_semestre(nombreSe, fechaI,fechaF,estado)

    return redirect("/semestres")


@app.route("/editar_semestre/")
def editar_semestre():
    id = request.form["idSemestre"]
    semestre = cont_sem.buscar_semestre_id(id)
    opt = [None, None]
    if(semestre[4] == 0):
        opt[0] = "selected"
    else:
        opt[1] = "selected"
    return render_template(semestre=semestre, opt=opt)


@app.route("/actualizar_semestre", methods=["POST"])
def actualizar_semestre():
    idSemestre = request.form["idSemestre"]
    nombreSe = request.form["nombreSe"]
    fechaI = request.form["fechaI"]
    fechaF = request.form["fechaF"]
    estado = request.form["estado"]
    if estado == "Vigente":
        estado = True
    else:
        estado = False
    
    cont_sem.actualizar_semestre(nombreSe, fechaI,fechaF,estado, idSemestre)

    return redirect("/semestres")



@app.route("/eliminar_semestre", methods=["POST"])
def eliminar_semestre():
    id = request.form["id"]
    print("El id del semestre que se quiere eliminar es", id)
    cont_sem.eliminar_semestre(id)
    return redirect("/semestres")

#facultad


@app.route("/facultades")
def facultades():
    facultades = cont_fac.obtener_facultad()
    return render_template("/facultad/listarFacultad.html", facultades = facultades)

@app.route("/facultades/<int:id>")
def facultad_editar(id):
    facultades = cont_fac.obtener_facultad()
    facultad = cont_fac.buscar_facultad_id(id)
    #print(facultad)
    return render_template("/facultad/listarFacultad.html", facultades = facultades, editFacultad = facultad)

@app.route("/facultades", methods=["POST"])
def facultades_nombre():
    nombre = request.form["nombre"]
    facultades = cont_fac.buscar_facultad(nombre)
    return render_template("/facultad/listarFacultad.html", facultades = facultades, editFacultad = None)


@app.route("/agregar_facultad")
def agregar_facultad():
    return render_template("/facultad/agregar.html")

@app.route("/guardar_facultad", methods=["POST"])
def guardar_facultad():
    
    nombreFa = request.form["nombreFa"]
    descripcion = request.form["descripcion"]
    estado = request.form["estado"]
    if estado == "Vigente":
        estado = True
    else:
        estado = False
    cont_fac.insertar_facultad(nombreFa,descripcion,estado)

    return redirect("facultades")


@app.route("/editar_facultad/")
def editar_facultad():
    id = request.form["idP"]
    facultad = cont_fac.buscar_facultad_id(id)
    opt = [None, None]
    if(facultad[3] == 0):
        opt[0] = "selected"
    else:
        opt[1] = "selected"
    return render_template(facultad=facultad, opt=opt)


@app.route("/actualizar_facultad", methods=["POST"])
def actualizar_facultad():
    idFacultad = request.form["idFacultad"]
    nombreFa = request.form["nombreFa"]
    descripcion = request.form["descripcion"]
    estado = request.form["estado"]
    if estado == "Vigente":
        estado = True
    else:
        estado = False
    
    cont_fac.actualizar_facultad(nombreFa, descripcion,estado, idFacultad)

    return redirect("facultades")

@app.route("/dar_baja", methods=["POST"])
def dar_baja():
    cont_fac.dar_baja(request.form["id"])
    return redirect("/facultades")

@app.route("/eliminar_facultad", methods=["POST"])
def eliminar_facultad():
    cont_fac.eliminar_facultad(request.form["id"])
    return redirect("/facultades")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
from bd import obtener_conexion

def insertar_semestre(nombre,fechai, fechaf, estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO semestre_academico(id,nombre,fechaI, fechaF, estado) VALUES (%s,%s,%s, %s, %s)",
                       (obtener_ultimoid(),nombre,fechai, fechaf, estado))
    conexion.commit()
    conexion.close()

def obtener_ultimoid():
    conexion = obtener_conexion()
    id=None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COALESCE((MAX(id)),0)+1 as id from semestre_academico")
        id = cursor.fetchone()
    conexion.close()
    return id

def obtener_semestre():
    conexion = obtener_conexion()
    semestre = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,DATE_FORMAT(fechaI, '%d-%m-%Y')as fechaI,DATE_FORMAT(fechaF, '%d-%m-%Y')as fechaF ,CASE estado WHEN 1 THEN 'Vigente' ELSE 'No vigente' END AS estado FROM semestre_academico")
        semestre = cursor.fetchall()
        print(semestre)
    conexion.close()
    return semestre
def obtener_semestre_index(limit,offset):
    conexion=obtener_conexion()
    semestre=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,DATE_FORMAT(fechaI, '%d-%m-%Y')as fechaI,DATE_FORMAT(fechaF, '%d-%m-%Y')as fechaF ,CASE estado WHEN 1 THEN 'Vigente' ELSE 'No vigente' END AS estado FROM semestre_academico limit {} offset {}".format(limit, offset))
        semestre = cursor.fetchall()
        print(semestre)
    conexion.close()
    return semestre
def actualizar_semestre(nombre,fechai, fechaf, estado, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE semestre_academico SET nombre= %s, fechaI= %s, fechaF= %s, estado=%s WHERE id = %s",
                       (nombre,fechai, fechaf, estado, id))
    conexion.commit()
    conexion.close()


def dar_baja(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE semestre_academico SET estado=0 WHERE id = %s",
                       (id))
    conexion.commit()
    conexion.close()
def dar_alta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE semestre_academico SET estado=1 WHERE id = %s",
                       (id))
    conexion.commit()
    conexion.close()
def buscar_semestre(nombre):
    conexion = obtener_conexion()
    semestre = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,fechaI, fechaF, estado FROM semestre_academico WHERE nombre LIKE ('%'||%s||'%')", (nombre,))
        semestre = cursor.fetchall()
    conexion.close()
    return semestre

def buscar_semestre_id(id):
    conexion = obtener_conexion()
    semestre = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,fechaI, fechaF, estado FROM semestre_academico WHERE id = %s", (id,))
        semestre = cursor.fetchone()
    conexion.close()
    return semestre

def eliminar_semestre(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM semestre_academico WHERE id = %s", (id))
    conexion.commit()
    conexion.close()
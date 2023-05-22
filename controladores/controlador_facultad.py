from bd import obtener_conexion

def insertar_facultad(nombre, descripcion, estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO facultad(id,nombre, descripcion, estado) VALUES (%s, %s,%s, %s)",
                       (obtener_ultimoid(),nombre, descripcion, estado))
    conexion.commit()
    conexion.close()

def obtener_ultimoid():
    conexion = obtener_conexion()
    id=None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COALESCE((MAX(id)),0)+1 as id from facultad")
        id = cursor.fetchone()
    conexion.close()
    return id

def obtener_facultad():
    conexion = obtener_conexion()
    facultad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre,descripcion ,CASE estado WHEN 1 THEN 'Vigente' ELSE 'No vigente' END AS estado FROM facultad")
        facultad = cursor.fetchall()
        print(facultad)
    conexion.close()
    return facultad

def actualizar_facultad(nombre,descripcion, estado, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE facultad SET nombre= %s, descripcion = %s, estado=%s WHERE id = %s",
                       (nombre, descripcion, estado, id))
    conexion.commit()
    conexion.close()


def dar_baja(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE facultad SET estado=0 WHERE id = %s",
                       (id))
    conexion.commit()
    conexion.close()
def dar_alta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE facultad SET estado=1 WHERE id = %s",
                       (id))
    conexion.commit()
    conexion.close()
def buscar_facultad(nombre):
    conexion = obtener_conexion()
    facultad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre, descripcion, estado FROM facultad WHERE nombre LIKE ('%'||%s||'%')", (nombre,))
        facultad = cursor.fetchall()
    conexion.close()
    return facultad

def buscar_facultad_id(id):
    conexion = obtener_conexion()
    facultad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,nombre, descripcion, estado FROM facultad WHERE id = %s", (id,))
        facultad = cursor.fetchone()
    conexion.close()
    return facultad

def eliminar_facultad(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM facultad WHERE id = %s", (id))
    conexion.commit()
    conexion.close()
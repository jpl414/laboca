import sqlite3

# =========================================================
# CONEXIÓN A LA BASE DE DATOS
# =========================================================

conexion = sqlite3.connect("seguridad.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario(
    dni INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    celular TEXT NOT NULL,
    direccion TEXT NOT NULL,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL
)
"""

# TABLA PERFIL
cursor.execute("""
CREATE TABLE IF NOT EXISTS perfil(
    id_perfil INTEGER PRIMARY KEY,
    nombre_perfil TEXT NOT NULL
)
""")

# TABLA PERMISO
# Guarda cada operacion que puede realizar un usuario.
cursor.execute("""
CREATE TABLE IF NOT EXISTS permiso(
    id_permiso INTEGER PRIMARY KEY,
    nombre_permiso TEXT NOT NULL
)
""")

# TABLA FAMILIA
# Agrupa cuatro permisos o mas.
cursor.execute("""
CREATE TABLE IF NOT EXISTS familia(
    id_familia INTEGER PRIMARY KEY,
    nombre_familia TEXT NOT NULL
)
""")

# TABLA PATENTE
# Agrupa hasta tres permisos.
cursor.execute("""
CREATE TABLE IF NOT EXISTS patente(
    id_patente INTEGER PRIMARY KEY,
    nombre_patente TEXT NOT NULL
)
""")

# RELACION FAMILIA - PERMISO
cursor.execute("""
CREATE TABLE IF NOT EXISTS familia_permiso(
    id_familia INTEGER,
    id_permiso INTEGER,
    PRIMARY KEY (id_familia, id_permiso),
    FOREIGN KEY (id_familia) REFERENCES familia(id_familia),
    FOREIGN KEY (id_permiso) REFERENCES permiso(id_permiso)
)
""")

# RELACION PATENTE - PERMISO
cursor.execute("""
CREATE TABLE IF NOT EXISTS patente_permiso(
    id_patente INTEGER,
    id_permiso INTEGER,
    PRIMARY KEY (id_patente, id_permiso),
    FOREIGN KEY (id_patente) REFERENCES patente(id_patente),
    FOREIGN KEY (id_permiso) REFERENCES permiso(id_permiso)
)
""")

# RELACION PERFIL - FAMILIA
cursor.execute("""
CREATE TABLE IF NOT EXISTS perfil_familia(
    id_perfil INTEGER,
    id_familia INTEGER,
    PRIMARY KEY (id_perfil, id_familia),
    FOREIGN KEY (id_perfil) REFERENCES perfil(id_perfil),
    FOREIGN KEY (id_familia) REFERENCES familia(id_familia)
)
""")

# RELACION PERFIL - PATENTE
cursor.execute("""
CREATE TABLE IF NOT EXISTS perfil_patente(
    id_perfil INTEGER,
    id_patente INTEGER,
    PRIMARY KEY (id_perfil, id_patente),
    FOREIGN KEY (id_perfil) REFERENCES perfil(id_perfil),
    FOREIGN KEY (id_patente) REFERENCES patente(id_patente)
)
""")

conexion.commit()


conexion.commit()

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

# =========================================================
# REGISTRAR USUARIO
# =========================================================

def registrar():

    print("============ REGISTRO ============")

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    dni = input("Ingrese DNI: ")
    celular = input("Ingrese celular: ")
    direccion = input("Ingrese dirección: ")
    usuario = input("Ingrese usuario: ")
    email = input("Ingrese email: ")
    contrasena = input("Ingrese contraseña: ")
    confirmar = input("Repita contraseña: ")

    # -----------------------------------------------------
    # VERIFICAR CAMPOS VACÍOS
    # -----------------------------------------------------
        print("El DNI debe contener solamente números")

    if (nombre == "" or
    if (nombre == "" or
        apellido == "" or
        dni == "" or
        celular == "" or
        direccion == "" or
        usuario == "" or
        email == "" or
        contrasena == "" or
        confirmar == ""):

        print("por favor complete todos los campos.")
        return

    if not celular.isdigit():
        print("El celular debe contener solamente números enteros")
        return

    if len(celular) < 10:
        print("El número de celular debe tener al menos 10 números enteros")
        return


    if len(contrasena) < 8:
        print("La contraseña debe tener mínimo 8 caracteres.")}
        contrasena = input("Ingrese contrasena: ")
        confirmar = input("Repita contrasena: ")
        return
import sqlite3

# =========================================================
# CONEXIÓN A LA BASE DE DATOS
# =========================================================

conexion = sqlite3.connect("seguridad.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario(
    dni INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    celular TEXT NOT NULL,
    direccion TEXT NOT NULL,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conexion.commit()

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

# =========================================================
# REGISTRAR USUARIO
# =========================================================

def registrar():

    print("============ REGISTRO ============")

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    dni = input("Ingrese DNI: ")
    celular = input("Ingrese celular: ")
    direccion = input("Ingrese dirección: ")
    usuario = input("Ingrese usuario: ")
    email = input("Ingrese email: ")
    contrasena = input("Ingrese contraseña: ")
    confirmar = input("Repita contraseña: ")

    # -----------------------------------------------------
    # VERIFICAR CAMPOS VACÍOS
    # -----------------------------------------------------
        print("El DNI debe contener solamente números")

    if (nombre == "" or
    if (nombre == "" or
        apellido == "" or
        dni == "" or
        celular == "" or
        direccion == "" or
        usuario == "" or
        email == "" or
        contrasena == "" or
        confirmar == ""):

        print("por favor complete todos los campos.")
        return

    if not celular.isdigit():
        print("El celular debe contener solamente números enteros")
        return

    if len(celular) < 10:
        print("El número de celular debe tener al menos 10 números enteros")
        return


    if len(contrasena) < 8:
        print("La contraseña debe tener mínimo 8 caracteres.")}
        contrasena = input("Ingrese contrasena: ")
        confirmar = input("Repita contrasena: ")
        return

    if contrasena != confirmar:
        print("Las contrasenas no coinciden, debe ingresar su contraseña de nuevo")
        print("  ")
        contrasena = input("Ingrese contrasena: ")
        confirmar = input("Repita contrasena: ")
        return

    cursor.execute(
        "SELECT * FROM usuario WHERE dni = ?",
        (int(dni),)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("Su usuario ya fue dado de alta.")
        return

    # -----------------------------------------------------
    # INSERTAR USUARIO
    # -----------------------------------------------------

    cursor.execute("""
        INSERT INTO usuario
        (dni, nombre, apellido, contrasena, celular, direccion, usuario, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        int(dni),
        nombre,
        apellido,
        contrasena,
        celular,
        direccion,
        usuario,
        email
    ))

    conexion.commit()

    print("Operación exitosa.")
    print("Usuario registrado correctamente.")

def login():

    print("========== LOGIN ==========")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        # -------------------------------------------------
        # VERIFICAR CAMPOS VACÍOS
        # -------------------------------------------------

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("Por favor complete sus datos.")
            continue

        # -------------------------------------------------
        # BUSCAR USUARIO EN LA BASE DE DATOS
        # -------------------------------------------------

        cursor.execute("""
            SELECT * FROM usuario
            WHERE usuario = ? AND contrasena = ?
        """, (
            usuario_ingresado,
            contrasena_ingresada
        ))

        resultado = cursor.fetchone()

        # -------------------------------------------------
        # SI ENCUENTRA EL USUARIO
        # -------------------------------------------------

        if resultado:

            print("Login correcto.")
            print("Bienvenido/a", resultado[1])
            return

        # -------------------------------------------------
        # SI LOS DATOS SON INCORRECTOS
        # -------------------------------------------------

        intentos += 1

        if intentos == 3:

            print("Su clave ha sido bloqueada.")
            return

        else:

            print("Datos incorrectos.")
            print("Intento", intentos, "de 3.")


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def menu():

    while True:

        print("========== MENÚ ==========")
        print("1 - Registrar usuario")
        print("2 - Iniciar sesión")
        print("3 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nom = input("Ingrese nombre: ")
            ape = input("Ingrese apellido: ")
            dnii = input("Ingrese DNI: ")
            celu = input("Ingrese celular: ")
            direc = input("Ingrese dirección: ")
            usua = input("Ingrese usuario: ")
            emaill = input("Ingrese email: ")
            contrasena = input("Ingrese contraseña: ")
            confirmar = input("Repita contraseña: ")   
            registrar()

        elif opcion == "2":
            login()
    print("========== LOGIN ==========")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("Por favor complete sus datos.")
            continue

        # -------------------------------------------------
        # BUSCAR USUARIO EN LA BASE DE DATOS
        # -------------------------------------------------

        cursor.execute("""
            SELECT * FROM usuario
            WHERE usuario = ? AND contrasena = ?
        """, (
            usuario_ingresado,
            contrasena_ingresada
        ))

        resultado = cursor.fetchone()

        if resultado:

            print("Login correcto.")
            print("Bienvenido/a", resultado[1])
            return

        intentos += 1

        if intentos == 3:

            print("Su clave ha sido bloqueada.")
            return

        else:

            print("Datos incorrectos.")
            print("Intento", intentos, "de 3.")
        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


# =========================================================
# EJECUTAR PROGRAMA
# =========================================================

menu()

# Cerrar conexión
conexion.close()
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    celular TEXT NOT NULL,
    direccion TEXT NOT NULL,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL
)
    if contrasena != confirmar:
        print("Las contrasenas no coinciden, debe ingresar su contraseña de nuevo")
        print("  ")
        contrasena = input("Ingrese contrasena: ")
        confirmar = input("Repita contrasena: ")
        return

    cursor.execute(
        "SELECT * FROM usuario WHERE dni = ?",
        (int(dni),)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("Su usuario ya fue dado de alta.")
        return

    # -----------------------------------------------------
    # INSERTAR USUARIO
    # -----------------------------------------------------

    cursor.execute("""
        INSERT INTO usuario
        (dni, nombre, apellido, contrasena, celular, direccion, usuario, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        int(dni),
        nombre,
        apellido,
        contrasena,
        celular,
        direccion,
        usuario,
        email
    ))

    conexion.commit()

    print("Operación exitosa.")
    print("Usuario registrado correctamente.")

def login():

    print("========== LOGIN ==========")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        # -------------------------------------------------
        # VERIFICAR CAMPOS VACÍOS
        # -------------------------------------------------

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("Por favor complete sus datos.")
            continue

        # -------------------------------------------------
        # BUSCAR USUARIO EN LA BASE DE DATOS
        # -------------------------------------------------

        cursor.execute("""
            SELECT * FROM usuario
            WHERE usuario = ? AND contrasena = ?
        """, (
            usuario_ingresado,
            contrasena_ingresada
        ))

        resultado = cursor.fetchone()

        # -------------------------------------------------
        # SI ENCUENTRA EL USUARIO
        # -------------------------------------------------

        if resultado:

            print("Login correcto.")
            print("Bienvenido/a", resultado[1])
            return

        # -------------------------------------------------
        # SI LOS DATOS SON INCORRECTOS
        # -------------------------------------------------

        intentos += 1

        if intentos == 3:

            print("Su clave ha sido bloqueada.")
            return

        else:

            print("Datos incorrectos.")
            print("Intento", intentos, "de 3.")


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def menu():

    while True:

        print("========== MENÚ ==========")
        print("1 - Registrar usuario")
        print("2 - Iniciar sesión")
        print("3 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nom = input("Ingrese nombre: ")
            ape = input("Ingrese apellido: ")
            dnii = input("Ingrese DNI: ")
            celu = input("Ingrese celular: ")
            direc = input("Ingrese dirección: ")
            usua = input("Ingrese usuario: ")
            emaill = input("Ingrese email: ")
            contrasena = input("Ingrese contraseña: ")
            confirmar = input("Repita contraseña: ")   
            registrar()

        elif opcion == "2":
            login()
    print("========== LOGIN ==========")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("Por favor complete sus datos.")
            continue

        # -------------------------------------------------
        # BUSCAR USUARIO EN LA BASE DE DATOS
        # -------------------------------------------------

        cursor.execute("""
            SELECT * FROM usuario
            WHERE usuario = ? AND contrasena = ?
        """, (
            usuario_ingresado,
            contrasena_ingresada
        ))

        resultado = cursor.fetchone()

        if resultado:

            print("Login correcto.")
            print("Bienvenido/a", resultado[1])
            return

        intentos += 1

        if intentos == 3:

            print("Su clave ha sido bloqueada.")
            return

        else:

            print("Datos incorrectos.")
            print("Intento", intentos, "de 3.")
        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


# =========================================================
# EJECUTAR PROGRAMA
# =========================================================

menu()

# Cerrar conexión
conexion.close()
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    celular TEXT NOT NULL,
    direccion TEXT NOT NULL,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL
)
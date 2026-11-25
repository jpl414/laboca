import sqlite3

# =========================================================
# CONEXIÓN A LA BASE DE DATOS
# =========================================================

conexion = sqlite3.connect("seguridad.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario(
    dni INTEGER PRIMARY KEY,import sqlite3

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


# =========================================================
# FUNCIÓN PARA VALIDAR CONTRASEÑA
# =========================================================

def validar_contrasena(contrasena):
    # Debe tener al menos 8 caracteres
    if len(contrasena) < 8:
        return False

    # Contar letras mayúsculas
    cantidad_mayusculas = 0

    # Saber si tiene carácter especial
    tiene_especial = False

    for caracter in contrasena:

        if caracter.isupper():
            cantidad_mayusculas += 1

        # Si no es letra ni número, es un carácter especial
        if not caracter.isalnum():
            tiene_especial = True

    # Debe tener como mínimo 2 mayúsculas
    if cantidad_mayusculas < 2:
        return False

    # Debe tener como mínimo 1 carácter especial
    if not tiene_especial:
        return False

    return True


# =========================================================
# REGISTRAR USUARIO
# =========================================================

def registrar():

    print("\n========== REGISTRO ==========\n")

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
        print("\nEl DNI debe contener solamente números.")

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

        print("\nPor favor complete todos los campos.")
        return

    # -----------------------------------------------------
    # VERIFICAR QUE DNI SEA NUMÉRICO
    # -----------------------------------------------------

    if not dni.isdigit():
        print("\nEl DNI debe contener solamente números.")
        return

    # -----------------------------------------------------
    # VERIFICAR QUE CELULAR SEA NUMÉRICO
    # -----------------------------------------------------

    if not celular.isdigit():
        print("\nEl celular debe contener solamente números.")
        return

    if len(celular) < 10:
        print("\nEl número de celular debe tener al menos 10 números.")
        return

    # -----------------------------------------------------
    # VALIDAR CONTRASEÑA
    # -----------------------------------------------------

    if len(contrasena) < 8:
        print("\nLa contraseña debe tener mínimo 8 caracteres.")
        return

    # Contar mayúsculas
    mayusculas = 0
    especial = False

    for caracter in contrasena:

        if caracter.isupper():
            mayusculas += 1

        if not caracter.isalnum():
            especial = True

    if mayusculas < 2:
        print("\nLa contraseña debe tener al menos 2 letras mayúsculas.")
        return

    if not especial:
        print("\nLa contraseña debe tener al menos 1 carácter especial.")
        return

    # -----------------------------------------------------
    # COMPARAR CONTRASEÑAS
    # -----------------------------------------------------

    if contrasena != confirmar:
        print("\nLas contraseñas no coinciden.")
        return

    # -----------------------------------------------------
    # BUSCAR SI EL DNI YA EXISTE
    # -----------------------------------------------------

    cursor.execute(
        "SELECT * FROM usuario WHERE dni = ?",
        (int(dni),)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("\nSu usuario ya fue dado de alta.")
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

    print("\nOperación exitosa.")
    print("Usuario registrado correctamente.")


# =========================================================
# LOGIN
# =========================================================

def login():

    print("\n========== LOGIN ==========\n")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        # -------------------------------------------------
        # VERIFICAR CAMPOS VACÍOS
        # -------------------------------------------------

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("\nPor favor complete sus datos.")
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

            print("\nLogin correcto.")
            print("Bienvenido/a", resultado[1])
            return

        # -------------------------------------------------
        # SI LOS DATOS SON INCORRECTOS
        # -------------------------------------------------

        intentos += 1

        if intentos == 3:

            print("\nSu clave ha sido bloqueada.")
            return

        else:

            print("\nDatos incorrectos.")
            print("Intento", intentos, "de 3.")


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def menu():

    while True:

        print("\n========== MENÚ ==========")
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

        elif opcion == "3":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción incorrecta.")


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
""")

conexion.commit()


# =========================================================
# FUNCIÓN PARA VALIDAR CONTRASEÑA
# =========================================================

def validar_contrasena(contrasena):
    # Debe tener al menos 8 caracteres
    if len(contrasena) < 8:
        return False

    # Contar letras mayúsculas
    cantidad_mayusculas = 0

    # Saber si tiene carácter especial
    tiene_especial = False

    for caracter in contrasena:

        if caracter.isupper():
            cantidad_mayusculas += 1

        # Si no es letra ni número, es un carácter especial
        if not caracter.isalnum():
            tiene_especial = True

    # Debe tener como mínimo 2 mayúsculas
    if cantidad_mayusculas < 2:
        return False

    # Debe tener como mínimo 1 carácter especial
    if not tiene_especial:
        return False

    return True


# =========================================================
# REGISTRAR USUARIO
# =========================================================

def registrar():

    print("\n========== REGISTRO ==========\n")

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

    if (nombre == "" or
        apellido == "" or
        dni == "" or
        celular == "" or
        direccion == "" or
        usuario == "" or
        email == "" or
        contrasena == "" or
        confirmar == ""):

        print("\nPor favor complete todos los campos.")
        return

    # -----------------------------------------------------
    # VERIFICAR QUE DNI SEA NUMÉRICO
    # -----------------------------------------------------

    if not dni.isdigit():
        print("\nEl DNI debe contener solamente números.")
        return

    # -----------------------------------------------------
    # VERIFICAR QUE CELULAR SEA NUMÉRICO
    # -----------------------------------------------------

    if not celular.isdigit():
        print("\nEl celular debe contener solamente números.")
        return

    if len(celular) < 10:
        print("\nEl número de celular debe tener al menos 10 números.")
        return

    # -----------------------------------------------------
    # VALIDAR CONTRASEÑA
    # -----------------------------------------------------

    if len(contrasena) < 8:
        print("\nLa contraseña debe tener mínimo 8 caracteres.")
        return

    # Contar mayúsculas
    mayusculas = 0
    especial = False

    for caracter in contrasena:

        if caracter.isupper():
            mayusculas += 1

        if not caracter.isalnum():
            especial = True

    if mayusculas < 2:
        print("\nLa contraseña debe tener al menos 2 letras mayúsculas.")
        return

    if not especial:
        print("\nLa contraseña debe tener al menos 1 carácter especial.")
        return

    # -----------------------------------------------------
    # COMPARAR CONTRASEÑAS
    # -----------------------------------------------------

    if contrasena != confirmar:
        print("\nLas contraseñas no coinciden.")
        return

    # -----------------------------------------------------
    # BUSCAR SI EL DNI YA EXISTE
    # -----------------------------------------------------

    cursor.execute(
        "SELECT * FROM usuario WHERE dni = ?",
        (int(dni),)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("\nSu usuario ya fue dado de alta.")
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

    print("\nOperación exitosa.")
    print("Usuario registrado correctamente.")


# =========================================================
# LOGIN
# =========================================================

def login():

    print("\n========== LOGIN ==========\n")

    intentos = 0

    while intentos < 3:

        usuario_ingresado = input("Ingrese usuario: ")
        contrasena_ingresada = input("Ingrese contraseña: ")

        # -------------------------------------------------
        # VERIFICAR CAMPOS VACÍOS
        # -------------------------------------------------

        if usuario_ingresado == "" or contrasena_ingresada == "":
            print("\nPor favor complete sus datos.")
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

            print("\nLogin correcto.")
            print("Bienvenido/a", resultado[1])
            return

        # -------------------------------------------------
        # SI LOS DATOS SON INCORRECTOS
        # -------------------------------------------------

        intentos += 1

        if intentos == 3:

            print("\nSu clave ha sido bloqueada.")
            return

        else:

            print("\nDatos incorrectos.")
            print("Intento", intentos, "de 3.")


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def menu():

    while True:

        print("\n========== MENÚ ==========")
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

        elif opcion == "3":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción incorrecta.")


# =========================================================
# EJECUTAR PROGRAMA
# =========================================================

menu()

# Cerrar conexión
conexion.close()
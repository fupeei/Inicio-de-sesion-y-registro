from app_flask.config.mysqlconecction import connectToMySQL
from app_flask import EMAIL_REGEX
from flask import flash

class Usuario:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.edad = datos["edad"]
        self.email = datos["email"]
        self.contraseña = datos["contraseña"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def agregar_uno(cls,datos):
        query = """
                Insert INTO usuarios (nombre,apellido,edad,email,contraseña) 
                VALUES(%(nombre)s,%(apellido)s,%(edad)s,%(email)s,%(contraseña)s);
                """
        resultado = connectToMySQL('usuarios_bd').query_db(query,datos)
        return resultado
    
    @classmethod
    def seleccionar_uno(cls, datos):
        query = """ 
                SELECT *
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL("usuarios_bd").query_db(query, datos)
        
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
    
    @staticmethod
    def validar_login(datos):
        es_valido = True
        if datos == None:
            flash("Usuario o contraseña incorrectas", "error_login")
            es_valido = False
        return es_valido
    
    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos["nombre"]) <= 2:
            flash("Usa un nombre valido", "error_nombre")
            es_valido = False
        if len(datos["apellido"]) <=2:
            flash("Usa un apellido valido", "error_apellido")
        if len(datos["edad"]) <=0:
            flash("Ingresa una edad valida", "error_edad")
            es_valido = False
        
        if not EMAIL_REGEX.match(datos['email']): 
            flash("Email invalido!", "error_email")
            is_valid = False
        return is_valid

        if len(datos["contraseña"]) <=8:
            flash("La contraseña debe tener al menos 8 caracteres", "error_contraseña")
            es_valido = False
        if datos["c-contraseña"] != datos ["contraseña"]:
            flash("Tus contraseñas no coinciden", "error_coincidir")
            es_valido = False
        return es_valido
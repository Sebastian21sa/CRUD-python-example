import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea una conexión con la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host='18.191.204.59',          
            database='employees',       
            user='studentsucundi',               
            password='mami_prende_la_radi0'       
        )
        if connection.is_connected():
            print('Conexión a la base de datos establecida.')
            return connection
    except Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None

def create_user(connection, nombre, email):
    """Inserta un nuevo usuario en la base de datos."""
    try:
        cursor = connection.cursor()
        query = "INSERT INTO departments (dept_no, dept_name) VALUES (%s, %s)"
        cursor.execute(query, (nombre, email))
        connection.commit()
        print('Usuario creado con éxito.')
    except Error as e:
        print(f'Error al crear usuario: {e}')
    finally:
        cursor.close()

def read_users(connection):
    """Lee todos los usuarios de la base de datos."""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM departments"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Error as e:
        print(f'Error al leer usuarios: {e}')
    finally:
        cursor.close()

def update_user(connection, user_id, nombre, email):
    """Actualiza un usuario en la base de datos."""
    try:
        cursor = connection.cursor()
        query = "UPDATE departments SET nombre = %s, email = %s WHERE id = %s"
        cursor.execute(query, (nombre, email, user_id))
        connection.commit()
        print('Usuario actualizado con éxito.')
    except Error as e:
        print(f'Error al actualizar usuario: {e}')
    finally:
        cursor.close()

def delete_user(connection, user_id):
    """Elimina un usuario de la base de datos."""
    try:
        cursor = connection.cursor()
        query = "DELETE FROM departments WHERE dept_no = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        print('Usuario eliminado con éxito.')
    except Error as e:
        print(f'Error al eliminar usuario: {e}')
    finally:
        cursor.close()

def main():
    connection = create_connection()
    if connection:
        # Crear un nuevo usuario
        create_user(connection, 'Juan Pérez', 'juan.perez@example.com')
        
        # Leer todos los usuarios
        print('Usuarios en la base de datos:')
        read_users(connection)
        
        # Actualizar un usuario existente (asumiendo que el ID del usuario es 1)
        update_user(connection, 1, 'Juan Pérez Actualizado', 'juan.perez.actualizado@example.com')
        
        # Leer todos los usuarios después de la actualización
        print('Usuarios después de la actualización:')
        read_users(connection)
        
        # Eliminar un usuario (asumiendo que el ID del usuario es 1)
        delete_user(connection, 1)
        
        # Leer todos los usuarios después de la eliminación
        print('Usuarios después de la eliminación:')
        read_users(connection)
        
        connection.close()

if __name__ == "__main__":
    main()
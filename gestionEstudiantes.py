from flask import Blueprint, request, jsonify
from conectionDB import *
from gestionEquipos import equipo_disponible

# http://localhost:5000/api/estudiantes

estudiantes_bp = Blueprint('estudiantes', __name__)


@estudiantes_bp.route('/estudiantes', methods=['GET'])
def get_student():
    conn = get_connection()
    # la parte de extras de pone los datos como objetos
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM estudiante')
    students = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(students)


@estudiantes_bp.route('/estudiantes', methods=['POST'])
def create_student():
    new_student = request.get_json()  # guarda lo que viene en un json en una variable
    cod = new_student['codigo_est']
    nom = new_student['nom_est']
    ape = new_student['ape_est']
    carrera = new_student['carrera']
    materia = new_student['materia_programacion']
    id_equipo = new_student['id_equipo']

    if (equipo_disponible(id_equipo)):
        conn = get_connection()  # crea una coneccion con la BD
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute('INSERT INTO estudiante VALUES (%s, %s, %s, %s, %s, %s) RETURNING *',
                    (cod, nom, ape, carrera, materia, id_equipo))  # consulta para la BD

        student_created = cur.fetchone()

        conn.commit()  # un commit para que el query se ejecute
        cur.close()
        conn.close()
        return jsonify(student_created)

    return jsonify({'message': 'team is full'}), 404


@estudiantes_bp.route('/estudiantes/<cod>', methods=['DELETE'])
def delete_student(cod):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute(
        'DELETE FROM estudiante WHERE codigo_est = %s RETURNING *', (cod,))
    student_deleted = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if student_deleted is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(student_deleted)


@estudiantes_bp.route('/estudiantes/deleteAll', methods=['DELETE'])
def delete_All():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DELETE FROM estudiante')

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({'message': 'All students deleted'})


@estudiantes_bp.route('/estudiantes/<cod>', methods=['PUT'])
def update_student(cod):

    new_student = request.get_json()  # guarda lo que viene en un jason en una variable
    nom = new_student['nom_est']
    ape = new_student['ape_est']
    carrera = new_student['carrera']
    materia = new_student['materia_programacion']
    id_equipo = new_student['id_equipo']

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('UPDATE estudiante SET nom_est=%s, ape_est=%s, carrera=%s, materia_programacion=%s, id_equipo=%s ' +
                'WHERE codigo_est=%s RETURNING *', (nom, ape, carrera, materia, id_equipo, cod))

    student = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if student is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(student)

from flask import Blueprint, request, jsonify
from conectionDB import *

# http://localhost:5000/api/equipos

equipos_bp = Blueprint('equipos', __name__)


@equipos_bp.route('/equipos', methods=['GET'])
def get_team():
    conn = get_connection()
    # la parte de extras de pone los datos como objetos
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM equipo')
    teams = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(teams)

@equipos_bp.route('/equipos/miembros/<id>', methods=['GET'])
def get_team_members(id):
    conn = get_connection()
    # la parte de extras de pone los datos como objetos
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT codigo_est, nom_est, ape_est, carrera, materia_programacion '+
                'FROM equipo e, estudiante es '+
                'WHERE e.id_equipo=es.id_equipo AND e.id_equipo=%s', (id,))
    
    members = cur.fetchall()
    cur.close()
    conn.close()

    return members

@equipos_bp.route('/equipos', methods=['POST'])
def create_team():
    new_team = request.get_json()  # guarda lo que viene en un jason en una variable
    cod = new_team['id_equipo'] 
    nom = new_team['nom_equipo']
    id_competencia = new_team['id_competencia']


    conn = get_connection()  # crea una coneccion con la BD
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO equipo(id_equipo, nom_equipo, id_competencia)'+
                ' VALUES (%s, %s, %s) RETURNING *',
                (cod, nom, id_competencia))  # consulta para la BD
    
    team_created = cur.fetchone()

    conn.commit()  # un commit para que el query se ejecute
    cur.close()
    conn.close()

    return jsonify(team_created)


@equipos_bp.route('/equipos/<cod>', methods=['DELETE'])
def delete_team(cod):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DELETE FROM equipo WHERE id_equipo = %s RETURNING *', (cod,))
    team_deleted = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if team_deleted is None:
        return jsonify({'message': 'Team not found'}), 404
    return jsonify(team_deleted)

@equipos_bp.route('/equipos/deleteAll', methods=['DELETE'])
def delete_All():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DELETE FROM equipo')

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({'message': 'All teams deleted'})

@equipos_bp.route('/equipos/<cod>', methods=['PUT'])
def update_team(cod):

    new_team = request.get_json()  # guarda lo que viene en un jason en una variable
    nom = new_team['nom_equipo']
    id_competencia = new_team['id_competencia']


    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('UPDATE equipo SET nom_equipo=%s, id_competencia=%s'+
                ' WHERE id_equipo=%s RETURNING *', (nom, id_competencia, cod))

    team = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if team is None:
        return jsonify({'message': 'Team not found'}), 404
    return jsonify(team)

def equipo_disponible(id):
    members= get_team_members(id)

    return not len(members) >=3


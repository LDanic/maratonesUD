from flask import Blueprint, request, jsonify
from conectionDB import *

# http://localhost:5000/api/equipos

competencias_bp = Blueprint('competencias', __name__)


@competencias_bp.route('/competencias', methods=['GET'])
def get_comp():
    conn = get_connection()
    # la parte de extras de pone los datos como objetos
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM competencia')
    comp = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(comp)

@competencias_bp.route('/competencias/<semestre>', methods=['PUT'])
def update_comp(semestre):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('UPDATE competencia SET semestre= %s', (semestre,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'new semester started'})

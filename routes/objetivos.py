from flask import Blueprint, request, jsonify

objetivos_bp = Blueprint('objetivos', __name__)


def init_objetivos_bp(db, User):
    # @objetivos_bp.route('/monto', methods=['POST'])
    # def agregar_monto():
    #     data = request.get_json()
    #     usuario = {}
    #     interfaz = ['monto']
    #     values = [data.get(item) for item in interfaz if data.get(item)]
    #     check = len(values) == len(interfaz)
    #     if check:
    #         for k, value in zip(interfaz, values):
    #             usuario[k] = value
    #         usuario['tabla'] = 'monto'
    #         db.insert(usuario)
    #         return jsonify({'mensaje': 'Monto agregado!'}), 201
        
    #     return jsonify({'error': 'Bad Request', 'mesaje': 'monto requeridos'}), 400

    @objetivos_bp.route('/monto', methods=['GET'])
    def obtener_monto():
        data = db.search(User.tabla == 'monto')
        return jsonify({'mensaje': data}), 200
    
    return objetivos_bp
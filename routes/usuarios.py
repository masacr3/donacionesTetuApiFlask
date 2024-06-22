from flask import Blueprint, request, jsonify

usuarios_bp = Blueprint('usuarios', __name__)


def init_usuarios_bp(db, User):
    @usuarios_bp.route('', methods=['POST'])
    def agregar_usuario():
        data = request.get_json()
        usuario = {}
        interfaz = ['nombre', 'provincia', 'monto']
        values = [data.get(item) for item in interfaz if data.get(item)]
        check = len(values) == len(interfaz)
        if check:
            for k, value in zip(interfaz, values):
                usuario[k] = value
            usuario['tabla'] = 'usuarios'
            db.insert(usuario)
            return jsonify({'mensaje': 'Usuario agregado!'}), 201
        
        return jsonify({'error': 'Bad Request', 'mesaje': 'nombre, provincia y monto requeridos'}), 400

    @usuarios_bp.route('', methods=['GET'])
    def obtener_usuarios():
        usuarios = db.search(User.tabla == 'usuarios')
        return jsonify(usuarios), 200
    
    return usuarios_bp
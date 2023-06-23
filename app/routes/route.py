from flask import Blueprint, jsonify


blueprint = Blueprint('mock', __name__)


@blueprint.route('/ping', methods=['GET'])
def ping():
  return jsonify('pong')
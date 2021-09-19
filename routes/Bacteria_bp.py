from flask import Blueprint

from controllers.Bacteria import Index, Save, ABacteria

BacteriaBP = Blueprint('Bacteria_bp', __name__)

BacteriaBP.route('/', methods=['GET'])(Index)
BacteriaBP.route('/ABacteria', methods=['GET'])(ABacteria)
BacteriaBP.route('/Save', methods=['POST'])(Save)
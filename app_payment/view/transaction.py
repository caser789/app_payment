from flask import Blueprint
from flask import jsonify

blueprint = Blueprint('transaction', __name__, url_prefix='/transaction')


@blueprint.route('/create', methods=['GET', 'POST'])
def create():
	return jsonify(meta=dict(code=200), data=dict(a=1))
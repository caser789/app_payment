from flask import Blueprint
from flask import request
from flask import jsonify
from dock.common.exceptions import AppBaseException

blueprint = Blueprint('transaction', __name__, url_prefix='/transaction')


class Provision(object):
    def __init__(self):
        pass

    @classmethod
    def create(cls, p):
        return cls()

    def to_dict(self):
        return {'id': 2}


class Transaction(object):

    @classmethod
    def from_provisions(cls, *provisions):
        return []

    @classmethod
    def create(cls):
        return cls()

    def to_dict(self):
        return {'id': 1}


class ProvisionsBelongsToDifferentTransactionsException(Exception):
    pass


error_provisions_from_different_transactions = AppBaseException(1000, 'Provisions no belong to the same transaction')


@blueprint.route('/create', methods=['GET', 'POST'])
def create():
    data = request.get_json(force=True, silent=True)
    provisions= data['provisions']
    provisions = [Provision.create(p) for p in provisions]
    try:
        transaction = Transaction.from_provisions(provisions)
    except ProvisionsBelongsToDifferentTransactionsException:
        raise error_provisions_from_different_transactions

    if not transaction:
        transaction = Transaction.create()
    return jsonify(meta=dict(code=200), data=transaction.to_dict())

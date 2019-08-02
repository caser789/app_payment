def init(app):
	from .view import transaction
	return [transaction.blueprint]
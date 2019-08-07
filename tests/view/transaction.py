import json
import mock
import unittest
from dock.web import DockApp

app = DockApp("")

import app_payment
app.mount(app_payment)
from app_payment.view.transaction import ProvisionsBelongsToDifferentTransactionsException


class CreateTransactionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.flaskapp.test_client()
        self.url = '/transaction/create'

    @mock.patch("app_payment.view.transaction.Transaction")
    def test_ok_by_new_transaction(self, Transaction):
        Transaction.from_provisions.return_value = None

        data = {
            'transaction_type': 1,
            'platform': 2,
            'client_id': 123,
            'user_id': 456,
            'total_amount': 900000,
            'currency': 'SGD',
            'provisions': [
                {
                    'expire_time': 1559883709,
                    'channel_id': 5005601,
                    'entity_id': 223610,
                    'channel_params': {}
                },
            ],
            'memo': 'memo',
            'extra_data': {},
        }
        self.app.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        Transaction.create.assert_called()

    @mock.patch("app_payment.view.transaction.Transaction")
    def test_ok_get_transaction_from_provision(self, Transaction):
        Transaction.from_provisions.return_value = mock.MagicMock()

        data = {
            'transaction_type': 1,
            'platform': 2,
            'client_id': 123,
            'user_id': 456,
            'total_amount': 900000,
            'currency': 'SGD',
            'provisions': [
                {
                    'expire_time': 1559883709,
                    'channel_id': 5005601,
                    'entity_id': 223610,
                    'channel_params': {}
                },
            ],
            'memo': 'memo',
            'extra_data': {},
        }
        self.app.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        Transaction.create.assert_not_called()

    @mock.patch("app_payment.view.transaction.Transaction")
    def test_provision_not_belong_to_same_transaction_then_error(self, Transaction):
        Transaction.from_provisions.side_effect = ProvisionsBelongsToDifferentTransactionsException
        data = {
            'transaction_type': 1,
            'platform': 2,
            'client_id': 123,
            'user_id': 456,
            'total_amount': 900000,
            'currency': 'SGD',
            'provisions': [
                {
                    'expire_time': 1559883709,
                    'channel_id': 5005601,
                    'entity_id': 223610,
                    'channel_params': {}
                },
            ],
            'memo': 'memo',
            'extra_data': {},
        }
        response = self.app.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.json['meta']['code'], 1000)


if __name__ == '__main__':
    unittest.main()

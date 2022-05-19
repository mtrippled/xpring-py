"""
These tests exist just to confirm that new definitions are working as
expected.
"""

import pytest

from xpring import serialization

# yapf: disable
TRANSACTION_EXAMPLES = [
    (
        {
            'TransactionType': 'NFTokenMint',
            'Account': 'raFNCL4bUc8aSVNBc836y2ikMZoA56Bbvc',
            'Fee': '12',
            'TransferFee': 1,
            'TokenTaxon': 0,
            'Flags': 9,
            'URI': '4e4654206d696e742074657374',
        },
        {
            'TransactionType': 'NFTokenCreateOffer',
            'Account': 'rpquDbJEKHLnecncaEXGYnKHaNNksAcV8j',
            'Owner': 'rJYJSYY8Uz699JEUmsNHkkyW89kHJFb2yR',
            'Fee': '12',
            'NFTokenID': '00090001C0659777390FF0082067917C690C222E7D07CAF0F7BFFFB100000016',
            'Amount': '5',
            'Flags': 0,
            'Sequence': 70638780
        },
    )
]
# yapf: enable

@pytest.mark.parametrize(('transaction','transaction2'), TRANSACTION_EXAMPLES)
def test_serialize_transaction(transaction, transaction2):
    blob = serialization.serialize_transaction(transaction)
    assert blob.hex()
    blob = serialization.serialize_transaction(transaction2)
    assert blob.hex()

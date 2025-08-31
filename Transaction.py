from ecdsa import SigningKey, SECP256k1


# 封装一笔交易的信息
class Transaction:

    def __init__(self, sender, receiver, amount, contract=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.contract = contract

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "contract": self.contract,
        }
        
        
    def sign_transaction(self, private_key):
        # 签名交易
        private_key = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
        message = str(self.to_dict()).encode('utf-8')
        self.signature = private_key.sign(message).hex()
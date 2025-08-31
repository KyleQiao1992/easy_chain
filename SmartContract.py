class SmartContract:
    def __init__(self, code):
        self.code = code
        self.state = {}

    def execute(self, sender, receiver, amount):
        # 模拟执行智能合约代码
        exec(
            self.code,
            {
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "state": self.state,
            },
        )

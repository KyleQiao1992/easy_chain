import hashlib
import time


class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index  # 区块高度（编号）
        self.timestamp = timestamp  # 时间戳
        self.transactions = transactions  # 本区块包含的交易列表
        self.previous_hash = previous_hash  # 前一区块的哈希值
        self.hash = self.calculate_hash()  # 自身哈希值

    def calculate_hash(self):
        sha = hashlib.sha256()
        transactions_str = "".join(
            [f"{tx.sender}{tx.receiver}{tx.amount}" for tx in self.transactions]
        )
        sha.update(
            f"{self.index}{self.timestamp}{transactions_str}{self.previous_hash}".encode(
                "utf-8"
            )
        )
        return sha.hexdigest()

    def proof_of_work(self, difficulty):
        self.nonce = 0
        computed_hash = self.calculate_hash()
        print(
            f"Mining block with difficulty {difficulty}...calculating hash...computed_hash: {computed_hash}"
        )

        while not computed_hash.startswith("0" * difficulty):
            print(f"nonce: {self.nonce}, hash: {computed_hash}")
            self.nonce += 1
            computed_hash = self.calculate_hash()
            # 限制挖矿次数，避免无限循环
            if self.nonce >= 100:
                print("Mining failed, nonce exceeded limit.")
                return computed_hash

        return computed_hash

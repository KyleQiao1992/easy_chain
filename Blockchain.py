import hashlib
import time

from Block import Block
from SmartContract import SmartContract
from Transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # 区块链列表，初始含创世区块
        self.pending_transactions = []  # 待打包的交易池
        self.mining_reward = 100  # 挖矿奖励金额
        self.difficulty = 1  # 挖矿难度
        self.contract = {}  # 合约字典

    def create_genesis_block(self):
        return Block(
            0, time.time(), [], "0"
        )  # 创世区块：index=0，无交易，previous_hash="0"

    def get_latest_block(self):
        return self.chain[-1]  # 返回链尾块

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)  # 将新区块加入区块链

    def mine_pending_transactions(self, mining_reward_address):
        # 创建奖励交易
        reward_tx = Transaction(None, mining_reward_address, self.mining_reward)
        # 将奖励交易加入待挖矿交易列表
        self.pending_transactions.append(reward_tx)
        # 构造新块
        new_block = Block(
            len(self.chain),
            time.time(),
            self.pending_transactions,
            self.get_latest_block().hash,
        )
        print("Mining block...")
        # 重新计算hash
        new_block.hash = new_block.proof_of_work(self.difficulty)
        # 将新块加入区块链
        self.add_block(new_block)
        # 清空待挖矿交易列表
        self.pending_transactions = []

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.receiver == address:
                    balance += tx.amount
        return balance

    def deploy_contract(self, contract_code):
        contract = SmartContract(contract_code)
        contract_address = hashlib.sha256(contract_code.encode()).hexdigest()
        self.contract[contract_address] = contract
        return contract_address

    def call_contract(self, contract_address, sender, receiver, amount):
        contract = self.contract[contract_address]
        if contract:
            contract.execute(sender, receiver, amount)
            tx = Transaction(sender, receiver, amount, contract)
            self.create_transaction(tx)

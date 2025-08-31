from Blockchain import  Blockchain
import SmartContract
from Transaction import Transaction 

if __name__ == '__main__':
    # 使用示例
    blockchain = Blockchain()

    # # 创建交易
    # blockchain.create_transaction(Transaction("Alice", "Bob", 5))
    # blockchain.create_transaction(Transaction("Bob", "Alice", 10))

    # print("Pending transactions:")
    # # 挖矿
    # blockchain.mine_pending_transactions("Miner")

    # # 打印区块链
    # for block in blockchain.chain:
    #     print(f"index: {block.index}")
    #     print(f"timestamp: {block.timestamp}")
    #     print(f"transactions: {block.transactions}")
    #     print(f"previous_hash: {block.previous_hash}")
    #     print(f"hash: {block.hash}")
    #     print("-")

    # # 打印余额
    # print(f"Balance of Miner1: {blockchain.get_balance('Miner1')}")
    # print(f"Balance of Alice: {blockchain.get_balance('Alice')}")
    # print(f"Balance of Bob: {blockchain.get_balance('Bob')}")
    
    
    # 部署智能合约
    contract_code = "print('Hello, world!')"
    
    contract_address = blockchain.deploy_contract(contract_code)
    
    blockchain.call_contract(contract_address, "Alice", "Bob", 10)
    
    blockchain.mine_pending_transactions("Miner")
    

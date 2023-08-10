from web3 import Web3
import datetime

def getBlockData(blockNumber):
    apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98' 
    web3 = Web3(Web3.HTTPProvider(apiUrl))
    apiBlockData = web3.eth.get_block(blockNumber)

    blockData = {}
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()
    #Fetch the The unix timestamp for when the block was collated.  
    transactionTimeStamp = datetime.datetime.fromtimestamp(apiBlockData['timestamp'])
    #Convert the timestamp in the reabdable format like Y-M-H-M-S. 
    readableDate = transactionTimeStamp.strftime("%Y-%m-%d %H:%M:%S")
    blockData['timestamp'] = readableDate

    #Fetch the hexadecimal of the difficulty of ethereum block.
    blockData['difficulty'] = apiBlockData['difficulty']
    
    #Fetch the hexadecimal of the total difficulty of the chain until this ethereum block.
    blockData['totalDifficulty'] = apiBlockData['totalDifficulty']
    
    #Fetch the maximum gas allowed in ethereum block.
    blockData['gasLimit'] = apiBlockData['gasLimit']

    #Fetch the total used gas by all transactions in ethereum block.
    blockData['gasUsed'] = apiBlockData['gasUsed']


    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions
    allTransactions = []
    for transactionIndex in range(1, 11):
        transaction = {}
        transactionHash = apiBlockData['transactions'][transactionIndex]
        transaction['transactionHash'] = transactionHash.hex()
        transactionDetails = web3.eth.get_transaction(transactionHash)
        transaction['srno'] = transactionIndex
        transaction['receiver'] = transactionDetails['to']
        transaction['sender'] = transactionDetails['from']
        transactionAmount = int(transactionDetails['value']) / 10 ** 18 # Converting to ether
        transaction['amount'] = transactionAmount
        allTransactions.append(transaction)
    blockData['transactions'] = allTransactions
    return blockData


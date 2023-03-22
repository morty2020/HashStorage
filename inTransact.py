import json
from web3 import Web3, HTTPProvider


def insertTransaction(_address, _id, _hash):

    blockchainAddress = 'http://127.0.0.1:7545'
    web3 = Web3(HTTPProvider(blockchainAddress))
    compiledContractPath = 'build/contracts/HashStorage.json'
    deployedContractAddress = '0xca547958Be0b9B44e79bfaEc7B25F14A8276bec1'

    with open(compiledContractPath) as file:
        contractJson = json.load(file)

        contractAbi = contractJson['abi']

    contract = web3.eth.contract(address=deployedContractAddress, abi=contractAbi)
    senderAddress = _address
    txHash = contract.functions.insertHash(_id, _hash).transact({'from': web3.toChecksumAddress(senderAddress)})
    txReceipt = web3.eth.waitForTransactionReceipt(txHash)

    if txReceipt['status'] == 1:
        print('Transaction successful!')
    else:
        print('Transaction failed!')

'''
Demo to connect to AustriaPro node on 0bsnetwork (test)
and perform basic funtions: get infos about an address and an asset

C. Baumann 2019/1
'''
from time import sleep
import pywaves as pw
import shutil

NODE = 'http://88.99.145.156:7431'
NETWORK = 'testnet'
ADDR = '3Mthq2HwiU4V2AqUmCsT9BV6UTB9MUV5eU9'

pw.setNode(NODE, NETWORK)
ADDRESS = pw.Address(address=ADDR)

print('------------------------------------------');
print("Demo getting infos about an address and an asset:")
print('------------------------------------------');
print("Using the following address:")
print(ADDRESS.address)
print('------------------------------------------');
print("Infos about address:")
print(ADDRESS)

print('------------------------------------------');
balance = ADDRESS.balance()
print('Balance 0bsnetwork Coin: %s' % (balance / 100000000))

AProV1_ID = 'FH6t21twyAwDeR7J2TTp7zQEAq5rXBvyfWvK8QMvfRAZ'
balance = ADDRESS.balance(AProV1_ID)
print('Balance AustriaPro Token V1: %s' % (balance / 1000000))

AProV1 = pw.Asset(AProV1_ID)
print('------------------------------------------');
print('Info about Asset:')
print(AProV1)


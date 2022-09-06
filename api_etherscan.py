#pip install etherscan-python
from config import database_infos
from etherscan import Etherscan

eth = Etherscan(api_key=database_infos['api_key'])
#eth = Etherscan(YOUR_API_KEY, net="ropsten") caso queira acessar a testnet

###CHAMADAS###
#Obs.: Os valores de resultado estao a 10**18.

balanco_eth_carteira = eth.get_eth_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")

balanco_eth_varias_carteiras = eth.get_eth_balance_multiple(addresses=["0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a", "0x63a9975ba31b0b9626b34300f7f627147df1f526", "0x198ef1ec325a96cc354c7266a038be8b5c558f67"])

atividade_transferencia_erc20_por_carteira = eth.get_erc20_token_transfer_events_by_address(address='0x4e83362442b8d1bec281594cea3050c8eb01311c', startblock=0, endblock=999999999, sort='asc')

atividade_transferencia_erc721_por_carteira = eth.get_erc721_token_transfer_events_by_address(address='0x4e83362442b8d1bec281594cea3050c8eb01311c', startblock=0, endblock=999999999, sort='asc')

atividade_transferencia_erc721_por_carteira_paginado = eth.get_erc721_token_transfer_events_by_address_and_contract_paginated(contract_address='0x06012c8cf97bead5deae237070f9587f8e7a266d', address='0x6975be450864c02b4613023c2152ee0743572325', page=1, offset=100, sort='asc')

max_suply_contrato = eth.get_total_supply_by_contract_address(contract_address='0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')


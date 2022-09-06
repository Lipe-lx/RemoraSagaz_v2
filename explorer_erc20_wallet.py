from config import database_infos
from etherscan import Etherscan

eth = Etherscan(api_key=database_infos['api_key'])




atividade_transferencia_erc20_por_carteira = eth.get_erc20_token_transfer_events_by_address(
    address='0x4e83362442b8d1bec281594cea3050c8eb01311c',
    startblock=0,
    endblock=999999999,
    sort='asc'
)

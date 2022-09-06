from config import database_infos
from etherscan import Etherscan
import pandas as pd
from datetime import datetime

eth = Etherscan(api_key=database_infos['api_key'])

address = '0x4e83362442b8d1bec281594cea3050c8eb01311c'
startblock = 0
endblock = 999999999
sort = 'asc'

atividade_transferencia_erc20_por_carteira = eth.get_erc20_token_transfer_events_by_address(
    address=address,
    startblock=startblock,
    endblock=endblock,
    sort=sort
)

# Setando em um DataFrame
carteira_erc20_completa = pd.DataFrame(atividade_transferencia_erc20_por_carteira)

# Setando coluna timestamp
carteira_erc20_completa['timeStamp'] = pd.to_datetime(carteira_erc20_completa['timeStamp'], unit='s')

# Selecionando somente colunas de interesse
carteira_erc20 = carteira_erc20_completa[['tokenName', 'tokenSymbol',
                                          'contractAddress', 'timeStamp', 'from', 'to', 'value']]

# carteira_erc20['value'] = carteira_erc20['value'].astype(float)
carteira_erc20 = carteira_erc20.assign(value=carteira_erc20['value'].str.replace(',', '.').astype(float))


# PESQUISA DE HISTORICO DE MOEDAS/ENDEREÇOS ERC20 TRANSACIONADOS PELA CARTEIRA SELECIONADA SETADA PELO ENDEREÇO DE CONTRATO
# realizar uma pesquisa de endereços de moedas e verificar as transações realizadas pela carteira referente.
def filtro_contrato():

    carteira_erc20_filtrado = carteira_erc20.copy()
    carteira_erc20_filtrado = carteira_erc20_filtrado.set_index('contractAddress')

    e_address = str(input())
    filtro = carteira_erc20_filtrado.loc[e_address]
    return print(filtro)

filtro_contrato()
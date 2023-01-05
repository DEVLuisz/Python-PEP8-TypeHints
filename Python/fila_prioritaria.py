from typing import Dict, List, Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]

class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atentidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, diriga-se ao caixa: {caixa}')
    
    def estatistica(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atentidos)

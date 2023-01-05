from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(2023))
print(fila_teste.chama_cliente(1))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(16))
print(fila_teste_2.chama_cliente(8))
print(fila_teste_2.estatistica(EstatisticaResumida('16/08/2022', 120)))

teste_fabrica = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(16))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('16/08/2022', 120)))


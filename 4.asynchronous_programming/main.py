import random
import time
import asyncio

async def funcao_simulada():
    tempo = random.randint(1, 5)
    await asyncio.sleep(tempo)
    return tempo

async def executar():
    inicio_processamento = time.time()
    print('Processando...')

    primeira_funcao_async = asyncio.create_task(funcao_simulada())
    segunda_funcao_async = asyncio.create_task(funcao_simulada())
    terceira_funcao_async = asyncio.create_task(funcao_simulada())
    await asyncio.gather(primeira_funcao_async, segunda_funcao_async, terceira_funcao_async)

    final_processamento = time.time()
    return f'{final_processamento - inicio_processamento:.2f}'

if __name__ == "__main__":
    tempo_total = asyncio.run(executar())
    print(f"Tempo total de execução: {tempo_total} segundos")
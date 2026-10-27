import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

MODELO_LLM = "gemini-3.8-flash"
TENTATIVAS = 3
ESPERA_SEGUNDOS = 2


def gerar_resposta(instrucao_sistema, mensagem):
    cliente = genai.Client()

    for tentativa in range(1, TENTATIVAS + 1):
        try:
            interacao = cliente.interactions.create(
                model=MODELO_LLM,
                system_instruction=instrucao_sistema,
                input=mensagem,
            )
            return interacao.output_text
        except errors.ServerError:
            if tentativa == TENTATIVAS:
                raise
            time.sleep(ESPERA_SEGUNDOS * tentativa)

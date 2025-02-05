import openai
import os

# Configure sua chave da API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_imagem(prompt):
    """
    Gera uma imagem baseada no prompt usando a API OpenAI.
    
    Args:
        prompt (str): Descrição para gerar a imagem.
        
    Returns:
        str: URL da imagem gerada.
    """
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    url_imagem = response["data"][0]["url"]
    print(f"Imagem gerada com sucesso! Acesse em: {url_imagem}")
    return url_imagem

# Exemplo de uso
if __name__ == "__main__":
    tema = "A futuristic police robot patrolling a cyberpunk city at night, using an AI-powered drone for surveillance. Holograms display crime analysis in real-time, with neon lights reflecting off wet streets. The robot wears a high-tech armor with blue LED accents. The background shows a dystopian skyline with flying cars and digital billboards. The scene is cinematic and highly detailed."
    gerar_imagem(tema)

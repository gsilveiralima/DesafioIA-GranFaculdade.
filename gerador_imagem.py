import base64
import os
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-image-2"


def gerar_imagem(prompt: str, output_path: str = "imagem_gerada.png") -> Path:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Defina OPENAI_API_KEY no ambiente antes de executar.")

    client = OpenAI()
    result = client.images.generate(
        model=MODEL,
        prompt=prompt,
        size="1024x1024",
    )

    image_base64 = result.data[0].b64_json
    if not image_base64:
        raise RuntimeError("A API não retornou dados de imagem.")

    destination = Path(output_path)
    destination.write_bytes(base64.b64decode(image_base64))
    return destination


if __name__ == "__main__":
    tema = (
        "A futuristic robot exploring a fictional neon city at night, "
        "cinematic concept art, detailed lighting, no real person or insignia."
    )
    arquivo = gerar_imagem(tema)
    print(f"Imagem salva em: {arquivo.resolve()}")

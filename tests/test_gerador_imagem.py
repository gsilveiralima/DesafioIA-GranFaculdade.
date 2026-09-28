import base64
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import gerador_imagem


class GeradorImagemTest(unittest.TestCase):
    def test_requires_api_key(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(RuntimeError):
                gerador_imagem.gerar_imagem("teste")

    def test_decodes_generated_image_to_disk(self) -> None:
        payload = base64.b64encode(b"fake-png-bytes").decode("ascii")
        fake_client = MagicMock()
        fake_client.images.generate.return_value = SimpleNamespace(
            data=[SimpleNamespace(b64_json=payload)]
        )

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "image.png"
            with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=True):
                with patch("gerador_imagem.OpenAI", return_value=fake_client):
                    result = gerador_imagem.gerar_imagem("cenario de teste", str(output))

            self.assertEqual(result, output)
            self.assertEqual(output.read_bytes(), b"fake-png-bytes")
            fake_client.images.generate.assert_called_once_with(
                model=gerador_imagem.MODEL,
                prompt="cenario de teste",
                size="1024x1024",
            )


if __name__ == "__main__":
    unittest.main()

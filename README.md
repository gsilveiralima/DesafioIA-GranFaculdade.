# Desafio IA — Gran Faculdade

Projeto pequeno em Python criado para praticar geração de imagens por prompt utilizando a OpenAI API.

## Requisitos

- Python 3.10 ou superior;
- credencial da API configurada na variável de ambiente `OPENAI_API_KEY`.

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuração

Defina `OPENAI_API_KEY` no ambiente do sistema. Não coloque a credencial dentro do arquivo Python e não versione arquivos locais de configuração.

## Execução

```bash
python gerador_imagem.py
```

A saída é salva localmente em `imagem_gerada.png`.

## Estrutura

```text
gerador_imagem.py  exemplo principal
requirements.txt   dependência Python
README.md          instruções
```

## Segurança

- credenciais permanecem fora do Git;
- imagens geradas são ignoradas pelo repositório;
- o prompt de demonstração utiliza cenário fictício;
- revise custos e limites da API antes de automações em volume.

## Observação

APIs e modelos evoluem. Este exemplo deve ser revisado periodicamente contra a documentação oficial.

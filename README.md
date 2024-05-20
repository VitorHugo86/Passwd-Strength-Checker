# Password Strength Checker

Este projeto é um verificador de força de senha em Python. Ele avalia a força de uma senha com base em vários critérios e também verifica se a senha está em uma lista de senhas comuns.

## Funcionalidades

- Verifica se a senha contém:
  - Pelo menos 6 caracteres
  - Pelo menos uma letra minúscula
  - Pelo menos uma letra maiúscula
  - Pelo menos um dígito
  - Pelo menos um caractere especial
- Verifica se a senha está em uma lista de senhas comuns (`commons.txt`)
- Informa ao usuário a força da senha (fraca, média, forte)
- Permite que o usuário verifique várias senhas em sequência
- Tratamento de erros para entrada de usuário e leitura de arquivos

## Como Usar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/password-strength-checker.git
    cd password-strength-checker
    ```

2. Certifique-se de ter o Python instalado na sua máquina (versão 3.x).

3. Crie um arquivo `commons.txt` na raiz do projeto contendo uma lista de senhas comuns, com uma senha por linha.

4. Execute o script:
    ```bash
    python password_checker.py
    ```

5. Siga as instruções na tela para inserir e verificar senhas.

## Estrutura do Projeto

- `password_checker.py`: Arquivo principal do script que contém as funções para verificar a força da senha e a lógica principal do programa.
- `commons.txt`: Arquivo de texto contendo a lista de senhas comuns (uma senha por linha).

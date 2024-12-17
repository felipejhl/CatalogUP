# CatalogUP

## Descrição do Projeto

Este projeto é uma automação de cadastro de produtos em um sistema web utilizando Python e a biblioteca `pyautogui`. Ele foi desenvolvido com o objetivo de facilitar o registro em massa de produtos a partir de uma base de dados no formato CSV. O código realiza as seguintes etapas:

1. Abre o navegador e acessa o sistema de login.
2. Realiza o login automático.
3. Importa uma base de dados (arquivo `produtos.csv`).
4. Realiza o cadastro de cada produto no sistema, preenchendo os campos necessários.

### ✅Requisitos

- Python 3 instalado
- Bibliotecas: `pyautogui`, `pandas`
- Navegador Google Chrome

### 🔎Observações

Para que o código funcione corretamente, é necessário ajustar as coordenadas dos cliques conforme o monitor do usuário. Isso é feito com o arquivo `pegar_posicao.py`.

## Instruções para Ajuste de Coordenadas

1. **Baixe o repositório e extraia os arquivos em uma pasta local.**

2. **Rode o arquivo `pegar_posicao.py`:**

   - Execute o script e posicione o cursor do mouse no local onde deseja registrar a coordenada.
   - Após 5 segundos, as coordenadas X e Y do ponteiro serão exibidas no terminal.
   - Exemplo de saída:
     ```
     Point(x=390, y=291)
     ```

3. **Atualize as coordenadas no arquivo `main.py`:**

   - No código do `main.py`, todas as linhas que contêm coordenadas têm um comentário indicando o botão ou campo correspondente no sistema.
   - Substitua as coordenadas existentes pelas obtidas com o `pegar_posicao.py`.

4. **Teste o código:**

   - Certifique-se de que o código está interagindo corretamente com o sistema antes de realizar o cadastro em massa.

## Estrutura do Arquivo CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

| Coluna           | Descrição                               |
| ---------------- | --------------------------------------- |
| `codigo`         | Código do produto                       |
| `marca`          | Marca do produto                        |
| `tipo`           | Tipo do produto                         |
| `categoria`      | Categoria do produto                    |
| `preco_unitario` | Preço unitário do produto               |
| `custo`          | Custo do produto                        |
| `obs`            | Observações adicionais (campo opcional) |

## Como Executar o Projeto

1. Certifique-se de que todos os requisitos estão atendidos.

2. Ajuste as coordenadas conforme descrito acima.

3. Coloque o arquivo `produtos.csv` na mesma pasta do `main.py`.

4. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

5. Verifique se os produtos estão sendo cadastrados corretamente no sistema.

### ⚠️Como Cancelar a Execução

O `pyautogui` controla o mouse e o teclado automaticamente, o que pode dificultar o uso do computador enquanto o código está em execução. Para interromper o script:

- Mova o ponteiro do mouse para o **canto superior esquerdo** da tela. Essa ação automaticamente cancela a execução do `pyautogui`.

Caso o script continue rodando, pressione `Ctrl + C` no terminal onde o código foi executado.

## Avisos

- O tempo de espera (`time.sleep`) entre as interações pode precisar ser ajustado dependendo da velocidade da sua conexão com a internet e do desempenho do computador.
- Este projeto foi criado para fins educativos e não deve ser usado em sistemas de produção sem as devidas permissões.

## Autor

Felipe Jheimisson Lima de Oliveira

---

Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* ou entrar em contato!


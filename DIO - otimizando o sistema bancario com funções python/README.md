# Sistema Bancário Otimizado com Funções em Python

Este projeto estende e otimiza o sistema bancário monousuário inicial através da refatoração de código com funções estruturadas e modularizadas em Python. A arquitetura foi reprojetada para modularizar transações financeiras, gerenciamento de cadastros de usuários (clientes) e abertura de contas correntes associadas.

## Recursos e Melhorias Arquiteturais

A principal evolução desta versão é a separação lógica de responsabilidades e a aplicação de regras rígidas de assinatura de funções, divididas em argumentos puramente posicionais (*positional-only*) e argumentos puramente nomeados (*keyword-only*).

### Assinaturas de Funções e Contratos de Parâmetros

1. **Depósito (`depositar`)**:
   - Assinatura: `depositar(saldo, valor, extrato, /)`
   - Regra: Parâmetros passados **apenas por posição** (*positional-only*).
   - Retorno: Tupla contendo o saldo atualizado e o histórico de extrato atualizado.

2. **Saque (`sacar`)**:
   - Assinatura: `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`
   - Regra: Parâmetros passados **apenas por nome** (*keyword-only*).
   - Retorno: Tupla contendo o saldo atualizado, extrato atualizado e contagem de saques efetuados.

3. **Exibir Extrato (`exibir_extrato`)**:
   - Assinatura: `exibir_extrato(saldo, /, *, extrato)`
   - Regra: Saldo recebido como posicional e extrato como nomeado.

### Novos Recursos Cadastrais

Além das transações fundamentais, a aplicação conta com gerenciamento de cadastro de clientes e contas:

- **Cadastrar Usuário (`criar_usuario`)**:
   - Cria um registro contendo: Nome Completo, Data de Nascimento, CPF (único) e Endereço formatado.
   - Valida duplicidade de CPF para manter a integridade cadastral.

- **Criar Conta Corrente (`criar_conta`)**:
   - Cria uma conta corrente associando-a a um CPF de usuário existente.
   - Cada conta possui uma agência fixa ("0001") e um número sequencial único autoincrementado.

- **Listar Contas (`listar_contas`)**:
   - Exibe no console a listagem consolidada de todas as agências, contas correntes e os respectivos titulares cadastrados.

---

## Estrutura do Projeto

O diretório está estruturado com os seguintes componentes:

- `sistema_bancario_otimizado.py`: Arquivo principal com todas as definições de funções modulares e o loop da aplicação.
- `README.md`: Documentação técnica completa.

---

## Instruções de Uso

### Pré-requisitos
Para a execução do script, certifique-se de possuir o Python instalado localmente (versão 3.10 ou superior recomendada).

### Execução

Abra seu terminal no diretório do projeto e execute:

```bash
python sistema_bancario_otimizado.py
```

### Exemplo de Uso de Cadastros e Contas

1. Inicie cadastrando um novo cliente selecionando a opção `nu` (Novo usuário).
2. Forneça o CPF e os dados solicitados.
3. Crie uma conta corrente para esse cliente informando o mesmo CPF na opção `nc` (Nova conta).
4. Visualize a relação de contas registradas escolhendo a opção `lc` (Listar contas).
5. Realize operações financeiras normais (`d` para depósito, `s` para saque e `e` para extrato).

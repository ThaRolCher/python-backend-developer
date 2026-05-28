# Sistema Bancário em POO com Python - Controle de Data e Hora (Datetime)

Este projeto implementa melhorias na arquitetura orientada a objetos (POO) do sistema bancário monousuário, integrando o controle temporal das transações por meio do módulo nativo `datetime` do Python. O foco principal é a governança das operações diárias, impondo limites quantitativos e detalhamento cronológico de todas as ações.

---

## Funcionalidades Implementadas

### 1. Limite Diário de Transações
O sistema estabelece um limite de **10 transações diárias** para cada conta bancária. Esse limite abrange todas as operações que alteram o estado financeiro da conta (depósitos e saques bem-sucedidos).

### 2. Bloqueio e Notificação de Excesso
Caso o cliente tente realizar uma nova transação após atingir o limite de 10 movimentações em um mesmo dia calendário, a operação é preventivamente interrompida na camada de validação e o usuário recebe uma mensagem indicando que excedeu o volume de transações permitido para o dia em questão.

### 3. Registro Cronológico Detalhado no Extrato
Todas as movimentações gravadas no histórico da conta carregam um selo temporal contendo o instante exato da operação (data e hora no formato padrão brasileiro `dd-mm-aaaa hh:mm:ss`). Esses dados são impressos de forma organizada na emissão do extrato.

---

## Detalhes da Arquitetura do Sistema

O sistema é construído sobre o modelo de classes UML anterior, recebendo melhorias específicas de tratamento temporal:

### Camada de Modelo e Controle
- **`Cliente` (e `PessoaFisica`)**: A classe controladora de execução `Cliente` agora atua como interceptadora de transações. Antes de submeter a transação para o registro na conta através de `realizar_transacao`, o sistema consulta o histórico da conta receptora para verificar a quantidade de transações do dia.
- **`Historico`**: Responsável por armazenar a lista de transações e expor o método `transacoes_do_dia(self)`. Esse método analisa as transações no histórico, converte suas strings temporais de volta para objetos `date` por meio de `datetime.strptime` e compara com o dia atual obtido por `datetime.now().date()`.
- **`ContaCorrente`**: Valida os limites financeiros por saque (R$ 500,00) e o número de saques do dia (máximo de 3). Para a contagem dos saques diários, passa a utilizar o escopo restrito do método `transacoes_do_dia()`, garantindo que os saques de dias anteriores não influenciem o limite do dia atual.
- **`Transacao` (Interface Abstrata)**: Subdividida nas classes concretas `Deposito` e `Saque`, responsáveis por executar os devidos acréscimos/decréscimos de saldo e invocar o método `adicionar_transacao` do histórico apenas em cenários de sucesso operacional.

---

## Estrutura de Diretórios

```
sist_bancario_POO_python_datetime/
├── README.md                          # Este documento de especificações técnicas
└── sist_bancario_POO_python_datetime.py # Código-fonte principal com a lógica em Python
```

---

## Instruções de Execução

### Pré-requisitos
- Python 3.10 ou superior instalado no sistema operacional.

### Como Executar o Sistema

1. Abra um terminal de comandos.
2. Navegue até a pasta correspondente:
   ```bash
   cd "trilha-python-dio/sist_bancario_POO_python_datetime"
   ```
3. Execute o programa utilizando o interpretador Python:
   ```bash
   python sist_bancario_POO_python_datetime.py
   ```

### Guia de Teste e Validação

Para validar o controle de transações diárias no terminal interativo:

1. **Cadastrar Cliente**: Insira a opção `nu` (Novo usuário) e digite os dados pessoais requeridos.
2. **Criar Conta**: Use a opção `nc` (Nova conta) para associar uma conta ao CPF cadastrado.
3. **Efetuar Movimentações**: Execute 10 depósitos consecutivos utilizando a opção `d`.
4. **Verificar Limite**: Tente efetuar o 11º depósito (ou saque) e confirme se o sistema exibe a mensagem de limite de transações excedido.
5. **Emitir Extrato**: Escolha a opção `e` e certifique-se de que todas as 10 transações constam listadas com as datas e horas reais da simulação.

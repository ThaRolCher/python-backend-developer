# Sistema Bancário em Python

Este projeto consiste em uma implementação de sistema bancário monousuário desenvolvido em Python. A aplicação simula operações essenciais de uma conta corrente via terminal, como depósitos, saques e visualização de extratos detalhados, garantindo a integridade dos dados e o cumprimento de regras de negócios financeiras.

## Recursos do Sistema

O sistema oferece as seguintes operações de conta:

1. **Depósito (`Depositar`)**:
   - Permite o aporte de fundos na conta corrente.
   - Restringe valores de entrada a números estritamente positivos.
   - Armazena o histórico da transação para exibição futura no extrato.

2. **Saque (`Sacar`)**:
   - Permite a retirada de fundos, sujeita a validações de segurança e limites de saldo.
   - Aplica um limite máximo de R$ 500,00 por transação individual.
   - Impõe uma cota máxima de até 3 saques diários.
   - Registra cada retirada no histórico do extrato.

3. **Extrato (`Extrato`)**:
   - Exibe a lista completa de todas as movimentações financeiras executadas na sessão.
   - Mostra o saldo consolidado atualizado em tempo real.
   - Apresenta uma mensagem informativa caso nenhuma movimentação tenha sido registrada.

4. **Sair (`Sair`)**:
   - Finaliza a sessão do terminal de forma segura.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma dentro do repositório:

- `sistema_bancario.py`: Código-fonte principal com a lógica de execução e tratamento de erros do menu de transações.
- `README.md`: Documentação técnica descrevendo as especificações e instruções de uso.

---

## Execução e Requisitos

### Pré-requisitos

Para executar este sistema, é necessário ter o Python instalado na máquina local (versão 3.10 ou superior recomendada).

### Instruções de Execução

Abra um terminal na pasta onde o arquivo `sistema_bancario.py` está localizado e execute o seguinte comando:

```bash
python sistema_bancario.py
```

### Exemplo de Uso

Ao iniciar o programa, o menu interativo será exibido no console:

```text
================ MENU ================
[d]     Depositar
[s]     Sacar
[e]     Extrato
[q]     Sair
=>
```

Digite a letra correspondente à operação desejada e pressione `Enter` para interagir com o console. Todas as mensagens de erro ou sucesso são formatadas de maneira clara para fornecer feedback imediato de cada transação.

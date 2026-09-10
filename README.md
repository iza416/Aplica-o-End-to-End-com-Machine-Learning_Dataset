# Sistema End-to-End de Detecção de Fraude em Cartões de Crédito

Aplicação de Machine Learning desenvolvida para demonstrar o ciclo de vida completo de um modelo de classificação: desde a preparação dos dados e treinamento até a disponibilização de uma API transacional com interface web.

---

## 📌 1. Visão Geral e Problema de Negócio

O objetivo desta solução é analisar o risco de compras em cartões de crédito em tempo real. Identificar transações suspeitas no momento da autorização protege os usuários contra prejuízos e reduz custos operacionais de contestação para as instituições financeiras.

A solução aplica regras de corte baseadas na probabilidade predita pelo modelo:
* **Risco Baixo:** Aprovação imediata da compra.
* **Risco Moderado:** Solicitação de autenticação em duas etapas (biometria).
* **Risco Crítico:** Bloqueio preventivo da operação.

---

## 📊 2. Dataset e Variáveis

* **Dataset:** `card_transdata.csv`
* **Variável-alvo (`target`):** `fraud`
  * `0`: Transação legítima
  * `1`: Transação fraudulenta

### Atributos de Entrada (`features`):
| Variável | Descrição |
| :--- | :--- |
| `distance_from_home` | Distância da casa do portador (km) |
| `distance_from_last_transaction` | Distância da última transação registrada (km) |
| `ratio_to_median_purchase_price` | Razão do valor atual em relação à mediana histórica do cliente |
| `repeat_retailer` | Compra em lojista frequente (1 = Sim, 0 = Não) |
| `used_chip` | Transação com uso de chip físico (1 = Sim, 0 = Não) |
| `used_pin_number` | Transação com digitação de senha (1 = Sim, 0 = Não) |
| `online_order` | Compra realizada via internet (1 = Sim, 0 = Não) |

### Como Executar o Projeto:

```bash
git clone cd
pip install pandas scikit-learn joblib fastapi uvicorn jinja2
python train_model.py
uvicorn app:app --reload
Abra através do navegador e faça o teste para obter as respostas.

---

### Qual dataset foi escolhido e qual problema ele representa?

O Dataset que escolhi foi o **Credit card fraud**: https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud

Ele representa o problema de identificação em tempo real de transações fraudulentas em cartões de crédito.

---

### Qual é a variável-alvo (target) que será prevista?

A coluna `fraud`, indicador de fraude.

---

### Quais são as classes possíveis?

* **`0`**: Transação legítima realizada pelo titular do cartão
* **`1`**: Transação com fraude

---

### Quais informações serão utilizadas como entrada do modelo?

* **`distance_from_home`**: Distância (em km) entre a residência cadastrada do titular e o local da transação.
* **`distance_from_last_transaction`**: Distância (em km) em relação ao ponto onde a última transação foi feita.
* **`ratio_to_median_purchase_price`**: Razão entre o valor da compra atual e o valor mediano histórico do portador, por exemplo $ 1,0 é o gasto típico $ 10 é muito maior (dez vezes maior) do que ele gasta.
* **`repeat_retailer`**: Indica se o cliente já comprou anteriormente naquele estabelecimento comercial.
* **`used_chip`**: Indica se a compra usou chip físico.
* **`used_pin_number`**: Indica se foi digitada a senha.
* **`online_order`**: Indica se a transação ocorreu em ambiente virtual/e-commerce ou presencial.

---

### Quem utilizaria essa aplicação e com qual finalidade?

**Gateways de Pagamento**

Com a finalidade de detectar fraudes, saber se liberam a compra, pedem verificação ou liberam.

---

### O que a aplicação fará com a classificação produzida pelo modelo?

Ao invés de retornar 0 ou 1 a aplicação indica a probabilidade de fraude, em três caminhos e de forma visual:

* **Verde:** Aprovação direta.
* **Laranja:** Transações em zonas de risco não são canceladas. O sistema solicita confirmação do usuário via biometria facial.
* **Vermelho:** Transações com alta probabilidade de fraude são bloqueadas.

---

### Como seria a interface ou experiência de uso dessa solução?

Uma interface onde o operador ou simulador insere os dados da transação em um formulário e recebe imediatamente o parecer em forma de card de alerta colorido (verde para aprovado, laranja para confirmação e vermelho para bloqueio).

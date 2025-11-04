**README — Cálculo de Métricas de Avaliação de Aprendizado / Evaluation Metrics Calculation Project**

---

### 🇧🇷 Português

#### Descrição

Este projeto tem como objetivo calcular as principais métricas utilizadas na avaliação de modelos de **classificação de dados**. As métricas implementadas são **acurácia**, **sensibilidade (recall)**, **especificidade**, **precisão** e **F1-score**.

Através da implementação manual e também com o uso das funções disponíveis na biblioteca `scikit-learn`, o projeto busca demonstrar o funcionamento prático de cada uma dessas métricas, baseando-se em uma **matriz de confusão** previamente definida.

#### Fórmulas principais

* **Acurácia:** (VP + VN) / (VP + VN + FP + FN)
* **Sensibilidade (Recall):** VP / (VP + FN)
* **Especificidade:** VN / (VN + FP)
* **Precisão (Precision):** VP / (VP + FP)
* **F1-Score:** 2 × (Precisão × Recall) / (Precisão + Recall)

Onde:

* VP = Verdadeiro Positivo
* VN = Verdadeiro Negativo
* FP = Falso Positivo
* FN = Falso Negativo

#### Exemplo de código

```python
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

# Dados de exemplo
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

print("Acurácia:", accuracy_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("Precisão:", precision_score(y_true, y_pred))
print("F1-Score:", f1_score(y_true, y_pred))
print("Matriz de confusão:\n", confusion_matrix(y_true, y_pred))
```

#### Objetivo educacional

O propósito é compreender o papel de cada métrica e sua importância na avaliação do desempenho de classificadores, principalmente em contextos onde há **desequilíbrio de classes**.

---

### 🇬🇧 English 

#### Description

This project aims to calculate the main metrics used for evaluating **data classification models**. The implemented metrics are **accuracy**, **recall (sensitivity)**, **specificity**, **precision**, and **F1-score**.

By implementing both manual formulas and the built-in functions from the `scikit-learn` library, this project demonstrates how each metric operates in practice, based on a predefined **confusion matrix**.

#### Main formulas

* **Accuracy:** (TP + TN) / (TP + TN + FP + FN)
* **Recall (Sensitivity):** TP / (TP + FN)
* **Specificity:** TN / (TN + FP)
* **Precision:** TP / (TP + FP)
* **F1-Score:** 2 × (Precision × Recall) / (Precision + Recall)

Where:

* TP = True Positive
* TN = True Negative
* FP = False Positive
* FN = False Negative

#### Code example

```python
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

# Example data
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("F1-Score:", f1_score(y_true, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
```

#### Educational goal

The purpose is to understand the role and importance of each metric when assessing classifier performance, especially in scenarios with **class imbalance**.

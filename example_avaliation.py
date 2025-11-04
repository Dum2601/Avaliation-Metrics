from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

# Dados usados como exemplo
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

print("Acurácia:", accuracy_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("Precisão:", precision_score(y_true, y_pred))
print("F1-Score:", f1_score(y_true, y_pred))
print("Matriz de confusão:\n", confusion_matrix(y_true, y_pred))

# P4 (Medium) — ML Training Log Line
# Hardcode: epoch = 3, loss = 0.4523187, accuracy = 0.87324.
# Produce this exact output using a single f-string:
# Epoch 003 | Loss: 0.4523 | Acc: 87.32%

epoch = 3
loss = 0.4523187
accuracy = 0.87324

print(f"Epoch {epoch:03}  |  Loss: {loss:.4f}  |  Acc: {accuracy:.2%}")
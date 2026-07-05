# Medium1(M1) — Early Stopping Simulator

# Hardcode this loss sequence:
# pythonlosses = [0.9, 0.75, 0.62, 0.55, 0.51, 0.49, 0.48, 0.47, 0.465, 0.462]
# target = 0.5
# Iterate through losses using for with enumerate.
# Break out as soon as loss drops below target,
# printing "converged at epoch <i> with loss <value>".

# Use the loop's else clause to print "did not converge"
# if the loop finished without breaking.

# Verification: With target = 0.5, your code should print convergence at epoch 5 (loss 0.49).
# Change target = 0.4 and rerun — it should print "did not converge."
# If your for-else fires incorrectly (or never),
# the construct isn't wired right.

pythonlosses = [0.9, 0.75, 0.62, 0.55, 0.51, 0.49, 0.48, 0.47, 0.465, 0.462]
target = 0.5

for i, loss in enumerate(pythonlosses):
    if loss < target:
        print(f"converged at epoch {i} with loss {loss}")
        break
    else:
        print("did not converge")
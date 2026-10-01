import dill

with open("artifacts/model.pkl", "rb") as f:
    model = dill.load(f)

print(type(model))
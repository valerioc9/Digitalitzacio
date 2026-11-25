cotxe = {"marca": "Seat", "model": "Ibiza", "color": "vermell", "any": 2019}

print(cotxe)
cotxe["any"] = 2020
model = cotxe.pop("model")
print(model)
print(cotxe)
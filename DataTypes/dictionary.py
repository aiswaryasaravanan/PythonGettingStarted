# dictionary

dictionary1 = {11: "Aishu", 12: "Swathi", 3: "Raji"}
dictionary2 = {"z": "Aishu", "s": (
    ["Shivu", "Swathi", "Sabeena"], ["Aishu", "Abi"])}  # tuple of list as value

print(dictionary1)
print(dictionary1.keys())
print(dictionary2.values())

print(dictionary2["z"])
dictionary2["z"] = "AishuSaravanan"
print(dictionary2["z"])
del dictionary2["z"]

capitals = {"USA": "Washington dc",
            "India":"New Dehli",
            "China":"Beijing",
             "Russia":"Moscow"}
print(capitals.get("Germany"))
print(capitals["Russia"])
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)
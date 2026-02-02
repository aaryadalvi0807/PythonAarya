test1 = {"Amit": 70, "Neha": 85}
test2 = {"Amit": 80, "Neha": 90}

merged = {
    name: (test1[name], test2[name])
    for name in test1
}

print(merged)

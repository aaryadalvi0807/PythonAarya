attendance = {"Ravi": ["P", "A", "P"], "Neha": ["P", "P", "P"]}

present_days = {
    name: records.count("P")
    for name, records in attendance.items()
}

print(present_days)

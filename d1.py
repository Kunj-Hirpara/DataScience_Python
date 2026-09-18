patient = {
    "p1": {
        "name": "abc",
        "bp": 120,
        "bsugar": 90,
        "colesterol": 180
    },
    "p2": {
        "name": "def",
        "bp": 130,
        "bsugar": 100,
        "colesterol": 200
    },
    "p3": {
        "name": "ghi",
        "bp": 140,
        "bsugar": 110,
        "colesterol": 220
    }
}
print("----- Patient Records -----")
for pid,data in patient.items():
    print("Patient ID: ", pid)
    print("Patient Name: ", data["name"])
    print("Blood Pressure: ", data["bp"])
    print("Blood Sugar: ", data["bsugar"])
    print("Cholesterol: ", data["colesterol"])
    print()

scores = {}

print("----- Total Health Scores -----")
for pid,data in patient.items():
    total = data["bp"] + data["bsugar"] + data["colesterol"]
    scores[pid] = total
    print(pid, ":", total)

# Healthiest patient - lowest total
healthiest = min(scores, key=scores.get)

# Critical patient - highest total
critical = max(scores, key=scores.get)

print("\nHealthiest Patient: ")
print(healthiest, "-", patient[healthiest]["name"])
print("Total Score: ", scores[healthiest])

print("\nCritical Patient: ")
print(critical, "-", patient[critical]["name"])
print("Total Score: ", scores[critical])
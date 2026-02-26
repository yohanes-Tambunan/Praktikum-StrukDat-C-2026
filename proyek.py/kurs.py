from tabulate import tabulate
kurs = [
    {"Kode": "USD", "Kurs": 16.875},
    {"Kode": "EUR", "Kurs": 19.995},
    {"Kode": "SGD", "Kurs": 13.360},
    {"Kode": "JPY", "Kurs": 109}
]
print(tabulate(kurs, headers="keys", tablefmt="grid"))
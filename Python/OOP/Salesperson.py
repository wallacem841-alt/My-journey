day_sales = {
    "Alice": [120.50, 300.00, 45.90],
    "Bob": [89.99, 150.00],
    "Charlie": [500.00, 75.25, 60.00, 220.40]
}

class Salesperson:
    def __init__(self, sales):
        self.sales = sum(sales)
        self.commition = self.sales * 0.05

today_sales = {}

for i in day_sales:
    salesperson = Salesperson(day_sales[i])
    today_sales[i] = {}
    today_sales[i]["Sales"] = salesperson.sales
    today_sales[i]["Commition"] = salesperson.commition

print(today_sales)
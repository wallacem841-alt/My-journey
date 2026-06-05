import pandas as pd

db = pd.read_excel("website_sales_report.xlsx")

'''for i, row in db.iterrows():
    print(row["Date"])'''

class Sale:
    def __init__(self, sale):
        self.sale = sale
        self.customer = self.sale["CustomerID"]
        self.revenue = self.sale["Revenue"]

    @property
    def status_check(self):
        if self.sale["Status"] == "Completed":
            return 1
        else:
            return 0


'''test = Custumer(db.iloc[0])

print(test.status_check)'''

temporary = {}

for _, row in db.iterrows():
    t = Sale(row)

    if t.customer not in temporary:
        temporary[t.customer] = []

    if t.status_check == 1:
        temporary[t.customer].append(t.revenue)

temporary2 = []

for i in temporary:
    if sum(temporary[i]) >= 500:
        temporary2.append(i)

print(temporary2)
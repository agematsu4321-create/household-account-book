

class Kakeibo:
    def __init__(self):
        self.transactions = []


    

    def add_transaction(self, date, amount, category, kind):
        tx = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "kind" : kind
        }
        self.transactions.append(tx)

    def list_transactions(self):
        return self.transactions


if __name__ == "__main__":
    asyncio.run(init_db())
    new_id = asyncio.run(add_transaction(date(2025, 12, 16), 1200, "食費", "expense"))
    rows = asyncio.run(list_transactions())
    print("inserted id:", new_id)
    print("rows:", [(r.id, r.tx_date, r.amount, r.category, r.kind) for r in rows])

     
        
def monthly_summary(rows, month: str):
    income_total = 0
    expense_total = 0
    by_category = {}

    for tx in rows:
        if tx.kind == "income":
            income_total += tx.amount
        elif tx.kind == "expense":
            expense_total += tx.amount
            by_category[tx.category] = by_category.get(tx.category, 0) + tx.amount

    return {
        "month": month,
        "income_total": income_total,
        "expense_total": expense_total,
        "balance": income_total - expense_total,
        "by_category": by_category,
    }

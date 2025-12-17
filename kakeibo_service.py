# kakeibo_service.py
from kakeibo import monthly_summary

import asyncio
from datetime import date

from sqlalchemy import select

from kakeibo_db import SessionLocal, Transaction, init_db


class KakeiboDB:
    async def add_transaction(self, tx_date: date, amount: int, category: str, kind: str) -> int:
        async with SessionLocal() as session:
            tx = Transaction(tx_date=tx_date, amount=amount, category=category, kind=kind)
            session.add(tx)
            await session.commit()
            await session.refresh(tx)
            return tx.id

    async def list_transactions(self):
        async with SessionLocal() as session:
            res = await session.execute(select(Transaction).order_by(Transaction.id.desc()))
            return res.scalars().all()


async def main():
    await init_db()

    k = KakeiboDB()
    #new_id = await k.add_transaction(date(2025, 12, 16), 1200, "食費", "expense")
    rows = await k.list_transactions()
    print(monthly_summary(rows, "2025-12"))

    print("inserted id:", new_id)
    print("rows:", [(r.id, r.tx_date, r.amount, r.category, r.kind) for r in rows])


if __name__ == "__main__":
    asyncio.run(main())
    rows = await k.list_transactions(date(2025, 12, 1), date(2026, 1, 1))
print(monthly_summary(rows, "2025-12"))

    


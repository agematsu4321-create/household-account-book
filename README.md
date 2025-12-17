# Household Account Book (Backend)

Python と SQLAlchemy（Async）を用いて作成した  
**家計簿アプリのバックエンド実装サンプル**です。

取引データを SQLite に保存し、  
**月別の収支サマリー（収入・支出・残高・カテゴリ別集計）**を算出できます。

---

## Why this project

未経験からバックエンドエンジニアを目指す中で、  
以下を意識して作成しました。

- DB設計と ORM の基礎理解
- 非同期処理（AsyncSession）の実践
- 業務ロジックと DB 操作の責務分離
- 小規模でも「実務を想定した構成」

---

## Features

- 収入・支出データの登録
- SQLite によるデータ永続化
- 月別収支サマリーの算出
  - 収入合計
  - 支出合計
  - 残高
  - カテゴリ別支出集計

---

## Tech Stack

- Python 3.10
- SQLAlchemy（Async）
- SQLite
- asyncio
- Git / GitHub

---

## Project Structure

```text
.
├─ kakeibo.py          # 集計ロジック（月次サマリー）
├─ kakeibo_db.py       # DB定義・初期化（SQLAlchemy）
├─ kakeibo_service.py  # サービス層（DB操作の実行）
├─ requirements.txt
├─ .gitignore
└─ README.md


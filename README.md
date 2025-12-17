Household Account Book (Backend)
Python と SQLAlchemy（Async）を用いて作成した、
家計簿アプリのバックエンド実装サンプルです。
取引データを SQLite データベースに保存し、
**月別の収支サマリー（収入・支出・残高・カテゴリ別集計）**を算出できます。
本プロジェクトは 業務を想定したバックエンド設計・実装力の可視化を目的としています。
Features
収入・支出データの登録
SQLite によるデータ永続化
月別サマリーの算出
収入合計
支出合計
残高
カテゴリ別支出集計
非同期 SQLAlchemy（AsyncSession）による DB 操作
ロジック・DB・サービス層の責務分離
Tech Stack
Python 3.10
SQLAlchemy (Async)
SQLite
asyncio
Git / GitHub
Project Structure
.
├── kakeibo.py          # 集計ロジック（月次サマリー）
├── kakeibo_db.py       # DB定義・初期化（SQLAlchemy）
├── kakeibo_service.py  # サービス層（DB操作の実行）
├── .gitignore
└── README.md
How to Run
1. リポジトリをクローン
git clone https://github.com/agamatsu4321-create/household-account-book.git
cd household-account-book
2. 依存関係をインストール
pip install sqlalchemy aiosqlite greenlet
3. 実行
python kakeibo_service.py
実行すると以下が行われます：
データベース初期化
取引データの登録
月別サマリーの出力
Example Output
{
  'month': '2025-12',
  'income_total': 0,
  'expense_total': 9600,
  'balance': -9600,
  'by_category': {
    '食費': 9600
  }
}
Design Notes
DBアクセスと集計ロジックを分離
DB操作：kakeibo_db.py, kakeibo_service.py
ビジネスロジック：kakeibo.py
実務を想定し、非同期 DB セッションを採用
API化（FastAPI など）は今後の拡張として想定
Future Improvements
FastAPI による REST API 化
月指定・期間指定での集計
ユーザー単位のデータ管理
テストコードの追加
Purpose
本リポジトリは
Python バックエンド開発の基礎力（設計・DB・非同期処理）を示すポートフォリオとして作成しています。

# Todo API - FastAPI + SQLAlchemy 練習專案

這是一個使用 **FastAPI** 和 **SQLAlchemy** 建立的 Todo 管理 API 專案，適合初學者學習現代 Python Web 開發技術。

## 專案簡介

本專案實作了一個完整的 Todo 管理系統，包含以下功能：

- 建立新的 Todo 項目
- 查詢特定 Todo 項目
- 更新 Todo 項目內容
- 刪除 Todo 項目
- 資料庫連線測試

## 技術架構

### 核心技術

- **FastAPI**: 現代、高效能的 Python Web 框架
- **SQLAlchemy**: Python 最受歡迎的 ORM（物件關聯對映）工具
- **Asyncpg**: 高效能的 PostgreSQL 非同步驅動程式
- **Pydantic**: 資料驗證和序列化工具
- **Uvicorn**: ASGI 伺服器，用於執行 FastAPI 應用程式

### 專案結構

```makefile
todo-fastapi-sqlalchemy/
├── app/                    # 主要應用程式目錄
│   ├── __init__.py
│   ├── main.py             # FastAPI 應用程式入口點
│   ├── models.py           # SQLAlchemy 資料模型
│   ├── schemas.py          # Pydantic 資料驗證模型
│   ├── crud.py             # 資料庫操作邏輯
│   ├── database.py         # 資料庫連線設定
│   └── config.py           # 環境變數設定
├── pyproject.toml          # 專案依賴管理
├── uv.lock                 # 依賴版本鎖定檔案
└── README.md               # 專案說明文件
```

## 🚀 快速開始

### 前置需求

- Python 3.10 或更高版本
- PostgreSQL 資料庫
- uv 套件管理工具（推薦）或 pip

### 1. 複製專案

```bash
git clone git@github.com:chienchuanw/todo-fastapi-sqlalchemy.git
cd todo-fastapi-sqlalchemy
```

### 2. 安裝依賴

使用 uv（推薦）：

```bash
uv sync
```

或使用 pip：

```bash
pip install -e .
```

### 3. 設定環境變數

建立 `.env` 檔案並設定資料庫連線：

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/todo_db
```

**重要提醒**：

- 請將 `username` 替換為你的 PostgreSQL 使用者名稱
- 請將 `password` 替換為你的 PostgreSQL 密碼
- 請將 `todo_db` 替換為你想使用的資料庫名稱

### 4. 啟動應用程式

```bash
uvicorn app.main:app --reload
```

成功啟動後，你會看到類似以下的訊息：

```log
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 📚 API 使用說明

### 基本 URL

```http
http://127.0.0.1:8000
```

### API 端點

#### 1. 測試資料庫連線

```http
GET /test
```

**回應範例**：

```json
{
  "status": "ok"
}
```

#### 2. 建立新的 Todo

```http
POST /todo/create
Content-Type: application/json

{
  "title": "學習 FastAPI",
  "description": "完成 FastAPI 教學課程",
  "completed": false
}
```

#### 3. 查詢特定 Todo

```http
GET /todo/{todo_id}
```

**範例**：`GET /todo/1`

#### 4. 更新 Todo

```http
PATCH /todo/{todo_id}
Content-Type: application/json

{
  "title": "學習 FastAPI（已更新）",
  "completed": true
}
```

#### 5. 刪除 Todo

```http
DELETE /todo/{todo_id}
```

### 互動式 API 文件

FastAPI 自動產生互動式 API 文件，啟動伺服器後可以透過以下網址存取：

- **Swagger UI**: <http://127.0.0.1:8000/docs>

## 常見問題

### Q: 啟動時出現資料庫連線錯誤

A: 請檢查：

1. PostgreSQL 是否正在執行
2. `.env` 檔案中的資料庫連線資訊是否正確
3. 資料庫是否存在

### Q: 如何重設資料庫？

A: 刪除資料庫中的 `todos` 資料表，重新啟動應用程式會自動建立。

### Q: 如何新增更多欄位？

A:

1. 在 `models.py` 中修改 `Todo` 類別
2. 在 `schemas.py` 中更新對應的 Pydantic 模型
3. 在 `crud.py` 中調整相關的資料庫操作

## 延伸貢獻

如果有不清楚的地方，希望能更深入理解，歡迎提交 issue 進行詢問，我都會盡力解答。

**祝學習愉快！** 🎉

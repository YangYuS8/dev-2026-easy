# FastAPI 任务服务练习仓库（Easy Beginner）

## 项目简介

这是一个更适合初学者的后端练习仓库，主题是一个基于 `FastAPI + SQLite` 的任务服务。

这个仓库不是完整成品，而是一个保留了少量缺口的练习项目。你需要阅读说明、尝试运行项目、定位问题，并完成至少一个真实修复。

## 技术栈

- Python 3.11+
- FastAPI
- SQLite
- pytest
- Docker Compose（可选）

## 推荐完成顺序

1. 先看 `TASK.md`
2. 再看 `.env.example`
3. 再看 `app/` 和 `tests/`
4. 最后尝试运行项目

## 启动方式

### 方式一：本地运行（推荐）

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 方式二：Docker Compose（可选）

```bash
cp .env.example .env
docker compose up --build
```

## 可以怎么验证

```bash
pytest
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/tasks
```

## 主要接口

- `GET /health`
- `GET /tasks`
- `POST /tasks`
- `PATCH /tasks/{task_id}/status`

## 这份版本主要考察什么

- 会不会阅读项目说明
- 会不会运行一个 Python 项目
- 会不会看懂报错
- 会不会完成至少一个真实修复
- 会不会记录自己做了什么

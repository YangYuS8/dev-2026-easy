# FastAPI + PostgreSQL 任务服务练习仓库（Easy）

## 项目简介

这是一个面向初学者的后端练习仓库，主题是 `FastAPI + PostgreSQL` 的任务服务。

这个仓库不是完整成品，而是一个带有少量缺口的练习项目。你需要阅读说明、尝试运行项目、定位问题，并完成至少一个真实修复。

## 技术栈

- Python 3.11+
- FastAPI
- PostgreSQL
- Docker / Docker Compose
- pytest

## 目录结构

```text
.
├── app/
├── docs/
├── tests/
├── .env.example
├── docker-compose.yml
├── TASK.md
├── report.md
├── ai-usage.md
└── README.md
```

## 推荐完成顺序

1. 先看 `TASK.md`
2. 再看 `docker-compose.yml`
3. 再看 `.env.example`
4. 最后看 `app/` 和 `tests/`

## 启动方式

### 方式一：Docker Compose（推荐）

```bash
cp .env.example .env
docker compose up --build
```

### 方式二：本地运行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

如果你的本机环境暂时不完整，也没关系。你可以先记录遇到的问题，再尝试修复。

## 可以怎么验证

例如：

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

## 这份 easy 版本的目标

这份仓库主要希望你练习：

- 阅读项目说明
- 尝试启动项目
- 看懂报错
- 完成至少一个真实修复
- 记录自己的排查过程

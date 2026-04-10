# FastAPI + PostgreSQL 任务服务考核起始仓库

## 项目简介

这是一个用于工程化与 AI 协同开发考核的起始仓库，主题是 `FastAPI + PostgreSQL` 任务服务。

仓库当前是半成品状态，不是完整标准答案。你需要阅读文档、启动项目、定位问题、补全功能，并以 Pull Request 形式提交结果。

## 技术栈

- Python 3.11+
- FastAPI
- PostgreSQL
- psycopg
- Docker
- Docker Compose
- pytest

## 目录结构

```text
.
├── app/
│   ├── api/
│   ├── config.py
│   ├── crud.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── docs/
│   └── overview.md
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_schemas.py
│   └── test_tasks.py
├── .env.example
├── Dockerfile
├── TASK.md
├── ai-usage.md
├── docker-compose.yml
├── report.md
└── requirements.txt
```

## 本地运行方式

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

说明：本地运行前请先确认 PostgreSQL 可连接，以及 `.env` 中的配置与本机环境一致。

## Docker Compose 运行方式

```bash
cp .env.example .env
docker compose up --build
```

说明：考核要求中明确需要使用 `Docker Compose` 方式完成一次启动与排查。

## API 概览

- `GET /health`
- `GET /tasks`
- `POST /tasks`
- `PATCH /tasks/{task_id}/status`

任务接口当前以 `tasks` 列表和单个 task 对象为主；`/health` 仍保留较简单的返回结构。

当前任务状态字段使用以下取值：`pending`、`in_progress`、`done`。

## 建议先看哪些文件

1. `TASK.md`
2. `docs/overview.md`
3. `docker-compose.yml`
4. `.env.example`
5. `app/config.py`
6. `app/main.py`
7. `tests/test_tasks.py`

## 排查提示

这是一个用于考核的半成品仓库，问题不一定只出现在 Python 代码中。

排查时建议同时关注以下几个方面：

- 文档说明是否和当前实现一致
- 环境变量模板是否覆盖了运行所需配置
- `Docker Compose` 配置是否和服务实际依赖一致
- 应用默认值是否和当前运行环境匹配
- 数据库连接相关配置是否前后一致
- 启动日志、报错信息和测试输出是否给出了直接线索

请注意，文档、配置文件和代码默认值之间可能并不是完全一致的。建议交叉阅读 `TASK.md`、`docker-compose.yml`、`.env.example`、`app/config.py`、测试文件以及启动日志，再做判断。

## Half-Finished Assessment Note

这是一个故意保留部分缺口的半成品 assessment starter。

- 有些配置或启动细节需要你自己检查
- 有些 Python 行为还不完整
- 测试只覆盖基础路径，不覆盖所有待修复点

请把它当成“接手他人半成品仓库”的练习，而不是从零创建项目。

## Existing Issues / Features Note

当前仓库已经具备基础任务列表、任务创建、状态更新、健康检查等能力，但仍存在若干待确认问题与待完成功能。

- 现有实现可以帮助你快速理解项目结构
- 文档不会直接写出所有需要修改的点
- 你需要自己定位至少部分环境、配置或代码问题

正式要求、提交方式和验收内容请查看 `TASK.md`。

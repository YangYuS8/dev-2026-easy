# dev-2026-05

## 题目名称

Python TCP 初学者任务：实现一个简单的文本协议服务器与客户端

## 这是一道什么题

这道题主要考查：

- Python 基础语法
- TCP Socket 基础使用
- 服务端与客户端基础通信
- 简单文本协议理解与实现
- 基础测试通过能力
- README 说明能力

这道题面向新人，不要求复杂网络框架，不要求数据库，不要求 Web 服务。

重点是：

- 你能不能看懂一个简单协议
- 你能不能完成服务端与客户端的基础交互
- 你能不能让核心功能跑通

---

## 如果这是模板仓库，你应该怎么开始

### 第一步：使用模板创建你自己的仓库
在 GitHub 页面点击：

- `Use this template`
- 创建你自己的新仓库

### 第二步：克隆到本地

```bash
git clone <你的仓库地址>
cd <你的仓库名>
```

### 第三步：创建虚拟环境（建议使用）

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 第四步：安装依赖

```bash
pip install -r requirements.txt
```

### 第五步：阅读题目与协议说明

请优先阅读：

- [TASK.md](./TASK.md)
- `protocol.py`

### 第六步：开始完成代码

你主要会修改：

- `server.py`
- 可能还包括 `client_example.py`

---

## 提交要求

你需要提交：

1. 完整源码
2. `README.md`
3. 通过题目要求的核心测试

---

## 评分与验收说明

详细内容请查看：

- [评分细则（面向 agent）](./docs/scoring.md)
- [验收清单](./docs/checklist.md)
- [学生 README 模板](./docs/student-readme-template.md)

---

## 给候选人的说明

这道题不是比谁写得最复杂，而是看你是否具备基础的 Python 和网络编程能力。

请优先保证：

- 理解协议要求
- 服务端能正常启动
- 客户端和服务端能完成基础交互
- 核心测试能通过
- README 能说明你做了什么

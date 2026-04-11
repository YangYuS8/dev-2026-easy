# TCP 服务练习仓库（Beginner）

## 项目简介

这是一个面向初学者的 Python 练习仓库。你的任务是补全一个非常基础的 TCP 服务。

这个服务会接收客户端发来的文本命令，并返回结果。

## 你需要了解的内容

你不需要会数据库，也不需要会 Web 框架。

只需要知道：

- Python 基础语法
- 函数
- 字符串处理
- 如何运行 Python 文件
- 如何运行测试

## 文件说明

- `server.py`：TCP 服务主程序
- `protocol.py`：命令处理逻辑，主要需要修改这里
- `client_example.py`：一个简单客户端示例
- `tests/test_protocol.py`：基础测试
- `TASK.md`：任务要求
- `report.md`：提交时填写

## 推荐完成顺序

1. 先看 `TASK.md`
2. 再看 `protocol.py`
3. 运行测试
4. 补全代码
5. 再运行测试验证

## 如何运行测试

```bash
pytest
```

## 如何运行服务

```bash
python server.py
```

## 如何运行客户端示例

```bash
python client_example.py
```

## 当前支持的命令

- `PING`
- `ECHO hello`
- `UPPER hello world`
- `ADD 1 2`

其中有些命令目前还没有补全，这正是你要完成的内容。

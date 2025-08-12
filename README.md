# Python GIL 性能测试项目

测试 Python 全局解释器锁对多线程性能的影响。

## 使用方法

```bash
# 创建Python 3.14虚拟环境
uv venv --python 3.14

# 或创建Python 3.14无GIL版本虚拟环境（实验性）
uv venv --python 3.14.0rc1+freethreaded

# 运行测试
python main.py
```

## 测试内容

- 单线程 vs 多线程性能对比
- CPU 密集型任务测试
- 线程数：1, 2, 4, 8

## 测试结果

### Python 3.14 (有GIL)

```text
迭代次数: 100,000,000
1线程: 6.096s
2线程: 5.889s
4线程: 5.905s
8线程: 5.865s
```

### Python 3.14 无GIL版本

```text
迭代次数: 100,000,000
1线程: 6.988s
2线程: 3.577s
4线程: 2.033s
8线程: 2.122s
```

# 数据库迁移

本目录保存 Alembic 环境和由 Alembic 命令生成的版本文件。

- 创建差异迁移：`alembic revision --autogenerate -m "中文说明"`
- 应用迁移：`alembic upgrade head`
- 查看当前版本：`alembic current`

自动生成的迁移需要在提交前人工核对，特别是约束、数据类型和索引。

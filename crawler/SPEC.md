# Feminist Content Crawler - 项目规范

## 1. 项目概述

从合法的开放来源（UN Women、国际组织报告、开放获取学术内容）爬取女权主义相关文章，存储到 feminist_women 数据库中。

## 2. 数据来源

### 主要来源（已确认合法）
1. **UN Women** (unwomen.org) - 联合国妇女组织，完全开放的新闻和报告
2. **WHO Gender Health** - 世界卫生组织性别健康报告
3. **UNDP Gender** - 联合国开发计划署性别平等报告

### 扩展来源（后续添加）
- 开放获取学术平台
- CC 协议许可的博客

## 3. 爬虫结构

```
crawler/
├── scrapers/
│   ├── __init__.py
│   ├── un_women_scraper.py    # UN Women 爬虫
│   ├── who_scraper.py         # WHO 爬虫
│   └── base_scraper.py        # 基础爬虫类
├── config/
│   ├── __init__.py
│   └── settings.py            # 配置
├── models/
│   ├── __init__.py
│   └── article.py             # 文章数据模型
├── storage/
│   ├── __init__.py
│   ├── database.py             # 数据库存储
│   └── api_client.py           # API 客户端
├── main.py                     # 入口脚本
├── requirements.txt            # 依赖
└── README.md                   # 说明文档
```

## 4. 数据模型

```python
Article:
    - title: str          # 标题
    - content: str        # 正文内容
    - category: str       # 分类 (从来源或自动分类)
    - author: str          # 作者/来源机构
    - cover_image: str    # 封面图 URL
    - source_url: str      # 原文链接
    - source_name: str    # 来源名称 (UN Women, WHO, etc.)
```

## 5. 数据库更新

通过 REST API 更新到后端数据库：
- POST /api/articles - 创建文章
- 或直接操作 MySQL 数据库

## 6. 分类映射

来源文章自动映射到预定义分类：
- Politics → Politics
- Health → Health
- Education → Education
- Workplace → Workplace
- Culture → Culture
- Activism → Activism
- 默认 → Politics

## 7. 技术栈

- Python 3.x
- requests - HTTP 请求
- beautifulsoup4 - HTML 解析
- selenium (可选) - 动态页面
- pymysql / mysql-connector-python - 数据库连接

## 8. 运行方式

```bash
cd crawler
pip install -r requirements.txt
python main.py                    # 运行所有爬虫
python main.py --source un_women # 运行指定爬虫
python main.py --limit 10        # 限制文章数量
```

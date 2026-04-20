# Feminist Content Crawler

从合法开放来源爬取女权主义相关文章的工具。

## 数据来源

### 已确认合法来源
- **UN Women** (unwomen.org) - 联合国妇女组织，完全开放的新闻和报告
- **WHO Gender Health** - 世界卫生组织性别健康报告（开发中）
- **UNDP Gender** - 联合国开发计划署性别平等报告（开发中）

## 安装

```bash
cd crawler
pip install -r requirements.txt
```

## 配置

通过环境变量配置：

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD=your_password
export DB_NAME=feminist_women
export API_BASE_URL=http://localhost:8080
```

## 使用方法

```bash
# 爬取所有来源
python main.py

# 只爬取 UN Women
python main.py --source un_women

# 每个来源限制 10 篇文章
python main.py --limit 10

# 测试模式（不保存到数据库）
python main.py --dry-run

# 指定 API URL
python main.py --api-url http://your-server:8080
```

## 输出

成功爬取后，文章会通过 API 或直接写入数据库：

```
2024-01-01 12:00:00 - __main__ - INFO - Starting UN Women scraper...
2024-01-01 12:00:01 - __main__ - INFO - Scraped 15 articles
2024-01-01 12:00:02 - __main__ - INFO - Saved: UN Women article title...
...
2024-01-01 12:00:30 - __main__ - INFO - Results: 15 saved, 0 skipped (duplicates)
```

## 添加新的爬虫

1. 在 `scrapers/` 目录创建新文件，如 `example_scraper.py`
2. 继承 `BaseScraper` 类
3. 实现 `get_article_urls()` 和 `parse_article()` 方法
4. 在 `main.py` 的 `SCRAPERS` 字典中注册

## 法律说明

本项目只从明确开放的合法来源爬取内容：
- 国际组织官方出版物
- 明确标注可转载的 CC 协议内容
- 开放获取的学术论文

请遵守各网站的 robots.txt 和服务条款。

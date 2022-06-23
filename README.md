<div align="center">
<a href="https://github.com/Leon1s97/Uttu/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/Uttu/docs/logo/logo_16x9.png" alt="Logo" width="700" height="400">
</a>

# :sparkles: uttu :sparkles:

***Next generation distributed crawler framework***

</div>

---


<!-- Introduction -->
<div align="center">

# :purple_heart: 项目简介

</div>

Uttu 是集成了分布式爬虫框架、运维管理界面以及爬虫工具箱的智能爬虫生态圈。

旨在用简单的方式帮助用户构建面向不同业务场景的复杂爬虫应用。

- Write script in Python
- Powerful WebUI with script editor, task monitor, project manager and result viewer
- MongoDB, Redis, SQLite, Microsoft SQL Server, PostgreSQL 作为后端数据库
- RabbitMQ, Redis and Kafka 作为消息队列
- Task priority, retry, periodical, recrawl by age, etc...
- Distributed architecture, Crawl Javascript pages, Python3+ support, etc...

快速上手: https://github.com/Leon1s97/Uttu/

文档: https://github.com/Leon1s97/Uttu/

Release notes: https://github.com/Leon1s97/Uttu/releases

---

<div align="center">

# :blue_heart: 特性

</div>


| 产品名称      | 技术选型 | 特性 |
| :-----------: |  :-----------: | :-----------: |
| Uttu      | Python + Javascript + Vue | 
| 火车头   | C#        |






---

<div align="center">

# :heart: 快速上手 

</div>

### :star2: 安装Uttu

```bash
$ python -m pip install uttu
```

### :star2: 项目结构:

```
├─ docs
├─ tests
├─ uttu
│  ├─ commands
│  ├─ spiders
│  ├─ templetes
│  ├─ watcher
│  ├─ worker
│  ├─ __init__.py
│  ├─ exceptions.py
│  └─ requirements.txt
├─ LICENSE
├─ .gitignore
├─ MANIFEST.in
├─ README.md
├─ setup.py
```

### :star2: 使用Uttu

```bash
$ python3 -m venv <venv-path>
$ cd <venv-path>
$ uttu startproject --name <projectname> --path <projectpath> -- templ <templetes>
```

---

<div align="center">

# :green_heart: 贡献者们

<a href="https://github.com/Leon1s97/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/cdn/avatar.jpg" alt="Leon1s" width="80" height="80">
</a>

[![Leon1s97's GitHub stats](https://github-readme-stats.vercel.app/api?username=Leon1s97&show_icons=true&theme=vue)](https://github.com/anuraghazra/github-readme-stats)


Thanks for all your wonderful PRs, issues and ideas. 

</div>

---

<div align="center">

# :yellow_heart: 开源许可

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
</div>

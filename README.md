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

Uttu 是集成了**分布式爬虫框架**、**开发运维界面**以及**爬虫工具箱**的智能爬虫生态圈。

旨在用简单的方式帮助用户快速构建面向不同业务场景的爬虫应用。

- 基于CLI开发的项目模板渲染器，可快速构建爬虫项目
- 内置轻量级爬虫和分布式爬虫，可应对各种需求场景
- 模块化设计，大大提高兼容性和可复用性，减少重复开发
- 支持项目的一键注册，上线及更新，无缝对接开发运维界面
- 常用功能整合为爬虫工具箱，丰富的配套设施和插件支持

- 为MongoDB, Redis, SQLite, Microsoft SQL Server, PostgreSQL 等常用数据库提供支持
- RabbitMQ, Redis and Kafka 作为消息队列

快速上手: https://github.com/Leon1s97/Uttu/

文档: https://github.com/Leon1s97/Uttu/

Release notes: https://github.com/Leon1s97/Uttu/releases

---

<div align="center">

# :blue_heart: 功能特性

</div>



### :star2: 同类产品比对

| 产品名称      | 技术选型 | 功能比对 |
| :-----------: |  :-----------: | :-----------: |
| Uttu      | Python + Golang + VueJS | |
| 火车头   | C#        | |
| Scrapy   | Python        | |
| SpiderEngine V1  | python        | |






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

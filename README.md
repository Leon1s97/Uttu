<div align="center">
<a href="https://github.com/Leon1s97/Uttu/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/Uttu/docs/logo/logo_16x9.png" alt="Logo" width="700" height="400">
</a>



# ✨ uttu ✨

***Next generation distributed crawler framework***

</div>

---


<!-- Introduction -->
<div align="center">

# 💖 项目简介

</div>

Uttu 是集成了**分布式爬虫框架**、**开发运维界面**以及**爬虫工具箱**的智能爬虫生态圈。

旨在爬虫场景下为开发者提供开箱即用的一站式解决方案，用简单的方式帮助开发者快速构建面向不同业务场景的爬虫应用。


<a href="https://github.com/Leon1s97/Uttu/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/Uttu/docs/UTTU 智能爬虫生态圈.svg" alt="Logo" width="800" height="500">
</a>



快速上手: https://github.com/Leon1s97/Uttu/

文档: https://github.com/Leon1s97/Uttu/

Release notes: https://github.com/Leon1s97/Uttu/releases

---

<div align="center">

# 💙 功能特性

</div>


- 基于CLI开发的项目模板渲染器，可快速构建爬虫项目
- 内置轻量级爬虫和分布式爬虫，可应对各种需求场景
- 模块化设计，大大提高兼容性和可复用性，**提高开发效率**
- 支持项目的一键注册，上线及更新，无缝对接开发运维界面
- 常用功能整合为爬虫工具箱，丰富的配套设施和插件支持, **降低爬虫成本**
- 为MongoDB, Redis, SQLite, Microsoft SQL Server, PostgreSQL 等常用数据库提供支持
- RabbitMQ, Redis and Kafka 作为消息队列


### 🌟 同类产品比对

| 产品名称      | 技术选型 | 功能比对 |
| :-----------: |  :-----------: | :-----------: |
| Uttu      | Python + Golang + VueJS | 自研分布式爬虫框架，在不提高使用门槛的前提下，可应对复杂网站的开发，并集成了运维管理，工具箱等功能。 |
| 火车头   | C#        | 商用软件，上手简单，能应对简单网站的抓取。可维护性和可拓展性很差，且无法开发复杂网站。 |
| Scrapy   | Python        | 功能强大的开源异步抓取框架，业务场景主要是全站抓取，本身框架过重且不支持分布式，无法适应海量信源的抓取， 且程序管理上有较大的难度。 |
| SpiderEngine V1  | Python        | 自研分布式爬虫框架，学习成本低， 能应对绝大多数网站的抓取，但是仍有部分复杂网址无法兼容。 |



---

<div align="center">

#  💜 快速上手 

</div>

### 🌟 安装Uttu

```bash
$ python -m pip install uttu
```

### 🌟 项目结构:

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

### 🌟 使用Uttu

```bash
$ python3 -m venv <venv-path>
$ cd <venv-path>
$ uttu startproject --name <projectname> --path <projectpath> -- templ <templetes>
```

---

<div align="center">

# 💚 贡献者们

<a href="https://github.com/Leon1s97/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/cdn/avatar.jpg" alt="Leon1s" width="80" height="80">
</a>

<!-- [![Leon1s97's GitHub stats](https://github-readme-stats.vercel.app/api?username=Leon1s97&show_icons=true&theme=vue)](https://github.com/anuraghazra/github-readme-stats) -->


Thanks for all your wonderful PRs, issues and ideas. 

</div>

---

<div align="center">

# 💛 开源许可

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
</div>

<div align="center">
<a href="https://github.com/Leon1s97/Uttu/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/Uttu/docs/logo/logo_16x9.png" alt="Logo" width="700" height="400">
</a>



# â¨ uttu â¨

***Next generation distributed crawler framework***

</div>

---


<!-- Introduction -->
<div align="center">

# ð é¡¹ç®ç®ä»

</div>

Uttu æ¯éæäº**åå¸å¼ç¬è«æ¡æ¶**ã**å¼åè¿ç»´çé¢**ä»¥å**ç¬è«å·¥å·ç®±**çæºè½ç¬è«çæåã

æ¨å¨ç¬è«åºæ¯ä¸ä¸ºå¼åèæä¾å¼ç®±å³ç¨çä¸ç«å¼è§£å³æ¹æ¡ï¼ç¨ç®åçæ¹å¼å¸®å©å¼åèå¿«éæå»ºé¢åä¸åä¸å¡åºæ¯çç¬è«åºç¨ã


<a href="https://github.com/Leon1s97/Uttu/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/Uttu/docs/UTTU æºè½ç¬è«çæå.svg" alt="Logo" width="800" height="500">
</a>



å¿«éä¸æ: https://github.com/Leon1s97/Uttu/

ææ¡£: https://github.com/Leon1s97/Uttu/

Release notes: https://github.com/Leon1s97/Uttu/releases

---

<div align="center">

# ð åè½ç¹æ§

</div>


- åºäºCLIå¼åçé¡¹ç®æ¨¡æ¿æ¸²æå¨ï¼å¯å¿«éæå»ºç¬è«é¡¹ç®
- åç½®è½»éçº§ç¬è«ååå¸å¼ç¬è«ï¼å¯åºå¯¹åç§éæ±åºæ¯
- æ¨¡ååè®¾è®¡ï¼å¤§å¤§æé«å¼å®¹æ§åå¯å¤ç¨æ§ï¼**æé«å¼åæç**
- æ¯æé¡¹ç®çä¸é®æ³¨åï¼ä¸çº¿åæ´æ°ï¼æ ç¼å¯¹æ¥å¼åè¿ç»´çé¢
- å¸¸ç¨åè½æ´åä¸ºç¬è«å·¥å·ç®±ï¼ä¸°å¯çéå¥è®¾æ½åæä»¶æ¯æ, **éä½ç¬è«ææ¬**
- ä¸ºMongoDB, Redis, SQLite, Microsoft SQL Server, PostgreSQL ç­å¸¸ç¨æ°æ®åºæä¾æ¯æ
- RabbitMQ, Redis and Kafka ä½ä¸ºæ¶æ¯éå


### ð åç±»äº§åæ¯å¯¹

| äº§ååç§°      | ææ¯éå | åè½æ¯å¯¹ |
| :-----------: |  :-----------: | :-----------: |
| Uttu      | Python + Golang + VueJS | èªç åå¸å¼ç¬è«æ¡æ¶ï¼å¨ä¸æé«ä½¿ç¨é¨æ§çåæä¸ï¼å¯åºå¯¹å¤æç½ç«çå¼åï¼å¹¶éæäºè¿ç»´ç®¡çï¼å·¥å·ç®±ç­åè½ã |
| ç«è½¦å¤´   | C#        | åç¨è½¯ä»¶ï¼ä¸æç®åï¼è½åºå¯¹ç®åç½ç«çæåãå¯ç»´æ¤æ§åå¯æå±æ§å¾å·®ï¼ä¸æ æ³å¼åå¤æç½ç«ã |
| Scrapy   | Python        | åè½å¼ºå¤§çå¼æºå¼æ­¥æåæ¡æ¶ï¼ä¸å¡åºæ¯ä¸»è¦æ¯å¨ç«æåï¼æ¬èº«æ¡æ¶è¿éä¸ä¸æ¯æåå¸å¼ï¼æ æ³éåºæµ·éä¿¡æºçæåï¼ ä¸ç¨åºç®¡çä¸æè¾å¤§çé¾åº¦ã |
| SpiderEngine V1  | Python        | èªç åå¸å¼ç¬è«æ¡æ¶ï¼å­¦ä¹ ææ¬ä½ï¼ è½åºå¯¹ç»å¤§å¤æ°ç½ç«çæåï¼ä½æ¯ä»æé¨åå¤æç½åæ æ³å¼å®¹ã |



---

<div align="center">

#  ð å¿«éä¸æ 

</div>

### ð å®è£Uttu

```bash
$ python -m pip install uttu
```

### ð é¡¹ç®ç»æ:

```
ââ docs
ââ tests
ââ uttu
â  ââ commands
â  ââ spiders
â  ââ templetes
â  ââ watcher
â  ââ worker
â  ââ __init__.py
â  ââ exceptions.py
â  ââ requirements.txt
ââ LICENSE
ââ .gitignore
ââ MANIFEST.in
ââ README.md
ââ setup.py
```

### ð ä½¿ç¨Uttu

```bash
$ python3 -m venv <venv-path>
$ cd <venv-path>
$ uttu startproject --name <projectname> --path <projectpath> -- templ <templetes>
```

---

<div align="center">

# ð è´¡ç®èä»¬

<a href="https://github.com/Leon1s97/">
<img src="https://cdn.jsdelivr.net/gh/Leon1s97/cdn/avatar.jpg" alt="Leon1s" width="80" height="80">
</a>

<!-- [![Leon1s97's GitHub stats](https://github-readme-stats.vercel.app/api?username=Leon1s97&show_icons=true&theme=vue)](https://github.com/anuraghazra/github-readme-stats) -->


Thanks for all your wonderful PRs, issues and ideas. 

</div>

---

<div align="center">

# ð å¼æºè®¸å¯

This project is licensed under the terms of the [MIT](https://opensource.org/licenses/MIT) license.
</div>

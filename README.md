# janog41-auto-taiji
明日からはじめるネットワーク運用自動化

## Play With Docker へのデプロイ

Play With Docker は、無料で、ブラウザのみで、docker swarmモードを試せる環境です。利用には Docker ID が必要になります。 Docker ID は https://www.docker.com/ から、無料で作成することができます。

Docker ID が用意できたら、下のボタンをCTRL押しながらポチってください。

<a href="http://play-with-docker.com?stack=https://raw.githubusercontent.com/mnagaku/janog41-auto-taiji/master/docker-compose.yml"><img src="https://raw.githubusercontent.com/play-with-docker/stacks/master/assets/images/button.png" /></a>

Docker ID でログインすると、デプロイが始まります。

デプロイが終わったら、デプロイの進捗を表示していた小窓を close してください。ダッシュボードに「8.8.8.8」というリンクができているので、これをポチって Jupyter にアクセスします。

Jupyter には「janog41-auto-taiji」フォルダができているので、それを開いてください。以降の操作は、そこに続きがあります。

あと、 Play With Docker 、EC2のスポットインスタンスなのか、1度、突然死することがありました。突然死があり得るので、そこは、そーゆーもんだと思って使うのが良いようです。

あと、Jupyter 上での rename が error になる、既知の不具合があるので、 必要なら Terminal から mv とかしてください。すいません、そのうち直します。てか、 PWD 上でしか発生しない予感。

## ローカルの Docker へのデプロイ

Windows もしくは Mac 上の Docker 環境であれば、 docker-compose コマンドが使えるので、

```
# docker-compose up -d
```

で、デプロイが始まります。

デプロイが終わったら、ブラウザで「localhost:8888」アクセスすると、 Jupyter に繋がります。

Jupyter には「janog41-auto-taiji」フォルダができているので、それを開いてください。以降の操作は、そこに続きがあります。

## 続き

[始動編](https://www.janog.gr.jp/meeting/janog41/application/files/8115/1496/7531/janog41-autoprep-taiji-01.pdf)にあるコード実行部分をNotebook化したのが、[こちら](janog41-autoprep-taiji-01.ipynb)になります。スライドと対応を見比べながら、コードを実行していくことができます。

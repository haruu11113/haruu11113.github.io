---
title: "How to Install Python"
date: 2022-04-19T00:00:00+09:00
description: how to install Python
hero: images/forest.jpg
---

## このページわかる事
mac（ubuntuでも可）でPython（主にPython3系）環境を構築する事ができます．

pyenvとは，OS上のPythonのバージョンの管理ができるツールです．Pythonの開発環境を作成する際にはpyenvなどのバージョン管理ツールを用いることが主流です（主流は言い過ぎかもですが，バージョン管理ツールを使っておらずあとで面倒になることがます．

pyenvとは，OS上のPythonのバージョンの管理ができるツールです．この記事ではpyenvを用い，Pythonバージョンを自由に切り替えられるよう，Python環境を構築します．つまり，ターミナル（端末）上で```Python```と打った際のPythonのバージョンを好きに切り替えられるように環境を構築します．

## OS
I tryed those OS.
- mac（10.0.1）
- ubuntu（18.04.5 and 20.04）

## Start

## 1. Install pyenv


まず，[ターミナル(端末)を開き以下のコマンドを入力](https://github.com/pyenv/pyenv#basic-github-checkout)+Enter

```
 git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

その後以下のコマンドを入力(bashの場合)．
(bash以外のshellを使っている場合は，公式github([pyenv](https://github.com/pyenv/pyenv))のreadmeい書いてあります．)

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

## 2. Pythonのインストール
以下のコマンドをターミナル(端末)に入力+Enter．好きなバージョンを選んでください．
```pyenv install --list```でインストール可能なバージョン一覧を見ることができます．

```
pyenv install バージョン
ex) pyenv install 3.6.0
```

## 3. インストールしたPythonを利用するように設定以下のコマンドをターミナル(端末)に入力+Enter．

```
pyenv global バージョン
ex) pyenv global 3.6.0
```

## その他のpyenvコマンド

### - ```pyenv versions```
インストール済のPythonのバージョン一覧を調べる．ここに表示されるバージョンはすでに```pyenv install バージョン``` 済であり，```pyenv global バージョン```する事が出来る．


### - ```pyenv update```
pyenv時代のバージョンアップ方法->公式github([pyenv-update](https://github.com/pyenv/pyenv-update))．するべきかはわからん．
1.インストール

```
git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
```

2.アップデート

```
pyenv update
```
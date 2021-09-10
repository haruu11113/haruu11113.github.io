---
title: Code
weight: 11
menu:
  notes:
    name: Code
    identifier: notes-tips-code
    parent: notes-tips
    weight: 111
---

{{< note title="Python name">}}
|name|mean|
|:--:|:--:|
|\_ | 使わない変数|
|\_\* |外部からアクセスされたくない変数・関数(アクセスは可能)|
|\_\_\*|プライベート変数・関数|
||
{{< /note >}}

{{< note title="fzf config">}}
- https://www.trhrkmk.com/posts/fzf-command-line-productivity-tools/
{{< /note >}}

{{< note title="python string to list">}}
string = "[1, 2, 3]"
eval(straing)
> [1, 2, 3]
{{< /note >}}

{{< note title="grepでファイル検索して、ディレクトリ移動をさせる">}}
```
grep -rl "検索ワード" [検索するディレクトリ] | xargs -I '{}' mv {} [移動先のディレクトリパス]
```
{{< /note >}}

{{< note title="git command">}}
- git addの取り消し(stagingの取り消し)

```
$ git reset HEAD <file name>
```

- commitだけ取り消して，staging状態に戻す

```
$ git reset --soft HEAD~
```

http://bcl.sci.yamaguchi-u.ac.jp/~jun/notebook/git/cancel/
{{< /note >}}

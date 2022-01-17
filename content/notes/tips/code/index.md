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


# GPUの有無を確認
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

# docker imageの一括削除
https://qiita.com/boiyama/items/9972601ffc240553e1f3

{{< /note >}}

{{< note title="fzf config">}}
- https://www.trhrkmk.com/posts/fzf-command-line-productivity-tools/
{{< /note >}}

{{< note title="fzf config">}}
- https://www.trhrkmk.com/posts/fzf-command-line-productivity-tools/
{{< /note >}}

{{< note title="move files using grep">}}
```
grep -rl "key word" ./ | xargs -I '{}' mv {} [dir path]
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

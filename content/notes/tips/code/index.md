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

{{< note title="fzf config">}}
- https://www.trhrkmk.com/posts/fzf-command-line-productivity-tools/
{{< /note >}}

{{< note title="move files using grep">}}
```
grep -rl "key word" ./ | xargs -I '{}' mv {} [dir path]
```
{{< /note >}}

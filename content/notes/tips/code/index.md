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


{{< note title="GPU">}}
### GPUの有無を確認
```
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
```

### 利用可能なGPUの有無を判定
```
import tensorflow as tf
tf.test.is_gpu_available()
```

- [tensorflowとcudaなどのバージョン対応](https://www.tensorflow.org/install/source?hl=ja#tested_build_configurations)
- [これでかいけつした](https://zenn.dev/ylabo0717/articles/48796b7f3470c7#2-6.-gpu認識確認)
- [これ見るとlibcudnn8の諸々わかった](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)
- [マルチGPUなどについて](https://www.tensorflow.org/guide/gpu?hl=ja)
- [dockerでのgpu](https://docs.docker.jp/compose/gpu-support.html)

```
apt-get install libcudnn8=8.9.1.23-1+cuda11.8
```

### gpuで計算系
- [cupy numpyの代替](https://docs.cupy.dev/en/stable/install.html#installing-cupy)
- [pandas numpyの代替](https://docs.rapids.ai/install#docker)
- [tsne-cuda](https://github.com/CannyLab/tsne-cuda/wiki/Installation)


{{< /note >}}


{{< note title="Docker">}}
### docker imageの一括削除
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

```
$ git config --global fetch.prune true
```

http://bcl.sci.yamaguchi-u.ac.jp/~jun/notebook/git/cancel/

- remoteリポジトリにないブランチを削除
```
git fetch -p && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

- [Gitでやらかした時に使える19個の奥義](https://qiita.com/muran001/items/dea2bbbaea1260098051)

{{< /note >}}

{{< note title="python">}}
```
# sklearn random forest
# 推定の確率を出す．claasses_の順番で確率が出る
model.classes_
model.predict_proba()
```
{{< /note >}}

{{< note title="mint60">}}
```
./keyboards/mint60/keymaps/custom
make mint60:custom
make mint60:custom:avrdude
```
{{< /note >}}
{{< note title="gif generation">}}
```
ffmpeg -i 画面収録_299U-08-09_1.93.N.mov -r 24 gamen_test1.gif
```
{{< /note >}}

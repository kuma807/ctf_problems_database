# バイナリファイル

## photopea

ぶっ壊れた画像開けたりする
https://www.photopea.com/
使った問題: https://picoctf2021.haydenhousen.com/forensics/tunn3l-v1s10n

## exiftool

ファイルの情報を取得できる

```
exiftool file
```

## CyberChef

16 進数の bit 演算とかができる。
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'62275c786663615c783165725c786237225c7863315c7831375c7861305c7838'%7D,'Standard',false)&input=NTE0NjZkNGU1ZjU3NTUzODE5NTU1MTQxNmU0ZjUzMDA0MTNmMWI1MDA4Njg0ZDU1MDQzODQxNTcwNDZlNDk1OQ

## シーザー暗号解読

http://www.net.c.dendai.ac.jp/crypto/caesar2.html?#

# 画像

## binwalk

中身に埋め込まれてるファイルがあるかなどを取り出すことが出来る。

```
binwalk -e file
```

## strings

ファイル内の表示可能な文字列を見つけてくれる。

```
strings file
```

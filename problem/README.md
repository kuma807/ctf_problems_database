# 問題一覧

[crackme-py](#crackme-py)  
[Magikarp Ground Mission](#magikarp-ground-mission)  
[tunn3l v1s10n](#tunn3l-v1s10n)  
[Easy Peasy](#easy-peasy)  
[Cookies](#cookies)  
[Insp3ct0r](#insp3ct0r)  
[Scavenger Hunt](#scavenger-hunt)
[Glory of the Garden](#glory-of-the-garden)

# crackme-py

## 解き方

crackme.py を読んで内容を理解する。flag を出力する関数が呼び出されていないためそれを呼び出すようにコードを変える。

## 学び

特になし

# Magikarp Ground Mission

## 解き方

cd,ls,cat などの linux コマンドを使ってマシン内にある flag を探す。

## 学び

特になし

# tunn3l v1s10n

## 解き方

1.まず与えられらバイナリファイルが何のファイルなのかを特定するために exiftool を使うとファイルの形式が BMP であることがわかる。あとはファイルの先頭(マジックナンバー)から BMP であることも特定できる。

2.Hex エディタでデータを見て、BMP の形式で間違っているところを探すとオフセットと情報ヘッダサイズが間違っているので修正する。

3.すると画像が表示されるが必要な情報が載ってない。やけに横に長い画像のため画像の height を Hex エディタで編集すると flag が見つかる。

## 学び

- file コマンドでバイナリファイルがどんなファイルだかわかるらしい（今回はデータが壊れてたのでダメだった）
- exiftool で色々ファイルの情報が見れる
- ファイル復元するときはファイルタイプのデータ形式を wiki で調べて壊れてないか確認するの典型ぽいかも？
- 画像の height,weidth を変えて追加情報探すのも典型かも？
- photopea ていうサイト使うと壊れた写真そのまま開けたらしい
- マジックナンバーの存在を知った

# Easy Peasy

## 解き方

1.コードを読むと暗号化の key の長さが 50000 しかなくて、すべて使い切るとまた最初から使い回す方式になっている。そのため 50000 文字を使い切って適当な文字列を再度送ることで flag を暗号化した key を特定できる、この key を使って暗号化された flag を解読すれば良い。

2.とりあえず 50000 文字使い切って"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"をサーバーに送る。サーバーから帰ってきた暗号を元にローカルで key を復元。復元した key を使って flag を復号した。

## 学び

- key を使い回すのは危ない
- python で 16 進数の文字列扱うのむずい
- 今回は 50000 文字使い切るために手作業で文字を送ったけど python を使って次のように送れる。また python だと"aaaaaaaaaaaaa"じゃなくて\x00 を送れるため key を復号する必要がなくなる。

```bash
python3 -c "print('\x00'*(50000-32)+'\n'+'\x00'*32)" | nc mercury.picoctf.net 36981
```

# Cookies

## 解き方

問題の名前からして cookie が怪しいので見に行くと name っていうものが保存されている。この name の value がデフォルトだと-1 になってるのでそれを適当に 1 に変更するとサイトに表示される内容が変わる。value を 1 から 18 まで試すと 18 で flag が出てくる。

## 学び

- cookie は変えられるため cookie だけをみてユーザー承認などをすると良くない

# Insp3ct0r

## 解き方

サイトを開いて管理者ツールを開くだけ html,css,js に flag が隠されている

## 学び

特になし

# Scavenger Hunt

## 解き方

サイトを開いて管理者ツールを開くと html,css,js に flag と次のフラグのヒントが隠されている。
`How can I keep Google from indexing my website?`  
このヒントから/robots.txt にアクセスすると flag と次のヒントが見つかる。
`I think this is an apache server... can you Access the next flag?`
apache サーバーなので/.htaccess,/.htpasswd,/server-status にアクセスすると/.htaccess に flag とヒントがある。
`I love making websites on my Mac, I can Store a lot of information there.`
mac なので/.DS_Store にアクセスすると最後の flag が見つかる

## 学び

- robots.txt は外部からアクセスすることが想定されていてクローラーとかが index 化して良いページの指定などをしている。
- /.htaccess は url リダイレクト、アクセス制限、キャッシュ制御などさまざまな設定を行うファイル。重要な設定に関わるファイルでセキュリティ的に外部から見れてはいけない。/.htaccess ないで外部から見れないように設定ができる。
- /.DS_Store は macOS の Finder によって作成される隠しファイルで、フォルダ内のファイルの表示方法(アイコンの位置、選択されたビューの種類、ウィンドウのサイズ、背景色や背景画像など）を記録します。/.DS_Store は macos 以外では不要なファイルで web サーバーなどにアップロードしてしまうと デレクトリ構造などがバレてしまう。git で/.DS_Store は含まないように気をつけよう。

# Glory of the Garden

## 解き方

exiftool で追加情報を見る。特に何もなし
binwalk でなかにファイルないか確認。何もなし
strings でファイル内に文字ないか確認 -> Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"

## 学び

特になし

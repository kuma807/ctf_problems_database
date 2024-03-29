# 概要

このレポジトリは ctf で解いた問題を簡単に管理するためのレポジトリです。このレポジトリを使うことで解いた合計問題数、カテゴリごとの問題数など様々なデータを [このサイト](https://kuma807.github.io/ctf_problems/) から見ることができます。

# レポジトリ構成

/data ・・・ picoCTF の問題に関するデータや今まで解いてきた問題のデータを保持  
/tools ・・・ 解いた問題の記録のためのツールなどが入っている  
/writeups ・・・ 解いた問題の witeup を保存するためのデレクトリ

# 準備

まず右上のボタンからこのブランチを fork してください。fork をすることでこのレポジトリのコピーがあなたの github アカウント下に作成されます。この作成されたコピーのレポジトリをローカルに clone してください。

# 問題の記録方法

ローカルに clone したリポジトリでコマンドを打つことで解いた問題を記録することができます。問題を解いた時はリポジトリのルートデレクトリで以下のコマンドを実行してください。

```bash
./solved
```

コマンド実行後に問題名、サイト名、コンテスト名、カテゴリーが順番に聞かれるため入力してください。

> [!TIP]  
> picoCTF の問題を解いた場合はサイト名を聞かれた時に何も入力せずに enter を押すことで、自動的にコンテスト名などの情報が記録されます

このコマンドを実行することで解いた問題が記録されるとともに /writeups/README.md に writeup の雛形が作成されます。writeup は書いても書かなくてもサイトで表示されるデータに違いは産まれません。  
また新しく解いた問題を記録したあとサイトに反映するためには github に変更を push する必要があります。

# データの見方

まずこのレポジトリを fork した時に作成されたコピーのレポジトリを開き、data/solved.json ファイルを開いてください。ファイルを開いたあと右上にある raw ボタンをクリックすると json 形式のページが表示されるので、この json 形式のページの url をコピーしてください。  
https://kuma807.github.io/ctf_problems/ にアクセスするとサイトが表示されます。サイトの上にあるテキストボックスに先ほどコピーした url を貼り付けて更新ボタンを押してください。
更新を押すデータが表示されます。また入力した url は保存されるため次回以降入力する必要はなくなります。

## 今まで解いてきた picoCTF の問題の反映方法

すでに解いた picoCTF の問題については手動で一問ずつ記録する必要はなく、一括で全ての問題を記録することができます。追加するためには **まず picoCTF にログインしてください** 。ログイン後以下の 4 つの url にアクセスして、取得した json をそれぞれのファイルに保存してください。

| url                                                          | 保存するファイル     |
| ------------------------------------------------------------ | -------------------- |
| http://play.picoctf.org/api/challenges/?page=1&page_size=100 | data/pico_data1.json |
| http://play.picoctf.org/api/challenges/?page=2&page_size=100 | data/pico_data2.json |
| http://play.picoctf.org/api/challenges/?page=3&page_size=100 | data/pico_data3.json |
| http://play.picoctf.org/api/challenges/?page=4&page_size=100 | data/pico_data4.json |

ファイルを保存後リポジトリのルートデレクトリで以下のコマンドを実行することで解いた picoCTF の問題が全て記録されます。

```bash
python3 tools/pico_init.py
```

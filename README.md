# 197カ国 暗記帳

国旗・国名・場所をセットで覚えるための、地球儀つきクイズとテストのアプリです。
スマホのホーム画面に追加すると、アプリのように起動できます（オフラインでも動きます）。

**アプリ：** https://marina-0731.github.io/atlas197/

## できること

- **図鑑で見る**：地域ごとの一覧から国を選ぶと、地球儀がその国へ回り、国旗・首都・場所の覚え方を表示
- **クイズ（4択）**：国旗 → 国名／場所 → 国名／国名 → 国旗
- **テスト**：地図に番号を振った国の国名を書き、国旗を①〜⑮から選んで採点
- **テスト範囲**：地域と番号（例：アジア 1〜15）で出題範囲をしぼれる
- 3回連続で正解した国を「覚えた」として記録（記録は各端末のブラウザに保存）

国の一覧・並び順・国名は「世界の国旗」の
[国旗一覧（大陸ごと）](https://www.world-national-flags.com/document/flagslist.html)
（197カ国：国連加盟193カ国＋バチカン・コソボ・クック諸島・ニウエ）に合わせています。

## ホーム画面への追加

- **iPhone / iPad（Safari）**：共有ボタン →「ホーム画面に追加」
- **Android（Chrome）**：メニュー →「ホーム画面に追加」または「アプリをインストール」

## ファイル構成

| パス | 内容 |
|---|---|
| `src/app.html` | アプリ本体（画面・クイズ・テストのコード） |
| `data/countries.json` | 197カ国のデータ（国名・首都・地域・番号・国旗絵文字・位置） |
| `world.json` | 世界地図（Natural Earth 1:50m、world-atlas より） |
| `index.html` | 公開用ページ（`tools/build.py` で生成） |
| `manifest.webmanifest`, `sw.js`, `icons/` | ホーム画面アプリ（PWA）用 |
| `tools/build.py` | `index.html` を組み立て、`sw.js` のキャッシュ版を更新 |
| `tools/make_icons.py` | アイコン画像を作成 |

## 更新のしかた

```bash
python3 tools/build.py
git add -A && git commit -m "変更内容" && git push
```

`build.py` を実行するとキャッシュの版が上がり、ホーム画面のアプリも次に開いたときに新しい版に切り替わります。

## 出典

- 地図：[world-atlas](https://github.com/topojson/world-atlas)（Natural Earth, public domain）
- 国コード・位置：[world-countries](https://github.com/mledoze/countries)（ODbL）
- ライブラリ：d3.js, topojson-client

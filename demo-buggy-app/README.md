# demo-buggy-app

学習用の「わざと不具合を含む」Python CLIサンプルです。
後でバグ修正デモを行う前提で作成しています。

## 想定シーン

- ユーザーごとのタスク一覧表示
- 完了率の計算

## 実行方法

```bash
cd demo-buggy-app
python3 main.py
```

## 注意

このサンプルには意図的な不具合が含まれます。
- 実行時エラー（NameError / KeyError）
- ロジック不具合（引数の型不一致）

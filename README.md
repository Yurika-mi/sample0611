# sample0611

このリポジトリは、日常業務で活用できるサンプルメモ集と、デバッグ学習用の Python サンプルアプリを収録した学習・実践向けリポジトリです。

---

## 📁 リポジトリ構成

```
sample0611/
├── README.md                      # このファイル
├── sample-memos/                  # 業務で使えるメモテンプレート集
│   ├── 01_daily_work_memo.md      # 日次作業メモ
│   ├── 02_meeting_minutes.md      # 打ち合わせメモ
│   ├── 03_bug_investigation_memo.md  # 不具合調査メモ
│   ├── 04_release_checklist_memo.md  # リリース前チェックリスト
│   ├── 05_idea_stock_memo.md      # 改善アイデアメモ
│   ├── 06_client_communication_memo.md  # 顧客連絡メモ
│   ├── 07_handover_memo.md        # 引き継ぎメモ
│   ├── 08_incident_report_memo.md # 障害報告メモ
│   ├── 09_onboarding_memo.md      # 新メンバー向けオンボーディングメモ
│   └── 10_retrospective_memo.md   # 振り返りメモ
└── demo-buggy-app/                # デバッグ学習用 Python サンプルアプリ
    ├── README.md
    ├── main.py
    └── service.py
```

---

## 📝 sample-memos — 業務メモテンプレート集

日常業務でそのまま使えるメモのサンプルテンプレートです。  
各ファイルを参考に、自分のプロジェクトへ応用してください。

| ファイル | 用途 |
|---|---|
| `01_daily_work_memo.md` | 日次作業の記録・振り返り |
| `02_meeting_minutes.md` | 打ち合わせの議題・決定事項・ToDoの管理 |
| `03_bug_investigation_memo.md` | 不具合の再現条件・仮説・対応方針の整理 |
| `04_release_checklist_memo.md` | リリース前の機能・品質・運用確認 |
| `05_idea_stock_memo.md` | 改善アイデアのストックと効果・優先度の検討 |
| `06_client_communication_memo.md` | 顧客との連絡内容・回答方針の記録 |
| `07_handover_memo.md` | 作業の引き継ぎ情報と残タスクの整理 |
| `08_incident_report_memo.md` | 障害発生時の事象・対応・再発防止策の記録 |
| `09_onboarding_memo.md` | 新メンバーの初日ゴール・参照資料・詰まりポイント |
| `10_retrospective_memo.md` | スプリント振り返り（KPT形式） |

---

## 🐛 demo-buggy-app — デバッグ学習用サンプルアプリ

ユーザーごとのタスク管理を模した Python CLI アプリです。  
**意図的な不具合**を含んでおり、デバッグ練習や Copilot を使ったバグ修正デモに活用できます。

### 含まれる不具合

- `NameError` — 未定義変数の参照
- `KeyError` — 存在しないキーへのアクセス
- 型不一致による引数エラー

### 実行方法

```bash
cd demo-buggy-app
python3 main.py
```

詳細は [`demo-buggy-app/README.md`](./demo-buggy-app/README.md) を参照してください。

---

## 🚀 使い方

1. このリポジトリをクローンします。
   ```bash
   git clone https://github.com/Yurika-mi/sample0611.git
   ```
2. `sample-memos/` のテンプレートを自分のプロジェクトにコピーして活用してください。
3. `demo-buggy-app/` でデバッグ練習やデモを行ってください。
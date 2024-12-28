# wandb_tutorial
このリポジトリは、Weights & Biases (wandb)を使用したLLM学習実験の追跡とモニタリングのチュートリアルを練習がてら作成します。


# ファイルの説明
```
wandb_tutorial/
├── .env_sample # 環境変数のサンプルファイル
├── config.py # 設定ファイル
├── data/ # データディレクトリ
│ ├── gpt-4.jsonl # GPT-4の応答データ
│ └── question_full.jsonl # 質問データ
├── prompt/ # プロンプトディレクトリ
│ └── judge_ja_prompts.jsonl # 日本語評価用プロンプト
└── 00_wandb_tutorial.ipynb # LoRA学習のチュートリアル
```

## セットアップ

1. 必要な環境変数を設定
   - `.env_sample`を`.env`にコピーし、必要なAPIキーを設定します
   - 必要なAPIキー:
     - OPENAI_API_KEY
     - WANDB_API_KEY
     - HUGGINGFACEHUB_API_TOKEN

2. 必要なパッケージのインストール
   ```bash
   pip install wandb python-dotenv transformers==4.38.2 peft==0.10.0 trl==0.7.10 torch==2.4.1+cu124
   ```
学習に影響があるパッケージバージョンは合わせて、追加で必要なパッケージは別途インストールしてください。



## データセット

- `gpt-4.jsonl`: GPT-4モデルの応答データを含むJSONLファイル
- `question_full.jsonl`: 様々なカテゴリ（coding, extraction, humanities, math, reasoning, roleplay, stem, writing）の質問データを含むJSONLファイル

## プロンプト

- `judge_ja_prompts.jsonl`: 日本語の回答を評価するためのプロンプトテンプレートを含むファイル
  - single-v1: 一般的な質問評価用
  - single-math-v1: 数学関連の質問評価用

## 使用方法

1. 環境変数の設定
2. Jupyter Notebookを起動
3. `00_wandb_tutorial.ipynb`を開いてチュートリアルを実行
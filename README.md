# example.llama-index

## summery

notion 上にある技術文書を前提とした PR レビューを行います

## for user

### Envioronment Variables

### save コマンド

```shell
pip install poetry
make install
poetry run python ./src/main.py save ${NOTION_DATABASE_ID} ${NOTION_QUERY_JSON}
```

- NOTION_QUERY_JSON
  指定した Notion Database から ドキュメントを取得するための条件です。 json 文字列で記述してください。

```json
// example value
{
  "filter": {
    "or": [
      {"property": "status", "select": {"equals": "approved"}},
      {"property": "status", "select": {"equals": "posted"}},
    ]
  }
}
```

### review コマンド

```shell
pip install poetry
make install
poetry run python ./src/main.py review ${QUERY}
```

- ex
- QUERY
  review 時の質問内容を記述してください。

## for developer

### 前提条件

docker を install しておくこと

### setup

vscode の dev container で開く

```shell
make install
```

拡張機能はおススメを入れておく

### コマンド

Makefile を参照

- ライブラリを追加する
  `poetry add termcolor`
  `poetry add -D flake8`

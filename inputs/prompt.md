## `gh pr diff ${{ github.event.number }}` コマンドで取得した PR の差分情報

```txt
diff --git a/.github/actions/review/action.yml b/.github/actions/review/action.yml
index 9773160..1a76311 100644
--- a/.github/actions/review/action.yml
           AZURE_OPEN_AI_EMBEDDING_MODEL_DEPLOY_NAME: ${{ inputs.AZURE_OPEN_AI_EMBEDDING_MODEL_DEPLOY_NAME }}
-          GOOGLE_APPLICATION_CREDENTIALS_JSON: ${{ inputs.GOOGLE_APPLICATION_CREDENTIALS_JSON }}
+          GOOGLE_APPLICATION_CREDENTIALS_JSON: '${{ inputs.GOOGLE_APPLICATION_CREDENTIALS_JSON }}'
           GOOGLE_INDEX_BUCKET_NAME: ${{ inputs.GOOGLE_INDEX_BUCKET_NAME }}
           GOOGLE_INDEX_FILE_NAME: ${{ inputs.GOOGLE_INDEX_FILE_NAME }}
           
       - name: Create comment
         shell: bash
         run: |
-          gh pr comment ${{ github.event.number }} -F ./review.md
+          cat review.md
+          gh pr comment ${{ github.event.number }} -F review.md
         env:
           GH_TOKEN: ${{ inputs.GITHUB_TOKEN }}
diff --git a/src/llama_index_wrapper/api.py b/src/llama_index_wrapper/api.py
index bdacf33..5550c4e 100644
--- a/src/llama_index_wrapper/api.py
+++ b/src/llama_index_wrapper/api.py
@@ -67,7 +67,7 @@ def save_notion_pages(self, documents: List[Document]) -> None:
         index.storage_context.persist(persist_dir=self.env.storage_context_tmp_dir)
 
     def ask(self, query: str) -> None:
-        print(query, file=sys.stderr)
+        print("query: \n" + query, file=sys.stderr)
         service_context = self.get_service_context()
         storage_context = StorageContext.from_defaults(
             docstore=SimpleDocumentStore.from_persist_dir(
```

## 回答してほしい内容

この PR の差分情報に対してコードの改善点を指摘するためのレビューを日本語で行ってください。また ADR による決定事項に反する変更や SQL インジェクション等のセキュリティ面で問題になりそうな変更、一般的なプログラミングプラクティスに反する変更が存在する場合、それらの指摘もレビュー内容に追加してください。

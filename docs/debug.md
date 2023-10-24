# debug

## vscode launch.json example

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: 現在のファイル",
      "type": "python",
      "request": "launch",
      "console": "integratedTerminal",
      "args": [
        "run",
        "save-precondition",
        "d7349790b1574ce1ac39caf524dda46e",
      ],
      // "args": [
      //   "gpt-review-with-precondition",
      // ],
      "cwd": "${workspaceFolder}",
      "env": {
        "PYTHONPATH": "${workspaceFolder}",
      },
      "module": "poetry",
      "justMyCode": true
    }
  ]
}
```

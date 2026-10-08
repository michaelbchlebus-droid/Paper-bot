name: paper-bot

on:
  schedule:
    - cron: "5 0,4,8,12,16,20 * * *"   # 5 minutes after each 4h bar closes (UTC)
  workflow_dispatch:                    # lets you run it by hand from the Actions tab

permissions:
  contents: write

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run paper bot
        run: python paper_bot.py
      - name: Save account state
        run: |
          git config user.name "paper-bot"
          git config user.email "paper-bot@users.noreply.github.com"
          git add paper_state.json
          git diff --cached --quiet || git commit -m "Update paper account"
          git push

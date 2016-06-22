# emogg

Slackのメッセージに対しReactionをつけることに特化したキーボードです。

## 使用方法

1. `cp config.json.sample config.json`
2. https://api.slack.com/docs/oauth-test-tokens から有効なtokenの値を取得し、auth.jsonのtokenに設定する。(記法はsampleを参照)
3. ハードウェアを適切に準備し、使用するGPIOピンと対応させるReactionをauth.jsonのReactionに設定する。(記法はsampleを参照)
4. `pip install slackclient`
5. `python main.py`

## 動作確認済み環境
Python 3.4.3

## 連絡先
* Email: contact@hideo54.com
* Twitter: @hideo54

# emogg

Slackのメッセージに対しReactionをつけることに特化したキーボードです。

## 使用方法

1. `cp config.json.sample config.json`
2. https://api.slack.com/docs/oauth-test-tokens から有効なtokenの値を取得し、auth.jsonのtokenに設定する。(記法はsampleを参照)
3. ハードウェアを適切に準備し、使用するGPIOピンと対応させるReactionをauth.jsonのReactionに設定する。(記法はsampleを参照)
4. `pip install slackclient`
5. `python main.py`

### ハードウェアの設計方法

「SunPro会誌 2016 技術書典」内の記事「まだReactionで消耗してるの?」を御覧ください。  
[300円でBOOTHにてダウンロード販売を行っています](https://sunpro.booth.pm/items/277203)。2016年12月25日からは無料で公開される予定です。

## 動作確認済み環境
Python 3.4.3

## 連絡先
* Email: contact@hideo54.com
* Twitter: @hideo54

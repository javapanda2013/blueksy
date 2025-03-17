# hello python on bluesky

from atproto import Client

import sys,time,os

client = Client(base_url='https://bsky.social')

# pass入力
# getpass使用
#blueskypass = getpass.getpass(prompt='Password: ')
# osの環境変数使用
blueskypass = os.environ['BLUE_SKY_PASSWORD']

client.login(login='okujotamama.bsky.social',password=blueskypass)

#投稿用の関数
def postBluesky(mes):

	global client
	client.send_post(mes)

# メッセージを入力

while True:
	#最新ポストを取得
	posts = client.app.bsky.feed.post.list(client.me.did, limit=1)
	for uri, post in posts.records.items():
    		print("最新ツイート:",uri, post.text)

	# 入力がなければ終了
	mes = input()
	if mes:
		print("引数を受取")
		postBluesky(mes)
		
	else:
		print("入力が有りません")
		time.sleep(1)
		exit()


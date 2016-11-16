import vkontakte, time, requests, json, datetime

def main():
	vk = vkontakte.API(token='')
	need_user_id = '2000000028'
	need_chat_id = '2000000025'
	sent_to = '2000000028'
	ids_of_unread_messages = ''
	
	server=''
	key=''
	ts=''
	pts=''
	while True:
		if server=='':
			try:
				longpoll = vk.get('messages.getLongPollServer',v='5.60')
				key=longpoll['key']
				server=longpoll['server']
				ts=longpoll['ts']
			except:
				print "Nebernii otvet ot LongPollServer"
				continue
		
		url='https://'+str(server)+'?act=a_check&key='+str(key)+'&ts='+str(ts)+'&wait=30&mode=32&version=1'
		longpoll = requests.post(url)
		json_Object = longpoll.json()

		try:
			pts=json_Object['pts']
			ts=json_Object['ts']
			updates=json_Object['updates']
		except:
			server=''
			key=''
			ts=''
			pts=''
			time.sleep(1);
			continue

		isnewmessages=False
		if updates!=None:
			for update in updates:
				if str(update[0])=='4':
					if str(update[3])==str(need_chat_id):
						ids_of_unread_messages=update[1]
						isnewmessages=True
						print "New Message!"
						break

		if isnewmessages:
			vk.get('messages.send',peer_id=sent_to,forward_messages=str(ids_of_unread_messages),v='5.60')
			vk.get('messages.markAsRead',peer_id=need_chat_id, v='5.60')
		
		ids_of_unread_messages = ''
		time.sleep(1);

if __name__ == '__main__':
	main()

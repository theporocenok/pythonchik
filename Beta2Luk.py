import vkontakte, time, requests, json, sys
	
def CheckUpdates(updates,need_chat_id):
	#print "Updates had taken!"
	ids_of_unread_messages=''
	for update in updates:
		if str(update[0])=='4':
			if str(update[3])==str(need_chat_id):
				ids_of_unread_messages+=str(update[1])
				ids_of_unread_messages+=","
	return ids_of_unread_messages

def main():
	vk = vkontakte.API(token='')
	vlad_id = '279036239'
	need_user_id = '2000000028'
	need_chat_id = '2000000025'
	need_short_chat_id = '25'
	sent_to = '2000000030'
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
		time.sleep(60)
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

		if updates!=None:
			ids_of_unread_messages=CheckUpdates(updates,need_chat_id)
			if ids_of_unread_messages!='':
				try:
					#print("Sent_to: " + str(sent_to) +"\nForward_messages: " + str(ids_of_unread_messages) + "\nLen of ids_of_unread_messages: " + str(len(ids_of_unread_messages)))
					vk.get('messages.send',peer_id=sent_to,forward_messages=str(ids_of_unread_messages),v='5.60')
				except:
					#print("Sent_to: " + str(sent_to) +"\nForward_messages: " + str(ids_of_unread_messages) + "\nLen of ids_of_unread_messages: " + str(len(ids_of_unread_messages)))
					#file_log = open("NotSendedMessages.txt", "a")
					#file_log.write(str(ids_of_unread_messages) +'\n')
					#file_log.close()
					try:
						vk.get('messages.send',peer_id=sent_to,forward_messages=str(ids_of_unread_messages),v='5.60')
					except:
						print('msg not sent:  ' + str(sys.exc_info()[1]))
						print("Forward_messages: " + str(ids_of_unread_messages) + "\nLen of ids_of_unread_messages: " + str(len(ids_of_unread_messages)) + "\nError is: " + str(ex))
						#print(str(ex))
						continue

		ids_of_unread_messages = ''

if __name__ == '__main__':
	main()

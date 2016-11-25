import vkontakte, time, requests, json, sys

def Err(ex):
	file_log = open("/home/pi/py/Brut2LukLog.txt","w")
	file_log.write(str(ex))
	file_log.close()
	
def CheckUpdates(updates,need_chat_id):
	ids_of_unread_messages=''
	for update in updates:
		print(str(update))
		if str(update[0])=='4':
			if str(update[3])==str(need_chat_id):
				ids_of_unread_messages+=str(update[1])
				ids_of_unread_messages+=","
	print("\n\n")
	return ids_of_unread_messages
	
def SendMessage(vk,updates,need_chat_id,sent_to):
	ids_of_unread_messages=CheckUpdates(updates,need_chat_id)
	if ids_of_unread_messages!='':
		try:
			vk.get('messages.send',peer_id=sent_to,forward_messages=str(ids_of_unread_messages),v='5.60')
		except:
			try:
				vk.get('messages.send',peer_id=sent_to,forward_messages=str(ids_of_unread_messages),v='5.60')
			except Exception, ex:
				Err("Forward_messages: " + str(ids_of_unread_messages) + "\nLen of ids_of_unread_messages: " + str(len(ids_of_unread_messages)) + "\nError is: " + str(ex))
	
def main():
	vk = vkontakte.API(token='')
	vlad_id = '279036239'
	need_user_id = '2000000028'
	need_chat_id = '2000000025'
	need_short_chat_id = '25'
	sent_to = '2000000030'
	
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
				print("New longpoll")
			except:
				Err("Nebernii otvet ot LongPollServer")
				continue
		time.sleep(60)
		url='https://'+str(server)+'?act=a_check&key='+str(key)+'&ts='+str(ts)+'&wait=30&mode=32&version=1'
		try:
			longpollsession = requests.post(url)
			json_Object = longpollsession.json()
		except:
			try:
				Err('Json not decoded: ' + str(sys.exc_info()[1])+"\nLongPoll :" + str(longpollsession))
			except:
				Err('Json not decoded: ' + str(sys.exc_info()[1]))
				continue
		
		try:
			pts=json_Object['pts']
			ts=json_Object['ts']
			updates=json_Object['updates']
			print("New update")
		except:
			server=''
			key=''
			ts=''
			pts=''
			#print("Error in JSON object")
			time.sleep(1);
			continue

		if updates!=None:
			SendMessage(vk,updates,need_chat_id,sent_to)
			updates=None

if __name__ == '__main__':
	main()

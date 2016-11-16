import vkontakte, time

def main():
	vk = vkontakte.API(token='')
	need_user_id = '279036239'
	need_chat_id = '2000000025'#2000000000+short_chat_id
	need_short_chat_id = '25'
	sent_to = '279036239'
	last_id_of_unread_messages = ''
	ids_of_unread_messages = ''
	
	server=''
	key=''
	ts=''
	indexs=1
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

		if ts!='':
			try:
				longpoll=vk.get('messages.getLongPollHistory',ts=ts,v='5.60')
			except:
				print "Nebernii otvet ot LongPollHistory"
				key=''
				server=''
				ts=''
				time.sleep(1)
				continue

		if longpoll and ts!='':
			try:
				history=longpoll['history']
				messages=longpoll['messages']
			except:
				key=''
				server=''
				ts=''
				time.sleep(1)
				print "V LongPollHistory net polya 'history' ili 'messages'"
				continue
		
		isnewmessages=False
		if history!=None:
			try:
				for index in range(len(history)):
					if str(len(history[-index]))=='4' and str(history[-index][-1])==need_user_id:
						isnewmessages=True
						break
			except:
				print "Error in proverke na novoe soobshenie from nuzhnii dialog"
				continue

		if isnewmessages:
			items=messages['items']
			for onemessage in items:
				try:
					if str(onemessage['user_id']) == need_user_id and str(onemessage['read_state'])=='0' and str(onemessage['out'])=='0':
						ids_of_unread_messages+=str(onemessage['id'])
						ids_of_unread_messages+=','
						last_id_of_unread_messages=onemessage['id']
				except:
					print "Error in sostavlenii spiska soobshenii"
					continue
			if len(ids_of_unread_messages)>5:
				print(str(ids_of_unread_messages))
				vk.get('messages.send',peer_id=279036239,forward_messages=str(ids_of_unread_messages),v='5.60')
				vk.get('messages.markAsRead',peer_id=need_user_id, start_message_id=last_id_of_unread_messages,v='5.60')
		
		last_id_of_unread_messages = ''
		ids_of_unread_messages = ''
		#print('Time of working: ' + str(indexs)+ ' : ts: ' + str(ts))
		indexs+=1
		time.sleep(1);

if __name__ == '__main__':
	main()

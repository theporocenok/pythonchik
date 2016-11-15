import vkontakte, time

def main():
	vk = vkontakte.API(token='')
	while True:
		unread_messages=-1
		full_message = vk.get('messages.getHistory',offset=unread_messages,count='1',user_id='68881826',start_message_id='-1',v='5.60')
		while full_message['items']!=[]:
			body_of_message = full_message['items']
			id_of_message = body_of_message[0]['id']
			ids_of_unread_messages+= str(id_of_message)
			ids_of_unread_messages+=","
			unread_messages=unread_messages-1
			full_message = vk.get('messages.getHistory',offset=unread_messages,count='1',user_id='68881826',start_message_id='-1',v='5.60')
		vk.get('messages.send',user_id='68881826',forward_messages=ids_of_unread_messages)
		vk.get('messages.markAsRead',peer_id='68881826',message_ids=id_of_message, start_message_id=id_of_message)
		time.sleep(60);
	
if __name__ == '__main__':
    main()
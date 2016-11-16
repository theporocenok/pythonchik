import vkontakte, time

def main():
	vk = vkontakte.API(token='13c403061a24dec856bcafadedb99925a7cd27f91e3773e96fbb2b3d42ca5af0e88371719f26791192fca')
	while True:
		unread_messages=-1
		full_message = vk.get('messages.getHistory',offset=unread_messages,count='1',user_id='102520364',start_message_id='-1',v='5.60')
		ids_of_unread_messages=''
		while full_message['items']!=[]:
			body_of_message = full_message['items']
			id_of_message = body_of_message[0]['id']
			ids_of_unread_messages+= str(id_of_message)
			ids_of_unread_messages+=","
			unread_messages=unread_messages-1
			full_message = vk.get('messages.getHistory',offset=unread_messages,count='1',user_id='102520364',start_message_id='-1',v='5.60')
		if ids_of_unread_messages!='':
			vk.get('messages.send',user_id='395099206',forward_messages=ids_of_unread_messages,v='5.60')
			vk.get('messages.markAsRead',peer_id='102520364',start_message_id=id_of_message,v='5.60')
		time.sleep(60);
	
if __name__ == '__main__':
    main()
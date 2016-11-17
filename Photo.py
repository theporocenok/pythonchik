import vkontakte, time

def TakeBestPhoto(photo_block):
	try:
		photo=photo_block['photo_2560']
	except:
		try:
			photo=photo_block['photo_1280']
		except:
			try:
				photo=photo_block['photo_807']
			except:
				try:
					photo=photo_block['photo_604']
				except:
					try:
						photo=photo_block['photo_130']
					except:
						try:
							photo=photo_block['photo_75']
						except:
							return ("Id: " + photo_block['id'] + "\nOwner_id: " + photo_block['owner_id'] + "\nDate: " + photo_block['date'] + "\nAccess_key :" + photo_block['access_key'] + "\n")
	return photo

def TakePhotoes(vk):
	all_dialogs = vk.get('messages.getDialogs',count='200',v='5.60')
	count_of_dialogs = all_dialogs['count']
	items_in_dialogs = all_dialogs['items']
	all_ids_in_dialogs=[]
	for index in range(len(items_in_dialogs)):
		try:
			temp_id=items_in_dialogs[index]['message']['chat_id']
			all_ids_in_dialogs.append(2000000000+temp_id)
		except:
			temp_id=items_in_dialogs[index]['message']['user_id']
			all_ids_in_dialogs.append(temp_id)
	startfrom=0
	fileids = open("PhotoesURLs.txt","a")
	for i in all_ids_in_dialogs:
		time.sleep(2)
		photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=i,start_from=startfrom,count='200',v='5.60')
		while True:
			time.sleep(2)
			item=photoes_in_one_dialoge['items']
			for in_item in item:
				if str(TakeBestPhoto(in_item['photo']))!='https://vk.com/images/x_null.gif':
					fileids.write(str(TakeBestPhoto(in_item['photo']))+'\n')
			if len(photoes_in_one_dialoge)>1:
				startfrom=photoes_in_one_dialoge['next_from']
				photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=i,start_from=startfrom,count='200',v='5.60')
			else:
				break
	fileids.close()


def TakePhotoesOneDialoge(vk,need_id):
	startfrom=0
	fileids = open("PhotoesURLsFromOneID.txt","a")
	time.sleep(2)
	photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=need_id,start_from=startfrom,count='200',v='5.60')
	while True:
		time.sleep(2)
		item=photoes_in_one_dialoge['items']
		for in_item in item:
			if str(TakeBestPhoto(in_item['photo']))!='https://vk.com/images/x_null.gif':
				fileids.write(str(TakeBestPhoto(in_item['photo']))+'\n')
		if len(photoes_in_one_dialoge)>1:
			startfrom=photoes_in_one_dialoge['next_from']
			photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=need_id,start_from=startfrom,count='200',v='5.60')
		else:
			break
	fileids.close()


def main():
	vk = vkontakte.API(token='')
	TakePhotoesOneDialoge(vk,'')
	
if __name__ == '__main__':
    main()

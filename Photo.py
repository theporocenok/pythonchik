import vkontakte, time

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
	fileids = open("PhotosURLs.txt","a")
	for i in all_ids_in_dialogs:
		time.sleep(2)
		photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=i,start_from=startfrom,count='200',v='5.60')
		while True:
			time.sleep(2)
			item=photoes_in_one_dialoge['items']
			for in_item in item:
				if str(in_item['photo']['photo_604'])!='https://vk.com/images/x_null.gif':
					fileids.write(str(in_item['photo']['photo_604'])+'\n')
			if len(photoes_in_one_dialoge)>1:
				startfrom=photoes_in_one_dialoge['next_from']
				photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=i,start_from=startfrom,count='200',v='5.60')
			else:
				break
	fileids.close()


def TakePhotoesOneDialoge(vk,need_id):
	startfrom=0
	fileids = open("PhotoneedURLs.txt","a")
	time.sleep(2)
	photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=need_id,start_from=startfrom,count='200',v='5.60')
	while True:
		time.sleep(2)
		item=photoes_in_one_dialoge['items']
		for in_item in item:
			if str(in_item['photo']['photo_604'])=='https://vk.com/images/x_null.gif':
				fileids.write(str(in_item['photo']['photo_604'])+'\n')
		if len(photoes_in_one_dialoge)>1:
			startfrom=photoes_in_one_dialoge['next_from']
			photoes_in_one_dialoge = vk.get('messages.getHistoryAttachments',media_type='photo',peer_id=need_id,start_from=startfrom,count='200',v='5.60')
		else:
			break
	fileids.close()


def main():
	vk = vkontakte.API(token='13c403061a24dec856bcafadedb99925a7cd27f91e3773e96fbb2b3d42ca5af0e88371719f26791192fca')
	TakePhotoes(vk)
	
if __name__ == '__main__':
    main()

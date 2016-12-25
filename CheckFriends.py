#!/usr/bin/env python
# -*- coding: utf-8 -*-
import vkontakte,time,sys,config

def friend_list(vk, userid):
	friends=vk.get('friends.get',user_id=userid,v='5.60')
	file_friends = open("friends"+str(userid)+".txt","a")
	for item in friends['items']:
		file_friends.write(str(item)+'\n')
	file_friends.close()

def find_friend(friends,user,userid):
	for friend in friends:
		if str(friend)==str(userid):
			return ('')
	return (str(user)+',')

def get_names(vk,ids):
	if ids!='':
		toreturn=''
		names=vk.get('users.get',user_ids=str(ids),v='5.60')
		for name in names:
			toreturn+= '%-10s %s\n' % (name['first_name'], name['last_name'])
		print toreturn

def find_from_other_users(vk,file_friends, userid):
	count=0
	unfriends=''
	deactivated=''
	for line in file_friends:
		try:
			temp=vk.get('friends.get',user_id=line,v='5.60')
			temps=find_friend(temp['items'],line,userid)
			if temps=='':
				count+=1
			else:
				unfriends+=temps
		except:
			temp=vk.get('users.get',user_ids=str(line),v='5.60')
			try:
				if temp[0]['deactivated']:
					deactivated+=line+','
			except:
				temp=vk.get('friends.get',user_id=line,v='5.60')
				temps=find_friend(temp['items'],line,userid)
				if temps=='':
					count+=1
				else:
					unfriends+=temps
				continue
			continue
		time.sleep(1)

	if deactivated!='':
		print (u'Удалённые друзья:')
		get_names(vk,deactivated)

	if unfriends!='':
		print (u'Скрывающие друзья:')
		get_names(vk,unfriends)

	print (u'Кол-во нескрывающих друзей: ' + str(count))

def find_from_followers(vk,file_friends,userid):
	count=0
	new_followers=''
	followers = vk.get('users.getFollowers',user_id=userid,v='5.60')
	for follower in followers['items']:
		for line in file_friends:
			if follower==line:
				new_followers+=line+','

	if new_followers!='':
		print (u'Новые подписчики из бывших друзей: \n')
		get_names(vk,new_followers)

vk = vkontakte.API(token=config.vk_token,v='5.60')

lukid='102520364'
nid='41300965'
user=nid

friend_list(vk, user)

file_friends = open("friends"+str(user)+".txt","r")

friends_ids=[]
count=0
for line in file_friends:
	friends_ids.append(line[0:len(line)-1])
	count+=1

print(u'Всего друзей: ' + str(count)+'\n')

find_from_other_users(vk,friends_ids,user)
find_from_followers(vk,friends_ids,user)

file_friends.close()

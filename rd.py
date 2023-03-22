data = []
count = 0

#for loop的程序是把清单里面的东西一个一个拿出来。
with open('reviews.txt', 'r') as read:  #打开reviews.txt的档案，‘r’是read的意思， as read 取名为read

	for line in read:  #每次都读取read文件里面的一行
		#data.append(line.strip())   # strip把line的每行都去掉空格，data.append是把数据加入data的文件中
		data.append(line) #把每个line的数据加到data里
		count = count + 1
		if count % 1000 ==0: #每1000次才打印出现进度
			print(len(data)) #显示读取进度
print(len(data))  #data文件的数据数量

print(data[0])

wc = {} # meaning word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key进wc字典
for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

while True:
	word = input('请问你想查什么字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现过的次数为：', wc[word])
	else:
		print('没有这个字哦')

print('感谢使用')
#print(wc)

#print(words)







#print(data) #打印出data文件所有数据
#print(data[0])  #读取data文件里面的第一个数据
#print('---------------')
#print(data[1])

#sum_len = 0 #先设置一个总长度的数据框架
#for d in data: #用d代表data里面的每个长度
#	sum_len = sum_len + len(d) #每个长度都加起来
#	avg = sum_len/len(data) #总数除去总长度
#print('留言长度是 ', sum_len)
#print('平均的长度是 ', avg)

#new = []
#for d in data: #
#	if len(d) < 100:
#		new.append(d)
#print('有', len(new) ,'个平均长度少于100')
#print(new[0])

#good = []
#for d in good:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '好评')
#print(good[0])



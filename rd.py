data = []
count = 0
with open('reviews.txt', 'r') as read:  #打开reviews.txt的档案，‘r’是read的意思， as read 取名为read

	for line in read:  #每次都读取read文件里面的一行
		#data.append(line.strip())   # strip把line的每行都去掉空格，data.append是把数据加入data的文件中
		data.append(line)
		count = count + 1
		if count % 1000 ==0: #每1000次才打印出现进度
			print(len(data)) #显示读取进度
print(len(data))  #data文件的数据数量
#print(data) #打印出data文件所有数据
print(data[0])  #读取data文件里面的第一个数据
print('---------------')
print(data[1])

sum_len = 0 #先设置一个总长度的数据框架
for d in data: #用d代表data里面的每个长度
	sum_len = sum_len + len(d) #每个长度都加起来
	avg = sum_len/len(data) #总数除去总长度
print('留言长度是 ', sum_len)
print('平均的长度是 ', avg)


import os  # 判断文件存在
import re  # 正则表达式提取文本
import requests  # 发送请求
import pandas as pd  # 存取csv文件
import datetime  # 转换时间用

# 请求头
headers = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
}


def trans_time(v_str):
	"""转换GMT时间为标准格式"""
	GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
	timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
	ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
	return ret_time


def get_containerid(v_loc):
	"""
	获取地点对应的containerid
	:param v_loc: 地点
	:return: containerid
	"""
	url = 'https://m.weibo.cn/api/container/getIndex'
	# 请求参数
	params = {
		"containerid": "100103type=92&q={}&t=".format(v_loc),
		"page_type": "searchall",
	}
	r = requests.get(url, headers=headers, params=params)
	cards = r.json()["data"]["cards"]
	scheme = cards[0]['card_group'][0]['scheme']  # 取第一个
	if '&' in scheme:
		containerid = re.findall(r'containerid=(.*?)&', scheme)[0]
	else:
		containerid = scheme.replace("https://m.weibo.cn/p/index?containerid=", "")
	print('[{}]对应的containerid是：{}'.format(v_loc, containerid))
	return containerid


def getLongText(v_id):
	"""爬取长微博全文"""
	url = 'https://m.weibo.cn/statuses/extend?id=' + str(v_id)
	r = requests.get(url, headers=headers)
	json_data = r.json()
	long_text = json_data['data']['longTextContent']
	# 微博内容-正则表达式数据清洗
	dr = re.compile(r'<[^>]+>', re.S)
	long_text2 = dr.sub('', long_text)
	# print(long_text2)
	return long_text2


def get_location(v_text):
	"""
	从博文中提取签到地点
	:param v_text: 博文
	:return: 地点
	"""
	if v_text:
		try:
			loc = re.findall(r'<span class=\"surl-text\">(.*?)</span>', v_text)[-1]  # 取出最后一个
		except:
			loc = ''
		return loc
	else:
		return ''


def get_weibo_list(v_keyword, v_max_page):
	"""
	爬取微博内容列表
	:param v_keyword: 搜索关键字
	:param v_max_page: 爬取前几页
	:return: None
	"""
	containerid = get_containerid(v_loc=v_keyword)
	for page in range(2, v_max_page + 1):
		print('===开始爬取第{}页微博==='.format(page))
		# 请求地址
		url = 'https://m.weibo.cn/api/container/getIndex'
		# 请求参数
		params = {
			"containerid": containerid,
			"luicode": "10000011",
			# "lcardid": "frompoi",
			# "extparam": "frompoi",
			"lfid": "100103type=92&q={}".format(v_keyword),
			"page": page,
		}
		# 发送请求
		r = requests.get(url, headers=headers, params=params)
		print(r.status_code)  # 查看响应码
		# 解析json数据
		try:
			card_group = r.json()["data"]["cards"][0]['card_group']
		except:
			card_group = []
		print(card_group)
		time_list = []  # 创建时间
		author_list = []  # 微博作者
		id_list = []  # 微博id
		bid_list = []  # 微博bid
		text_list = []  # 博文
		text2_list = []  # 博文2
		loc_list = []  # 签到地点
		reposts_count_list = []  # 转发数
		comments_count_list = []  # 评论数
		attitudes_count_list = []  # 点赞数
		for card in card_group[1:]:
			# 微博创建时间
			try:
				create_time = trans_time(card['mblog']['created_at'])
			except:
				create_time = ''
			time_list.append(create_time)
			# 微博作者
			try:
				author = card['mblog']['user']['screen_name']
			except:
				author = ''
			author_list.append(author)
			# 微博id
			id = card['mblog']['id']
			id_list.append(id)
			# 微博bid
			bid = card['mblog']['bid']
			bid_list.append(bid)
			# 微博博文
			text = card['mblog']['text']
			text_list.append(text)
			# 微博内容-正则表达式数据清洗
			dr = re.compile(r'<[^>]+>', re.S)
			text2 = dr.sub('', text)  # 正则表达式提取微博内容
			text2_list.append(text2)
			# 判断是否存在全文
			try:
				isLongText = card['mblog']['isLongText']
				if isLongText == True:
					long_text = getLongText(id)
					text2_list[-1] = long_text  # 把text2_list中的最后一个博文替换成long_text
			except:
				pass
			# 签到地点
			loc = get_location(v_text=text)
			loc_list.append(loc)
			# 转发数
			try:
				reposts_count = card['mblog']['reposts_count']
			except:
				reposts_count = ''
			reposts_count_list.append(reposts_count)
			# 评论数
			try:
				comments_count = card['mblog']['comments_count']
			except:
				comments_count = ''
			comments_count_list.append(comments_count)
			# 点赞数
			try:
				attitudes_count = card['mblog']['attitudes_count']
			except:
				attitudes_count = ''
			attitudes_count_list.append(attitudes_count)
		print('微博数量：', len(text2_list))
		# 把列表数据保存成DataFrame数据
		df = pd.DataFrame(
			{
				'页码': page,
				'微博id': id_list,
				'微博bid': bid_list,
				'微博作者': author_list,
				'发布时间': time_list,
				'微博内容': text2_list,
				'签到地点': loc_list,
				'转发数': reposts_count_list,
				'评论数': comments_count_list,
				'点赞数': attitudes_count_list,
			}
		)
		# 表头
		if os.path.exists(v_weibo_file):
			header = False
		else:
			header = True
		# 保存到csv文件
		df.to_csv(v_weibo_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
		print('csv保存成功:{}'.format(v_weibo_file))


if __name__ == '__main__':
	# 爬取前几页
	max_search_page = 10  # 爬前n页
	# 爬取关键字
	search_keyword = '桂林路'
	# 保存文件名
	v_weibo_file = '微博清单_{}_前{}页.csv'.format(search_keyword, max_search_page)
	# 如果csv文件存在，先删除之
	if os.path.exists(v_weibo_file):
		os.remove(v_weibo_file)
		print('微博清单存在，已删除: {}'.format(v_weibo_file))
	# 调用爬取微博函数
	get_weibo_list(v_keyword=search_keyword, v_max_page=max_search_page)
	# 数据清洗-去重
	df = pd.read_csv(v_weibo_file)
	# 删除重复数据
	df.drop_duplicates(subset=['微博bid'], inplace=True, keep='first')
	# 删除作者为空的数据
	df.drop(df[df.微博内容 == '抱歉，此微博已被删除。查看帮助： 网页链接'].index, axis=0, inplace=True)
	# 再次保存csv文件
	df.to_csv('去重后_' + v_weibo_file, index=False, encoding='utf_8_sig')
	print('数据清洗完成')

import json
import re
import requests
from one import OneNote
from xhs_utils.xhs_util import get_headers, get_search_data, get_params, js, check_cookies, handle_profile_info


class Search:
    def __init__(self, cookies=None):
        if cookies is None:
            self.cookies = check_cookies()
        else:
            self.cookies = cookies
        self.search_url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
        self.headers = get_headers()
        self.params = get_params()
        self.oneNote = OneNote(self.cookies)

    def get_search_note(self, query, number):
        data = get_search_data()
        api = '/api/sns/web/v1/search/notes'
        data = json.dumps(data, separators=(',', ':'))
        data = re.sub(r'"keyword":".*?"', f'"keyword":"{query}"', data)
        page = 0
        note_ids = []
        while len(note_ids) < number:
            page += 1
            data = re.sub(r'"page":".*?"', f'"page":"{page}"', data)
            ret = js.call('get_xs', api, data, self.cookies['a1'])
            self.headers['x-s'], self.headers['x-t'] = ret['X-s'], str(ret['X-t'])
            response = requests.post(self.search_url, headers=self.headers, cookies=self.cookies,
                                     data=data.encode('utf-8'))
            res = response.json()
            print(res)
            if not res['data']['has_more']:
                print(f'搜索结果数量为 {len(note_ids)}, 不足 {number}')
                break
            items = res['data']['items']
            for note in items:
                note_id = note['id']
                note_ids.append(note_id)
                if len(note_ids) >= number:
                    break
        return note_ids

    def handle_note_info(self, query, number, sort, need_cover=False):
        request_data = get_search_data()
        request_data['keyword'] = query
        request_data['sort'] = sort
        request_data = json.dumps(request_data, separators=(',', ':'))
        request_data = re.sub(r'"keyword":".*?"', f'"keyword":"{query}"', request_data)
        api = '/api/sns/web/v1/search/notes'
        page = 0
        index = 0
        result = []
        with open('./datas_search/result.csv', 'a', encoding='utf8') as f:
            f.write(
                '用户id,用户昵称,ip地址,评论内容,用户签名,评论时间,笔记id,发布时间,标题,评论数量,收藏数量,喜欢数量,分享数量,作者昵称,作者签名\n')

            while index < number:
                page += 1
                request_data = re.sub(r'"page":".*?"', f'"page":"{page}"', request_data)
                ret = js.call('get_xs', api, request_data, self.cookies['a1'])
                self.headers['x-s'], self.headers['x-t'] = ret['X-s'], str(ret['X-t'])
                response = requests.post(self.search_url, headers=self.headers, cookies=self.cookies,
                                         data=request_data.encode('utf-8'))
                res = response.json()
                try:
                    items = res['data']['items']
                except:
                    print(f'搜索结果数量为 {index}, 不足 {number}')
                    break
                for note in items:
                    index += 1
                    note_info = self.oneNote.get_one_note_info('', note['id'])
                    if not note_info:
                        continue
                    user_info = self.get_profile(note['note_card']['user']['user_id'])
                    comments = self.get_comment(note['id'])
                    cc = 0
                    if len(comments) > 0:
                        for comment in comments:
                            data = {**comment}
                            if cc == 0:
                                data['id'] = note_info.note_id
                                data['upload_time'] = note_info.upload_time
                                data['title'] = note_info.desc.replace("\n", "")
                                data['comment_count'] = note_info.comment_count
                                data['collect_count'] = note_info.collected_count
                                data['digg_count'] = note_info.liked_count
                                data['share_count'] = note_info.share_count
                                data['blogger_name'] = user_info.nickname
                                data['blogger_signature'] = user_info.interaction
                            cc += 1
                            line = str(data['user_id']) \
                                   + ',' \
                                   + str(data['nickname']) \
                                   + ',' + str(data.get('ip_location', '')) \
                                   + ',' + str(data['content']) + ',' \
                                   + str(data.get('signature', '')) \
                                   + ',' + str(data['create_time']) \
                                   + ',' + str(data.get('id', '')) \
                                   + ',' \
                                   + str(data.get('upload_time', '')) \
                                   + ',' \
                                   + str(data.get('title', '')) \
                                   + ',' \
                                   + str(data.get('comment_count', '')) \
                                   + ',' + str(data.get('collect_count', '')) \
                                   + ',' \
                                   + str(data.get('digg_count', '')) \
                                   + ',' + str(data.get('share_count', '')) \
                                   + ',' \
                                   + str(data.get('blogger_name', '')) \
                                   + ',' \
                                   + str(data.get('blogger_signature', '')) \
                                   + '\n'
                            print(line)
                            f.write(str(line))
                            result.append(data)
                    if index >= number:
                        break
                if not res['data']['has_more'] and index < number:
                    print(f'搜索结果数量为 {index}, 不足 {number}')
                    break
            print(f'搜索结果全部下载完成，共 {index} 个笔记')

        f.close()

    def get_profile(self, userId):
        url = 'https://www.xiaohongshu.com/user/profile/' + userId
        headers = get_headers()
        response = requests.get(url, headers=headers, cookies=self.cookies)
        html_text = response.text
        profile = handle_profile_info(userId, html_text)
        return profile

    def get_comment(self, note_id):
        comments = []
        url = 'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page'
        params = {
            'note_id': note_id,
            'image_formats': 'jpg,webp,avif',
            'cursor': '',
            'top_comment_id': ''
        }
        has_more = True
        i = 1
        while has_more:
            response = requests.get(url, params=params, cookies=self.cookies)
            res = response.json()['data']
            has_more = res['has_more'] or res.get('cursor')
            params['cursor'] = res.get('cursor', '')
            for c in res['comments']:
                print(f"第{i}条评论：{c['content']}")
                comment = {
                    'user_id': c['user_info']['user_id'],
                    'nickname': c['user_info']['nickname'],
                    'ip_location': c.get('ip_location', ''),
                    'content': c['content'].replace("\n", ""),
                    'create_time': c['create_time']
                }
                # p = self.get_profile(c['user_info']['user_id'])
                # comment['signature'] = p.interaction
                comments.append(comment)
                i += 1
        return comments

    def main(self, info):
        query = info['query']
        number = info['number']
        sort = info['sort']
        self.handle_note_info(query, number, sort, need_cover=True)


if __name__ == '__main__':
    search = Search()
    # 搜索的关键词 
    query = '预制菜'
    # 搜索的数量（前多少个）
    number = 2000
    # 排序方式 general: 综合排序 popularity_descending: 热门排序 time_descending: 最新排序
    sort = 'popularity_descending'
    info = {
        'query': query,
        'number': number,
        'sort': sort,
    }
    search.main(info)

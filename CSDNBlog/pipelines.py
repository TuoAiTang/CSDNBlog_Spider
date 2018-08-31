import json
import codecs
import pymysql


class CsdnblogPipeline(object):

    def __init__(self):
        self.file = open('CSDNBlog_data.json', mode='wb')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # print("TYPE OF LINE:" + str(type(line)))
        # print("CONTENT OF LINE:" + line)
        # self.file.write(line.encode('utf8'))
        db = pymysql.connect(host="localhost", user="root",
                             password="admin", db="csdn", port=3306)
        cur = db.cursor()
        sql_insert = """insert into all_blog values(null, '%s', '%s')
        """ %(item['article_name'], item['article_url'])

        try:
            cur.execute(sql_insert)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()


        return item

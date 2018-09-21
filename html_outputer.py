# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):  # 构造函数
        self.datas = []  # 列表

    def collect_data(self, data):
        if data is None:  # 为空
            return
        self.datas.append(data)  # 把数据添加到列表中

    def output_html(self):
        fout = open('output.html', 'w')  # 以写的模式建立一个文件对象
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")  # 以表格的形式展示
        for data in self.datas:
            print(data['url'], data['title'], data['summary'])
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            # 设置编码会出现乱码
            # fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title'])
            # fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()  # 关闭文件
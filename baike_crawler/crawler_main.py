from baike_crawler import url_manager, html_downloader, html_parser, html_outputer


class CrawlerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)    #加入入口url
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()    #获取url
            html_cont = self.downloader.download(new_url)       #下载
            new_urls, new_data = self.parser.parse(new_url, html_cont)        #解析
            self.urls.add_new_urls(new_urls)    #加入解析出的新url
            self.outputer.collect_data(new_data)     #收集数据
        self.outputer.output_html()      #输出数据


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_crawler = CrawlerMain()
    obj_crawler.craw(root_url)
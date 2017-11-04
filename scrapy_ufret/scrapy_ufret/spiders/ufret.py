import scrapy
from scrapy_ufret.items import Title


class UfretSpider(scrapy.Spider):
    # Spiderの名前
    name = 'ufret'
    # クロール対象とするドメインのリスト
    allowed_domains = ['ufret.jp']
    # クロールを開始するURLのリスト。1要素のタプルの末尾にはカンマが必要。
    start_urls = [ \
              'http://ufret.jp/' \
            , 'http://www.ufret.jp/song.php?data=40140' \
            ]

    def parse(self, response):
        '''
        Spiderを実行すると、start_urlsに指定したURLのページを取得し、
        scrapy.Responseオブジェクトを引数としてparse()メソッドが呼び出される。
        '''
        for t in response.css('h1').css('strong::text').extract():
            item = Title()
            item['title'] = t
            # Titleインスタンスを返す
            # コマンド scrapy crawl ufret -o output.jlで結果を出力できる
            yield item



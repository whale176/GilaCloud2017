import requests
from lxml import etree

# Choose which ptt board url u would like to visit.
search_topic = 'https://www.ptt.cc/bbs/ToS/index.html'
page = requests.get(search_topic).text
tree = etree.HTML(page)

# Parse the html content
posts_reg = '//div[@class="r-ent"]/descendant::text()'
rough_posts = tree.xpath(posts_reg)

# test for the results
print(rough_posts)

# 2nd way to get the results
post_title = tree.xpath('//div[@class="title"]/a/text()')
post_date = tree.xpath('//div[@class="meta"]/div[@class="date"]/text()')

# test for teh results
print(post_title)
print(post_date)

# Next, Should soup the html results.

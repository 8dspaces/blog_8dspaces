import requests
def get_page(url):
    try:
        import requests
        page = requests.get(url)  # example "http://www.douban.com"
        return page.text
    except:
        return ""
    
def get_all_links(page):
    
    links = []
    begin_link = page.find("<a href=")
    while begin_link > 0:
        start_quote = page.find('"', begin_link)
        end_quote = page.find('"', start_quote+1)
        url = page[start_quote+1: end_quote]
        if url not in links:
            links.append(url)
        page = page[end_quote+1:]
        begin_link = page.find("<a href=")
        
    return links
    
def add_to_index(index, keyword, url):

    # for entry in index:
        # if entry[0] == keyword:
            # if url not in entry[1]:
                # entry[1].append(url)
                # return 
    # index.append([keyword,[url]])
    if keyword in index:
        if url not in index[keyword]: 
            index[keyword].append(url)
    else:
        index[keyword] = [url]

def add_to_index_2(index, keyword, url):
    # new format of data structure [keyword, [[url, count],[url,count]]]
    # the count can be used to track the popularity of the url
    for entry in index:
        if entry[0] == keyword:
            for element in entry[1]:
                if element[0] == url:
                    element[1] = element[1] + 1
                    return 
    # if it's a new keywords, just add it 
    index.append([keyword,[url,0]])
    
def look_up(index, word):
    
    # for entry in index:
        # if entry[0] == word:
            # return entry[1]
    # return []
    if word in index:
        return index[word]
    else:
        return []
    
def add_page_to_index(index,url,content):
    
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index, keyword, url)
        
def crawl_web(seed):
    
    tocrawl = [seed]
    crawled = []
    #index = []
    index = {}
    while tocrawl:
        urlpage = tocrawl.pop()
        if urlpage not in crawled:
            content = get_page(urlpage)  # get page will use requests 
            add_page_to_index(index, keyword, urlpage)
            crawled.append(urlpage)
            urls = get_all_links(content)
            for i in urls:
                if i not in tocrawl:
                    tocrawl.append(i)
    return index


if __name__ == "__main__":
    index = []
    add_page_to_index(index, "help.page","just a test")
    add_page_to_index(index, "wooho.page","test a page")
    for i in index:
        print i
        
        
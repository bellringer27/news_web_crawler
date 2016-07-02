import urllib2
import codecs
def remove_html(string):
    while(string.find("<")!=-1):
        string = string[:string.find("<")]+""+string[string.find(">")+1:]
    while(string.find("&nbsp;")!=-1):
        string = string[:string.find("&nbsp;")]+" "+string[string.find("&nbsp;")+6:]
    return string
while True:
    print"Enter the URL you wish to crawl..."
    print'Usage -"http://phocks.org/stumble/creepy/"<-- With the double quotes'
    myurl = input("@>")
    response = urllib2.urlopen(myurl)
    orig_page_source =page_source=response.read()
    data=""
    if(myurl.find("cnn")!=-1):
        title = page_source[(page_source.find("<h1 class=\"pg-headline\">")+24):page_source.find("</h1>")]
        page_source = page_source[page_source.find("</h1>")+5:]
        page_source = page_source[page_source.find("<span class=\"metadata__byline__author\">")+39:]
        author = page_source[:page_source.find("</span>")]
        author = remove_html(author)
        page_source = page_source[page_source.find("</span>")+7:]
        page_source = page_source[page_source.find("<p class=\"update-time\">")+23:]
        date = page_source[:page_source.find("<span id=\"js-pagetop_video_source\" class=\"video__source top_source\"></span></p>")]
        page_source = page_source[page_source.find("<span id=\"js-pagetop_video_source\" class=\"video__source top_source\"></span></p>")+85:]
        while(page_source.find("<div class=\"zn-body__paragraph\">")!=-1):
            beg=page_source.find("<div class=\"zn-body__paragraph\">")
            page_source=page_source[beg:]
            end=page_source.find("</div>")
            data = data +"\n"+remove_html(page_source[beg:end])
            print(remove_html(page_source[beg:end]))
            page_source = page_source[end+6:]
    else:
        page_source = page_source[page_source.find("articleInfo")+11:]
        title=page_source[(page_source.find("summary:\"<p>")+12):page_source.find("<\/p>")]
        author = "N/A"
        page_source = page_source[page_source.find("pubDate:\"")-1:]
        date = page_source[page_source.find("pubDate:\"")+8:page_source.find("\",")]
        page_source = page_source[page_source.find("<div class=\"article-text\">"):]
        temp_source = page_source[:page_source.find("</div>")]
        page_source = page_source[page_source.find("</div>")+6:]
        while(temp_source.find("<p>")!=-1):
            data = data +"\n"+remove_html(temp_source[temp_source.find("<p>")+3:temp_source.find("</p>")])
            temp_source = temp_source[temp_source.find("</p>")+4:]
    try:
        data = data.encode('UTF-8')
        #data = data.decode('Latin-1')
    except:
        lol = "wat"
    print("Title: "+title)
    print("Author: "+author)
    print("Date: "+date)
    print("Data: "+data)
    print"Successfully added to the database"

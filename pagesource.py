import urllib2
def remove_html(string):
    while(string.find("<")!=-1):
        string = string[:string.find("<")]+""+string[string.find(">")+1:]
    return string
while True:
    print"Enter the URL you wish to crawl..."
    print'Usage -"http://phocks.org/stumble/creepy/"<-- With the double quotes'
    myurl = input("@>")
    response = urllib2.urlopen(myurl)
    orig_page_source =page_source=response.read()
    #print(page_source)
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
         #   print(data)
        #page_source = page_source[page_source.find("<div class=\"zn-body__paragraph\">")-1:]
        #data=page_source[page_source.find("<div class=\"zn-body__paragraph\">")+32:page_source.find("</div>")]
        print("Title: "+title)
        print("Author: "+author)
        print("Date: "+date)
        #print("Data: "+data)
    #else:
        
    #print(data)
    print"Successfully added to the database"

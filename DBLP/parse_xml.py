import xml.sax

class PublicationHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentType = ""
        self.CurrentData = ""
        self.pubkey = ""
        self.title = ""
        self.journal = ""
        self.year = ""
        self.book_title = ""
        self.author = ""
    
    # Call when an element starts
    def startElement(self, tag, attributes):
        if tag == "article" or tag == "inproceedings":
            self.CurrentType = tag
            print "**********", tag
            self.pubkey = attributes['key']
            print "pubkey:", self.pubkey
        elif self.CurrentType == "article" or self.CurrentType == "inproceedings":
            self.CurrentData = tag
    
    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentType == "article" or self.CurrentType == "inproceedings":
            if tag == "article" or tag == "inproceedings":
                self.CurrentType = ""
                
            elif self.CurrentData == "title":
                print "Title:", self.title
            elif self.CurrentData == "journal":
                print "Journal:", self.journal
            elif self.CurrentData == "year":
                print "Year:", self.year
            elif self.CurrentData == "booktitle":
                print "Book title:", self.book_title
            elif self.CurrentData == "author":
                print "Author:", self.author
        self.CurrentData = ""
        
    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "title":
            self.title  = content
        elif self.CurrentData == "journal":
            self.journal  = content
        elif self.CurrentData == "year":
            self.year  = content
        elif self.CurrentData == "booktitle":
            self.book_title  = content
        elif self.CurrentData == "author":
            self.author = content
            print "check parsing author:", content

    
    
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = PublicationHandler()
parser.setContentHandler( Handler )

parser.parse(os.path.join(root, xml_f_name))

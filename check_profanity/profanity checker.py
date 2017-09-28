import urllib

def read_text():
    quotes= open("/Users/shabadlamba/Documents/my python programs/Python Foundation with Python/check_profanity/movie_quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()
    profanity_check(contents_of_file)
    
def profanity_check(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print output
    connection.close()
    
read_text()

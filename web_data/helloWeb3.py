'''Prompt the user for a name, and display a web page including the name,
taking the web page template from a file.'''

def fileToStr(fileName): # NEW
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def main():
    person = input('Enter a name: ')  
    contents = fileToStr('helloTemplate.html').format(**locals())   # NEW
    browseLocal(contents) 

def strToFile(text, filename):  
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()

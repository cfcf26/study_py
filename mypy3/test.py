import re

def regexStrip(string,characters):
    mo = spaceStripRegex.search(string) # Calls upon the global regex for separating left and right white space from content
    string = mo.group(2)    # Isolates the string content from bounding white space and re-assigns it to a variable
    
    characters = '[' + characters + ']' # Stores other characters to be stripped in format compatible with character class
    
    # Regex for stripping other characters contains argument built via string concatenation as opposed to single raw string
    characterStripRegex = re.compile(
        '^' + characters + '*' +    # Zero or more of the characters to be stripped on left side of content
        r'(.*?)' +  # Defines unstripped content as the only group. Nongreedy so as not to include characters to be stripped on right side 
        characters + '*$')  # Zero or more of the characters to be stripped on the right side of the content
    mo = characterStripRegex.search(string)
    string = mo.group(1)
    print(string)
    
# Global regex that groups initial string into left white space, content, and right white space
spaceStripRegex = re.compile(r'''
    ^(\s)*  # Left white space if any
    (.*?)   # String content
    (\s)*$  # Right white space if any
    ''', re.VERBOSE)

string = '  **SpamSpamBaconSpamEggsSpamSpam   '
characters = 'ampS*'

regexStrip(string,characters)
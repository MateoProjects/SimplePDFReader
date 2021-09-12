import pdfplumber

"""
Process text. Receives one text and try to find all data that we can interpret in terms of medicine.
"""


def processText(text):
    """
    Function for clean text
    :param text: Text that you need to clean in form of list.
    :return: return Clean Text
    """
    print(type(text))
    for line in text:
        print(line)
    return text


class ReaderFile:
    """
    Class for Reader Files
    """

    def __init__(self, path):
        """
        Constructor
        :param path: Path where PDF is stored
        """
        self.path = path



    def readFile(self):
        """
        Function thats reads PDF
        :return: Returns the text after passing through a filter to clean the text.
        """
        with pdfplumber.open(self.path) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            text = text.split('\n')
            return processText(text)

from pdfreader import SimplePDFViewer

class Scrapper:

    """This is a general scrapper tool used to extract data from college catologs and put
    them into a JSON file"""

    def __init__(self, fl: str):
        fd = open(fl, 'rb')
        self._parser = SimplePDFViewer(fd)

    def get_metadata(self):
        return self._parser.metadata

    def get_page(self, file_path: str, page=1):
        #self._parser.navigate(page)
        self._parser.render()
        stored = self._parser.canvas.text_content
        with open(file_path, "w") as f:
            f.write(stored)



if __name__ == '__main__':
    test_case = Scrapper(r"D:\timsa\OneDrive\Documents\GitHub\academic_advisor\data\PDFs\example-text-crash-report.pdf")
    print(test_case.get_metadata())
    print(test_case.get_page(r"D:\timsa\OneDrive\Documents\GitHub\academic_advisor\data\courses\template.txt"))


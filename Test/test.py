from docx import Document
search = "1-2 П9"
def add_rasp(search):
    doc = Document("testdoc.docx")

    tables = doc.tables

    text = ""

    for i in range(len(tables[1].rows)):
        if i%5 == 0:
            for j in range(len(tables[1].rows[i].cells)):
                if j%3==0:
                    #print(j)
                    if search == tables[1].rows[i].cells[j].text.strip():
                        text += tables[1].rows[i].cells[j].text.strip() + '\t'
                        text += tables[1].rows[i].cells[j+2].text.strip() + '\n'
                        for k in range(1, 5):
                            text += tables[1].rows[i+k].cells[j].text.strip() + '\t'
                            text += tables[1].rows[i+k].cells[j+1].text.strip() + '\t'
                            text += tables[1].rows[i+k].cells[j+2].text.strip() + "\n"
                        print(text)
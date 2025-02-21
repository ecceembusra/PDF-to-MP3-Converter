import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def PdfToText(pdf_path):
    text_=""
    pdf_read=PyPDF2.PdfReader(open(pdf_path,'rb'))
    for page_no in range(len(pdf_read.pages)):
        text_ +=pdf_read.pages[page_no].extract_text()
    
    return text_

def TextToMp3(text_,output):
    trans=gTTS(text=text_,lang='tr')
    trans.save(output)


def selectFile():
    file_=filedialog.askopenfilename(filetypes=[("PDF Files","*pdf")])
    if file_:
        pdf_text=PdfToText(file_)
        TextToMp3(pdf_text,"newPlayer.mp3")
        os.system("start newPlayer.mp3")


app=tk.Tk()
app.title("Book Reading App")
app.geometry("250x150")

button_=tk.Button(app,text="SELECT PDF",command=selectFile,bg="white",fg="blue",highlightbackground = "blue",highlightthickness = 12,padx=20,pady=20)
button_.pack(pady=20)
app.mainloop()
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from tkinter import *
from tkinter import messagebox

def enviar_email():
    try:
        if entry_email.get() == '':
            messagebox.showerror('ERRO', 'Preencha o campo de E-mail.')
        else:
            Email_Enviar = "email@gmail.com" # Colocar o email que vai enviar mensagem
            Senha_enviar = 'senha' # Colocar a senha do email
            Email_Receber = entry_email.get() 
            # Instância do MIMEMultipart
            msg = MIMEMultipart()
            msg['From'] = Email_Enviar
            msg['To'] = Email_Receber

            # Titulo da mensagem
            msg['Subject'] = "Email via Python"

            body = text_send.get("1.0",'end-1c')
            print(body)

            msg.attach(MIMEText(body, 'plain'))

            #Servidor SMTP
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.ehlo()
            # Segurança
            s.starttls()
            s.ehlo()
            s.login(Email_Enviar, Senha_enviar)
            
            # Converte para String
            text = msg.as_string()
            
            s.sendmail(Email_Enviar, Email_Receber, text)
            s.quit()

            messagebox.showinfo('SUCESSO', 'E-mail enviado com sucesso!')
            entry_email.delete('0', END)
            text_send.delete('0.0', END)

    except Exception as e:
        print("O erro é =", e)

if __name__ == "__main__":
    janela = Tk()
    janela.title("Python E-mail")
    BACKGROUND = "#004080"
    janela['background'] = BACKGROUND
    janela.geometry("700x450")
    janela.resizable(False, False)
    label_title = Label(janela,background='darkgreen',fg='white',height=2, font='arial 22',text='Enviar e-mail com python (Gmail)')
    label_title.pack(fill= X, side=TOP)

    label_text = Label(janela, text='Enviar para: teste@gmail.com', font='arial 14 bold', bg=BACKGROUND, fg='white')
    label_text.place(x=50,y=100)

    entry_email = Entry(janela, font='arial 13', width=65)
    entry_email.place(x=50, y=130)
    entry_email.insert(0,'teste@gmail.com')

    label_text2 = Label(janela, text='Texto:', font='arial 14 bold', bg=BACKGROUND, fg='white')
    label_text2.place(x=50,y=190)
    text_send = Text(janela, width=65, height=7, font='arial 13')
    text_send.place(x=50, y=220)

    btn_enviar = Button(janela, text='ENVIAR',command=enviar_email, font='arial 15 bold', bg='green', fg='white', width=15, height=1)
    btn_enviar.place(x=250, y=380)

    janela.mainloop()




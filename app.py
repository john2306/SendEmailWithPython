from CoreMail import CoreMailClient
from jinja2 import Template

cm_client = CoreMailClient(
    smtp_server="smtp.gmail.com",
    port= 587,
    sender_email= "backtesty.world@gmail.com",
    password= "vortnhsngttsamgm",
    receiver_email=["johnmendozauni@gmail.com"],
    subject="Subject Test Python Email",
    message=Template(open("email_template.html").read())\
        .render(name="John Coder Py", message="Hello World"),
    from_name="John Coder Py | From"
)
cm_client.send_email()  # Send email without attachments

# Sirve para enviar correos con archivos adjuntos
#cm_client.send_email(*("asistencia.xlsx", "contrato.docx",\
#                       "data.rar", "fotiko.jpeg", "music.mp3",\
#                        "tecnologia.MP4", "templates.zip")) # Send email without attachments
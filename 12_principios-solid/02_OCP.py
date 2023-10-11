"""
Principio OCP => principio de abierto/cerrado

Este principio nos indica que las estructuras de software (clases, módulos, funciones), tienen que estar abiertas para
la extensión pero cerradas para la modificación

En resumen deberiamos poder agregar nuevas funcionalidades sin tener que cambiar el código fuente de una clase (o de las
entidades como tal)
"""

class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}")

class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")



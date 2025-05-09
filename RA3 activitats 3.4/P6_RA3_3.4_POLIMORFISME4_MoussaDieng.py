class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print("Email:", missatge)

class SMS(Missatger):
    def enviar(self, missatge):
        print("SMS:", missatge)

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print("WhatsApp:", missatge)

def enviar_missatges(missatgers, missatge):
    for m in missatgers:
        m.enviar(missatge)

enviar_missatges([Email(), SMS(), WhatsApp()], "Hola!")
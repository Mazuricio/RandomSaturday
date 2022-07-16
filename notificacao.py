import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def notificar(texto):
    Notify.init("Random Saturday!")
    notifica = Notify.Notification.new("Random Saturday", "%s" % texto)
    notifica.show()
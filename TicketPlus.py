from inventario import InventarioStub
from UserDummy import UsuarioDummy
from FakeRepository import RepositorioFake
from EmailDummy import EmailDummy
from StockSpy import InventarioSpy
from unittest.mock import Mock

email_mock = Mock()
class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True

inventario_spy = InventarioSpy()

   
service = TicketService(
   inventario_spy,   
   #None,
   #InventarioStub(),
   #None,
   #UsuarioDummy(),
   RepositorioFake(),
   #None
   #EmailDummy()
   email_mock
)
service.comprar(UsuarioDummy(),2)
email_mock.enviar_confirmacion.assert_called_once()

print(inventario_spy.veces_consultado)
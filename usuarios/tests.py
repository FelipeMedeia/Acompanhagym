import datetime
from django.test import TestCase, Client
from django.contrib.auth.models import User

from usuarios.models import Clientes


# Create your tests here.

class TestUsuarios(TestCase):
    c = Client()

    def setUp(self):
        self.client = Client()

    def test_cadastro_usuario(self):
        c = Client()
        response = c.post("/cadastro/", {"nome": "Teste", "email": "teste@teste.com", "senha": "1234"}, follow=True)
        response.status_code

    def test_se_porta_200(self):
        c = Client()
        response = self.c.get('/cadastro/')
        response.content
        self.assertEqual(response.status_code, 200)

    def test_cadastro_se_ja_existe_nome_igual(self):
        c = Client()
        response = c.get('/cadastro/',
                         {'nome': 'Teste', 'email': 'teste@teste.com', 'senha': '1234'}, follow=True)
        response.redirect_chain
        self.assertEqual(response.status_code, 200)

    def Test_cadastro_usuario_nome(self):
        c = Client()
        response = c.views.cadastro.post({'nome': 'Teste', 'email': 'teste@teste.com', 'senha': '1234'})
        response.content
        self.assertEqual(response, {'nome': 'Teste', 'email': 'teste@teste.com', 'senha': '1234'})


class TestClientes(TestCase):

    def setUp(self):
        User.objects.create_user(username='AdminTest', password='123456', id=1)
        Clientes.objects.create(
            nome='Teste', email='teste@teste.com', endereco='Rua 123',
            data_nascimento='2000-10-10',
            peso=50, altura=169, user_id=1
        )

    def test_cadastro_cliente_nome(self):
        cl = Clientes.objects.get(nome='Teste')
        self.assertEquals(cl.__str__(), 'Teste')

    def test_cadastro_cliente_nome_invalido(self):
        cl = Clientes.objects.get(nome='Teste')
        self.assertNotEqual(cl.nome, 'Testar')

    def test_cadastro_cliente_email(self):
        cl = Clientes.objects.get(email='teste@teste.com')
        self.assertEquals(cl.email, 'teste@teste.com')

    def test_cadastro_cliente_email_invalido(self):
        cl = Clientes.objects.get(email='teste@teste.com')
        self.assertNotEqual(cl.email, 'teste@este.com')

    def test_cadastro_cliente_endereco(self):
        cl = Clientes.objects.get(endereco='Rua 123')
        self.assertEquals(cl.endereco, 'Rua 123')

    def test_cadastro_cliente_endereco_invalido(self):
        cl = Clientes.objects.get(endereco='Rua 123')
        self.assertNotEqual(cl.endereco, 'Rua')

    def test_cadastro_cliente_data_nascimento(self):
        cl = Clientes.objects.get(data_nascimento='2000-10-10')
        self.assertEqual(cl.data_nascimento, datetime.date(2000, 10, 10))

    def test_cadastro_cliente_data_nascimento_invalido(self):
        cl = Clientes.objects.get(data_nascimento='2000-10-10')
        self.assertNotEqual(cl.data_nascimento, datetime.date(2000, 11, 20))

    def test_cadastro_cliente_peso(self):
        cl = Clientes.objects.get(peso=50)
        self.assertEquals(cl.peso, 50)

    def test_cadastro_cliente_peso_invalido(self):
        cl = Clientes.objects.get(peso=50)
        self.assertNotEqual(cl.peso, 40)

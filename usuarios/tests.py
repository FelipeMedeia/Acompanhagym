from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse



# Create your tests here.
class Test_usuarios(TestCase):
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


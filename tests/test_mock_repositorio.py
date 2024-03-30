import pytest
from unittest.mock import Mock


@pytest.fixture
def posts():
    posts = [{'userId': 1, 'Id': 1, 'title': 'Titulo teste 1',
              'body': 'Conteudo do blog 1'},
             {'userId': 2, 'Id': 2, 'title': 'Titulo teste 2',
              'body': 'Teste de conteudo do blog 2'}]
    return posts


@pytest.fixture
def post_by_user_id():
    post = [{'userId': 2, 'Id': 2, 'title': 'Titilo teste 2',
             'body': 'Teste de conteudo do blog 2'}]
    return post


def test_buscar_blog(posts):
    blog = Mock()
    blog.posts.return_value = posts
    resultado = blog
    assert resultado is not None


def test_buscar_pelo_id(post_by_user_id):
    blogRepositorio = Mock()
    blogRepositorio.obter_blog_pelo_id.return_value = post_by_user_id
    resultado = blogRepositorio.obter_blog_pelo_id(2)
    assert resultado is not None

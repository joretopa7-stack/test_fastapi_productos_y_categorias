"""Casos del Módulo IV: 4 positivos, 4 negativos y 2 de frontera."""


# =========================
# Casos positivos (4)
# =========================


def test_cp001_create_product_valid(client):
    """CP001 - Crear producto correctamente."""
    payload = {
        "name": "Mouse Gamer",
        "category": "Laptops",
        "price": 120.00,
        "stock": 5,
        "available": True,
    }
    response = client.post("/products", json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Mouse Gamer"
    assert "id" in response.json()


def test_cp002_list_products(client):
    """CP002 - Consultar la lista de productos."""
    response = client.get("/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 5


def test_cp003_get_existing_product(client):
    """CP003 - Consultar un producto existente por ID."""
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_cp004_create_category_valid(client):
    """CP004 - Crear una categoría válida."""
    payload = {
        "name": "Tablets",
        "description": "Dispositivos táctiles",
        "active": True,
    }
    response = client.post("/categories", json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Tablets"
    assert "id" in response.json()


# =========================
# Casos negativos (4)
# =========================


def test_cp005_get_non_existing_product(client):
    """CP005 - Rechazar consulta de producto inexistente."""
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_cp006_get_non_existing_category(client):
    """CP006 - Rechazar consulta de categoría inexistente."""
    response = client.get("/categories/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found"}


def test_cp007_reject_category_name_too_short(client):
    """CP007 - Rechazar categoría con nombre inválido."""
    response = client.post("/categories", json={"name": "AB"})

    assert response.status_code == 422


def test_cp008_reject_non_numeric_category_id(client):
    """CP008 - Rechazar ID de categoría no numérico."""
    response = client.get("/categories/abc")

    assert response.status_code == 422


# =========================
# Casos de frontera (2)
# =========================


def test_cp009_accept_product_with_zero_stock(client):
    """CP009 - Aceptar stock igual al límite inferior permitido."""
    payload = {
        "name": "Producto sin existencias",
        "category": "Laptops",
        "price": 10.00,
        "stock": 0,
        "available": False,
    }
    response = client.post("/products", json=payload)

    assert response.status_code == 201
    assert response.json()["stock"] == 0


def test_cp010_reject_product_with_negative_stock(client):
    """CP010 - Rechazar stock justo debajo del límite permitido."""
    payload = {
        "name": "Producto inválido",
        "category": "Laptops",
        "price": 10.00,
        "stock": -1,
        "available": False,
    }
    response = client.post("/products", json=payload)

    assert response.status_code == 422

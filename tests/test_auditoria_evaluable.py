"""Automatización trazable del mini-proyecto evaluable.

Se conservan los IDs de casos de docs/casos-prueba.md.
"""


# Categorías: etapa guiada

def test_cp_cat_01_create_category_valid(client):
    response = client.post("/categories", json={"name": "Perifericos"})
    assert response.status_code == 201


def test_cp_cat_02_list_categories(client):
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_cp_cat_03_get_existing_category(client):
    response = client.get("/categories/1")
    assert response.status_code == 200


def test_cp_cat_04_get_unknown_category_404(client):
    response = client.get("/categories/99999")
    assert response.status_code == 404


def test_cp_cat_05_category_name_too_short(client):
    response = client.post("/categories", json={"name": "AB"})
    assert response.status_code == 422


def test_cp_cat_06_category_name_exactly_three_characters(client):
    response = client.post("/categories", json={"name": "ABC"})
    assert response.status_code == 201


def test_cp_cat_07_duplicate_category_observed_behavior(client):
    client.post("/categories", json={"name": "Audio"})
    response = client.post("/categories", json={"name": "audio"})
    # El contrato evaluable exige 409 para duplicados sin distinguir mayúsculas.
    assert response.status_code == 409


# Productos: etapa evaluable

def test_cp_prod_01_create_product_valid(client):
    response = client.post("/products", json={
        "name": "Mouse inalambrico", "category": "Perifericos",
        "price": 120000, "stock": 5, "available": True,
    })
    assert response.status_code == 201


def test_cp_prod_02_list_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_cp_prod_03_get_existing_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200


def test_cp_prod_04_get_unknown_product_404(client):
    response = client.get("/products/99999")
    assert response.status_code == 404


def test_cp_prod_05_update_product_valid(client):
    response = client.put("/products/1", json={"price": 250000})
    assert response.status_code == 200


def test_cp_prod_07_delete_product_valid(client):
    created = client.post("/products", json={
        "name": "Temporal", "category": "Perifericos",
        "price": 1, "stock": 1, "available": True,
    }).json()
    response = client.delete(f"/products/{created['id']}")
    assert response.status_code == 204


def test_cp_prod_09_product_name_too_short(client):
    response = client.post("/products", json={
        "name": "AB", "category": "Perifericos",
        "price": 10, "stock": 1,
    })
    assert response.status_code == 422


def test_cp_prod_10_product_name_exactly_three_characters(client):
    response = client.post("/products", json={
        "name": "ABC", "category": "Perifericos",
        "price": 10, "stock": 1,
    })
    assert response.status_code == 201


def test_cp_prod_14_stock_zero_is_accepted(client):
    response = client.post("/products", json={
        "name": "Monitor", "category": "Perifericos",
        "price": 850000, "stock": 0,
    })
    assert response.status_code == 201


def test_cp_prod_15_negative_stock_is_rejected(client):
    response = client.post("/products", json={
        "name": "Monitor", "category": "Perifericos",
        "price": 850000, "stock": -1,
    })
    assert response.status_code == 422

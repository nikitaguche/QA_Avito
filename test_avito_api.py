import pytest
import requests
import random
import uuid

BASE_URL = "https://qa-internship.avito.com"

@pytest.fixture
def sample_ad_data():
    return {
        "sellerID": random.randint(111111, 999999),
        "name": f"Test Ad {random.randint(1, 100)}",
        "price": random.randint(100, 10000),
        "statistics": {
            "likes": 0,
            "viewCount": 0,
            "contacts": 0
        }
    }

@pytest.fixture
def created_ad(sample_ad_data):
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=sample_ad_data
    )
    assert response.status_code == 200
    status_msg = response.json().get("status", "")
    ad_uuid = status_msg.split(" - ")[-1] if " - " in status_msg else None
    assert ad_uuid and uuid.UUID(ad_uuid)
    return ad_uuid

def test_create_ad_success(sample_ad_data):
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=sample_ad_data
    )
    assert response.status_code == 200
    assert "status" in response.json()

def test_create_ad_missing_price():
    data = {"sellerID": 123456, "name": "Invalid Ad"}
    response = requests.post(f"{BASE_URL}/api/1/item", json=data)
    assert response.status_code == 200

def test_get_ad_by_id(created_ad):
    response = requests.get(f"{BASE_URL}/api/1/item/{created_ad}")
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0
    assert response_data[0]["id"] == created_ad

def test_get_ad_invalid_id():
    response = requests.get(f"{BASE_URL}/api/1/item/invalid_id123")
    assert response.status_code == 400

def test_get_seller_ads(sample_ad_data):
    response = requests.get(f"{BASE_URL}/api/1/{sample_ad_data['sellerID']}/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_nonexistent_seller():
    response = requests.get(f"{BASE_URL}/api/1/999999999/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_ad(created_ad):
    response = requests.delete(f"{BASE_URL}/api/2/item/{created_ad}")
    assert response.status_code == 200

def test_double_delete(created_ad):
    requests.delete(f"{BASE_URL}/api/2/item/{created_ad}")
    response = requests.delete(f"{BASE_URL}/api/2/item/{created_ad}")
    assert response.status_code in [200, 404]

def test_api_versions_interaction(sample_ad_data):
    create_res = requests.post(f"{BASE_URL}/api/1/item", json=sample_ad_data)
    assert create_res.status_code == 200
    ad_uuid = create_res.json()["status"].split(" - ")[-1]
    del_res = requests.delete(f"{BASE_URL}/api/2/item/{ad_uuid}")
    assert del_res.status_code == 200
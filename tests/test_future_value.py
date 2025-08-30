def test_future_value(client):
    payload = {"P": 10000, "R": 0.040753, "N": 4, "T": 10}
    response = client.post("/future-value", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Future Value of 15000 when starting with 10000 compounded at 0.040753 interest rate, 4 times per year over 10 years"}
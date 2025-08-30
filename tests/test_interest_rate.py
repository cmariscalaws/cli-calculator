def test_required_rate(client):
    payload = {"FV": 15000, "P": 10000, "N": 4, "T": 10}
    response = client.post("/required-rate", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "4.08% is the required interest rate to grow $10000 to $15000 if compounding 4 times per year over 10 years."}
def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Tennis Club"
    email = "testuser@example.com"

    # Ensure not already signed up
    resp = client.get("/activities")
    assert resp.status_code == 200
    participants = resp.json()[activity]["participants"]
    assert email not in participants

    # Act: signup (email passed as query param)
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert signup response
    assert resp.status_code == 200
    assert f"Signed up {email} for {activity}" in resp.json().get("message", "")

    # Verify participant added
    resp = client.get("/activities")
    assert email in resp.json()[activity]["participants"]

    # Act: unregister
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})
    # Assert unregister response
    assert resp.status_code == 200
    assert f"Unregistered {email} from {activity}" in resp.json().get("message", "")

    # Verify participant removed
    resp = client.get("/activities")
    assert email not in resp.json()[activity]["participants"]

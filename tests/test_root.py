def test_root_redirect(client):
    # Arrange: client fixture provided
    # Act - TestClient follows redirects, so final response should be the static page
    response = client.get("/")
    # Assert - final URL should be the static index page
    assert response.status_code == 200
    assert str(response.url).endswith("/static/index.html")

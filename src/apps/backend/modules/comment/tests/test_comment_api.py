def test_create_comment(client):
    account_id = "test_account"
    task_id = "test_task"

    response = client.post(
        f"/accounts/{account_id}/tasks/{task_id}/comments",
        json={
            "title": "Test Comment",
            "description": "This is a test comment",
        },
    )

    assert response.status_code == 201

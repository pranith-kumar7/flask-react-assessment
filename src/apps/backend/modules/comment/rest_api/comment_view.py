from dataclasses import asdict

from flask import jsonify, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView

from modules.authentication.rest_api.access_auth_middleware import access_auth_middleware
from modules.comment.errors import CommentBadRequestError
from modules.comment.comment_service import CommentService
from modules.comment.types import (
    CreateCommentParams,
    UpdateCommentParams,
    DeleteCommentParams,
)


class CommentView(MethodView):
    @access_auth_middleware
    def post(self, account_id: str, task_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        if request_data is None:
            raise CommentBadRequestError("Request body is required")

        if not request_data.get("title"):
            raise CommentBadRequestError("Title is required")

        if not request_data.get("description"):
            raise CommentBadRequestError("Description is required")

        create_comment_params = CreateCommentParams(
            account_id=account_id,
            task_id=task_id,
            title=request_data["title"],
            description=request_data["description"],
        )

        created_comment = CommentService.create_comment(
            task_id=task_id,
            params=create_comment_params,
        )

        comment_dict = asdict(created_comment)
        return jsonify(comment_dict), 201

    @access_auth_middleware
    def patch(self, account_id: str, comment_id: str) -> ResponseReturnValue:
        request_data = request.get_json()

        if request_data is None:
            raise CommentBadRequestError("Request body is required")

        if not request_data.get("title"):
            raise CommentBadRequestError("Title is required")

        if not request_data.get("description"):
            raise CommentBadRequestError("Description is required")

        update_comment_params = UpdateCommentParams(
            account_id=account_id,
            comment_id=comment_id,
            title=request_data["title"],
            description=request_data["description"],
        )

        updated_comment = CommentService.update_comment(params=update_comment_params)
        comment_dict = asdict(updated_comment)

        return jsonify(comment_dict), 200

    @access_auth_middleware
    def delete(self, account_id: str, comment_id: str) -> ResponseReturnValue:
        delete_params = DeleteCommentParams(
            account_id=account_id,
            comment_id=comment_id,
        )

        CommentService.delete_comment(params=delete_params)
        return "", 204

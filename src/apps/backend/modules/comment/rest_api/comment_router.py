from flask import Blueprint

from modules.comment.rest_api.comment_view import CommentView


class CommentRouter:
    @staticmethod
    def create_route(*, blueprint: Blueprint) -> Blueprint:
        comment_view = CommentView.as_view("comment_view")

        # Create a comment for a task
        blueprint.add_url_rule(
            "/accounts/<account_id>/tasks/<task_id>/comments",
            view_func=comment_view,
            methods=["POST"],
        )

        # Update a comment
        blueprint.add_url_rule(
            "/accounts/<account_id>/comments/<comment_id>",
            view_func=comment_view,
            methods=["PATCH"],
        )

        # Delete a comment
        blueprint.add_url_rule(
            "/accounts/<account_id>/comments/<comment_id>",
            view_func=comment_view,
            methods=["DELETE"],
        )

        return blueprint

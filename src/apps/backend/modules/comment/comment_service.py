from modules.application.common.types import PaginationResult
from modules.task.internal.task_reader import TaskReader
from modules.task.internal.task_writer import TaskWriter
from modules.comment.types import (
    CreateCommentParams,
    UpdateCommentParams,
    DeleteCommentParams,
    Comment,
    CommentDeletionResult,
)

class CommentService:
    @staticmethod
    def create_comment(*,task_id:str, params: CreateCommentParams) -> Comment:
        return TaskWriter.create_comment(task_id=task_id,params=params)

    @staticmethod
    def update_comment(*, params: UpdateCommentParams) -> Comment:
        return TaskWriter.update_comment(params=params)

    @staticmethod
    def delete_comment(*, params: DeleteCommentParams) -> CommentDeletionResult:
        return TaskWriter.delete_comment(params=params)

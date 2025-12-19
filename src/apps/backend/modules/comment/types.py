from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from modules.application.common.types import PaginationParams, PaginationResult, SortParams


@dataclass(frozen=True)
class Comment:
    id: str
    task_id:str
    account_id: str
    description: str
    title: str


@dataclass(frozen=True)
class GetCommentParams:
    account_id: str
    comment_id: str


@dataclass(frozen=True)
class GetPaginatedCommentsParams:
    account_id: str
    pagination_params: PaginationParams
    sort_params: Optional[SortParams] = None


@dataclass(frozen=True)
class CreateCommentParams:
    account_id: str
    task_id:str
    description: str
    title: str


@dataclass(frozen=True)
class UpdateCommentParams:
    account_id: str
    comment_id: str
    task_id:str
    description: str
    title: str


@dataclass(frozen=True)
class DeleteCommentParams:
    account_id: str
    comment_id: str


@dataclass(frozen=True)
class CommentDeletionResult:
    comment_id: str
    deleted_at: datetime
    success: bool

class CommentErrorCode:
    NOT_FOUND: str = "Comment_ERR_01"
    BAD_REQUEST: str = "Comment_ERR_02"

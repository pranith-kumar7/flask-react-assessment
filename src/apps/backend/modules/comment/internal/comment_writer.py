class CommentWriter:
    @staticmethod
    def create_comment(*, task_id: str, params: CreateCommentParams) -> Comment:
        comment_bson = commentModel(
            task_id=task_id,
            account_id=params.account_id,
            description=params.description,
            title=params.title,
        ).to_bson()

        query = commentRepository.collection().insert_one(comment_bson)
        created_comment_bson = commentRepository.collection().find_one({"_id": query.inserted_id})

        return commentUtil.convert_comment_bson_to_comment(created_comment_bson)

    @staticmethod
    def update_comment(*, params: UpdateCommentParams) -> Comment:
        updated_comment_bson = commentRepository.collection().find_one_and_update(
            {"_id": ObjectId(params.comment_id), "account_id": params.account_id, "active": True},
            {"$set": {"description": params.description, "title": params.title, "updated_at": datetime.now()}},
            return_document=ReturnDocument.AFTER,
        )

        if updated_comment_bson is None:
            raise commentNotFoundError(comment_id=params.comment_id)

        return commentUtil.convert_comment_bson_to_comment(updated_comment_bson)

    @staticmethod
    def delete_comment(*, params: DeleteCommentParams) -> CommentDeletionResult:
        comment = commentReader.get_comment(
            params=GetCommentParams(account_id=params.account_id, comment_id=params.comment_id)
        )

        deletion_time = datetime.now()
        updated_comment_bson = commentRepository.collection().find_one_and_update(
            {"_id": ObjectId(comment.id)},
            {"$set": {"active": False, "updated_at": deletion_time}},
            return_document=ReturnDocument.AFTER,
        )

        if updated_comment_bson is None:
            raise commentNotFoundError(comment_id=params.comment_id)

        return CommentDeletionResult(
            comment_id=params.comment_id,
            deleted_at=deletion_time,
            success=True,
        )

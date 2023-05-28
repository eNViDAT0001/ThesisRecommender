import IO.comment_request as CommentReq



def UpdateComment(comment: CommentReq.Req):
    return {'message': 'update successful', 'error': None}
def CreateComment(comment: CommentReq.Req):
    return {'message': 'create successful', 'error': None}
def DeleteComment(comment: CommentReq.DeleteReq):
    return {'message': 'delete successful', 'error': None}
def ListProductRecommendedIDsByUserID(userID: int):
    return [1, 2, 3, 4, 5]
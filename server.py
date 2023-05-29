import pandas as pd
import grpc
from concurrent import futures
from sklearn.metrics.pairwise import cosine_similarity
import recommender_pb2_grpc as pb2_grpc
import recommender_pb2 as pb2

df = pd.read_csv('Data/comment.csv')

class RecommenderService(pb2_grpc.RecommenderBaseCommentServicer):

    def AddComment(self, request, context):
        return pb2.NonQueryResponse({'message': 'create successful'})

    def UpdateComment(self, request, context):
        return pb2.NonQueryResponse({'message': 'update successful'})

    def DeleteComment(self, request, context):
        return pb2.NonQueryResponse({'message': 'delete successful'})
        
    def LisRecommendedProductIDsByUserID(self, request, context):
        return pb2.RecommentRes({'product_id': [1, 2, 3, 4, 5]})

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_RecommenderBaseCommentServicer_to_server(RecommenderService(), server)
    server.add_insecure_port('[::]:9180')
    server.start()
    print("Server started on port 9180...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
import pandas as pd
import grpc
import csv
from concurrent import futures
from recommendation import RecommendProducts
import recommender_pb2_grpc as pb2_grpc
import recommender_pb2 as pb2

df = pd.read_csv('Data/comment.csv')

class RecommenderService(pb2_grpc.RecommenderBaseCommentServicer):

    def AddComment(self, request, context):
        with open('./Data/comment.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([request.user_id, request.product_id, request.rating])
        return pb2.NonQueryResponse(message="Dummy Message")
        
    def LisRecommendedProductIDsByUserID(self, request, context):
        result = RecommendProducts(request.user_id)
        return pb2.RecommendRes(product_id=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_RecommenderBaseCommentServicer_to_server(RecommenderService(), server)
    server.add_insecure_port('[::]:9180')
    server.start()
    print("Server started on port 9180...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    
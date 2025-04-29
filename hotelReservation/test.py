import requests
import random
import time


def reviews():
    url = "http://localhost:5000/review"
    payload = {"hotelId":"2", "username": "Cornell_0", "password": "0000000000"}
    t_before = time.time()
    r = requests.get(url, params=payload)
    t_after = time.time()
    t = t_after - t_before
    print(r.text)
    print("review=",t)

reviews()

#rpc tests for the knative service
''' 

# plain ip for the pod
grpcurl -plaintext -import-path ./benchmarks/DeathStarBench/hotelReservation/ -proto services/user/proto/user.proto   -d '{ "username": "Cornell_0", "password": "0000000000"}'   192.168.127.87:8086   user.User.CheckUser


# IP of the  for the istio external ip
grpcurl -plaintext   -import-path ./benchmarks/DeathStarBench/hotelReservation/   -proto services/user/proto/user.proto   -d '{ "username": "Cornell_0", "password": "0000000000"}'   \
    -H "Host: srv-user.default.172.10.10.0.sslip.io"   \
    172.10.10.2:80   \
    user.User.CheckUser


# IP of the  for the istio cluster/internal ip
grpcurl -plaintext   -import-path ./benchmarks/DeathStarBench/hotelReservation/   -proto services/user/proto/user.proto   -d '{ "username": "Cornell_0", "password": "0000000000"}'   \
    -H "Host: srv-user.default.10.103.12.215.sslip.io"   \
    10.103.12.215:80   \
    user.User.CheckUser


grpcurl -plaintext  -vv -import-path . \
    -proto services/user/proto/user.proto   -d '{ "username": "Cornell_0", "password": "0000000000"}' \
    srv-user.default.10.103.165.197.sslip.io:80 \
    user.User.CheckUser 

grpcurl -plaintext  -vv -import-path . \
    -proto services/user/proto/user.proto   -d '{ "username": "Cornell_0", "password": "0000000000"}' \
    srv-user:80 \
    user.User.CheckUser 


'''
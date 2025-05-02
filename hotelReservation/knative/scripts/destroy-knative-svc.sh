#!/bin/bash


cd $(dirname $0)/..

for i in *.yaml
do
  kubectl delete -f ${i}  &
done
wait
sleep 30

kubectl delete -f svc/  &

echo "Finishing in 30 seconds"
sleep 30

kubectl get pods

cd - >/dev/null

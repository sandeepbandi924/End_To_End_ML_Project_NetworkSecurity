import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE='SANDEEPAI'
    collection='NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)










#      - name: Build, tag, and push image to Amazon ECR
#         id: build-image
#         env:
#           ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
#           ECR_REPOSITORY: ${{ secrets.ECR_REPOSITORY_NAME }}
#           IMAGE_TAG: latest
#         run: |
#           # Build a docker container and
#           # push it to ECR so that it can
#           # be deployed to ECS.
#           docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
#           docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
#           echo "::set-output name=image::$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"

#   Continuous-Deployment:
#     needs: build-and-push-ecr-image
#     runs-on: self-hosted
#     steps:
#       - name: Checkout
#         uses: actions/checkout@v3

#       - name: Configure AWS credentials
#         uses: aws-actions/configure-aws-credentials@v1
#         with:
#           aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
#           aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
#           aws-region: ${{ secrets.AWS_REGION }}

#       - name: Login to Amazon ECR
#         id: login-ecr
#         uses: aws-actions/amazon-ecr-login@v1
      
      
#       - name: Pull latest images
#         run: |
#          docker pull ${{secrets.AWS_ECR_LOGIN_URI}}/${{ secrets.ECR_REPOSITORY_NAME }}:latest
         
#       #- name: Stop and remove  container if running
#        # run: |
#         # docker ps -q --filter "name=networksecurity" | grep -q . && docker stop networksecurity && docker rm -fv networksecurity
       
#       - name: Run Docker Image to serve users
#         run: |
#          docker run -d -p 8080:8080 --ipc="host" --name=networksecurity -e 'AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }}' -e 'AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }}' -e 'AWS_REGION=${{ secrets.AWS_REGION }}'  ${{secrets.AWS_ECR_LOGIN_URI}}/${{ secrets.ECR_REPOSITORY_NAME }}:latest
#       - name: Clean previous images and containers
#         run: |
#          docker system prune -f
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
import sys


if __name__ == '__main__':
    try:
        trainingpipeline = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipeline)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info('Initiate the data ingestion')
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info('Data initiation Completed')
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipeline)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info('Initiate the data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info('Data validation Completed')
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
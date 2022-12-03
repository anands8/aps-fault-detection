from sensor.entity import artifact_entity, config_entity
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd


class DataValidation:

    def __init__(self,data_validation_config):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e,sys)

    def is_required_columns_exists(self,)->bool:
        pass

    def drop_missing_values_columns(self,df:pd.DataFrame,threshold:float=0.3)->pd.DataFrame:
        """
        Description: This function will drop columns containing misssing values more than specified threshold
        =========================================================
        Params:
        df: a pandas DataFrame
        threshold: percentage criteria to drop a column
        =========================================================
        return Pandas dataframe if atleast a single column is available sfter missing values are dropped
        """
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)


    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass
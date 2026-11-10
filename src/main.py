import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from extract import extract_users_from_api
from transform import clean_and_enrich_data
from load import load_to_parquet

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s'
)

def run_pipeline():
    logger = logging.getLogger("ETL_Orchestrator")
    logger.info("🚀 Démarrage du pipeline ETL...")
    
    API_URL = "https://jsonplaceholder.typicode.com/users"
    OUTPUT_PATH = "data/cleaned_users.parquet"
    
    try:
        raw_df = extract_users_from_api(API_URL)
        clean_df = clean_and_enrich_data(raw_df)
        load_to_parquet(clean_df, OUTPUT_PATH)
    except Exception as e:
        logger.error(f"💥 Échec du pipeline : {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()
  

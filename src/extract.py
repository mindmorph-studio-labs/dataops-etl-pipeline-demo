import requests
import logging
import pandas as pd
from typing import List, Dict

logger = logging.getLogger(__name__)

def extract_users_from_api(api_url: str) -> pd.DataFrame:
    """Extrait les données depuis une API REST publique."""
    logger.info(f"📥 Extraction depuis {api_url}")
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        df = pd.DataFrame(response.json())
        logger.info(f"✅ {len(df)} lignes extraites.")
        return df
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Erreur API : {e}")
        raise

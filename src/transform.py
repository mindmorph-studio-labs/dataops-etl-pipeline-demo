import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_and_enrich_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et enrichit les données."""
    logger.info("🔄 Transformation en cours...")
    initial_count = len(df)
    df = df.drop_duplicates()
    
    if 'name' in df.columns:
        df['name'] = df['name'].str.strip().str.title()
    if 'email' in df.columns:
        df['email'] = df['email'].str.lower().str.strip()
        df['email_domain'] = df['email'].apply(lambda x: x.split('@')[-1] if '@' in str(x) else 'unknown')
        
    logger.info(f"✅ {initial_count - len(df)} doublons supprimés.")
    return df
  

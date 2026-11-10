import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_to_parquet(df: pd.DataFrame, output_path: str) -> None:
    """Sauvegarde les données au format Parquet optimisé."""
    logger.info(f"📤 Chargement vers {output_path}")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, engine='pyarrow', compression='snappy', index=False)
    logger.info("🚀 Pipeline terminé.")
  

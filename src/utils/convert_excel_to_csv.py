import pandas as pd
import dask.dataframe as dd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def convert_excel_to_dask(xlsx_path: str, csv_path: str):
    """
    Excel 파일을 CSV로 변환하고, 변환된 CSV를 Dask DataFrame으로 로드하는 함수
    """
    try:
        # CSV 변환 수행
        
        logger.info(f"!엑셀 파일을 CSV로 변환 중: {xlsx_path} → {csv_path}")
        df_excel = pd.read_excel(xlsx_path)
        df_excel.to_csv(csv_path, index=False, encoding="ISO-8859-1")
        logger.info(f"!CSV 변환 완료: {csv_path}")

        # Dask로 CSV 로드
        logger.info(f"!Dask로 CSV 로딩 중: {csv_path}")
        df = dd.read_csv(
            csv_path,
            encoding="ISO-8859-1",
            on_bad_lines="skip",
            blocksize="16MB",
            assume_missing=True,
            dtype={"InvoiceNo": "object"}
        )
        return df

    except Exception as e:
        logger.error(f"!Excel to Dask 변환 중 오류 발생: {e}")
        raise
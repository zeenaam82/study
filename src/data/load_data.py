import os
import dask.dataframe as dd
from src.utils.convert_excel_to_csv import convert_excel_to_dask
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_dataset(file_path):
    """
    고객 데이터를 Dask DataFrame으로 로드하는 함수.
    CSV가 없고 XLSX가 존재하면 자동 변환 후 로드.
    """
    try:
        xlsx_file = file_path.replace(".csv", ".xlsx")

        if os.path.exists(file_path):
            logger.info(f"CSV 파일 '{file_path}' 로드 중...")
            df = dd.read_csv(
                file_path,
                encoding="ISO-8859-1",
                on_bad_lines="skip",
                blocksize="16MB",
                assume_missing=True,
                dtype={"InvoiceNo": "object"}
            )
            return df

        elif os.path.exists(xlsx_file):
            logger.info(f"CSV 파일이 없어 XLSX 파일 '{xlsx_file}'을 변환 중...")
            df = convert_excel_to_dask(xlsx_file, file_path)
            return df

        else:
            logger.error(f"'{file_path}' 또는 '{xlsx_file}' 파일이 존재하지 않습니다.")
            raise FileNotFoundError(f"{file_path} 또는 {xlsx_file} 파일이 존재하지 않습니다.")

    except Exception as e:
        logger.error(f"데이터 로드 중 오류 발생: {e}")
        raise
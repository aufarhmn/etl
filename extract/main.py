import os
import time as t


from stock import ExtractStock
from trends import ExtractTrends

def validate_directory() -> None:
    if os.path.exists('../frames'):
        print('directory ensured')
        return
    print('Directory does not exist')
    print('Creating /frames')
    os.mkdir('../frames')


if __name__ == "__main__":
    validate_directory()
    
    start = round(t.time()*1000)
    ExtractStock()
    ExtractTrends()
    end = round(t.time()*1000) - start
    print(f"Ingestion succeed in {end}ms")
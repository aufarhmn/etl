import subprocess
from dotenv import load_dotenv
from ingest_raw.ingest import StartIngest
from pipeline.etl import StartPipeline

if __name__ == '__main__':
    load_dotenv('.env.production')
    StartIngest()
    StartPipeline()
    
    subprocess.call("rm -rf frames", shell=True)
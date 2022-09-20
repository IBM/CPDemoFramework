import logging
import pandas

logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from apis import endpoints, MainAPI, usecases

mainAPI = MainAPI()
governanceArtifactAPI = endpoints.GovArtifactAPI(mainAPI)
governanceArtifactAPI.importArtifactsZIP(sys.argv[1])
print("success")
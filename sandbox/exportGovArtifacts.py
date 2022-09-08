import logging
import pandas

logging.basicConfig(format="%(asctime)s %(levelname)-7s %(message)s", level=logging.INFO)
import sys
sys.path.append('../')
from apis import endpoints, MainAPI, usecases

mainAPI = MainAPI()
governanceArtifactAPI = endpoints.GovArtifactAPI(mainAPI)
governanceArtifactAPI.exportArtifactsZIP(sys.argv[1],"always",sys.argv[2],"all_top_level")
print("success")
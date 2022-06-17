from apis import main
import logging

class SubAPI():
  """Abstract API class that ensures the same MainAPI's can be used for multiple SubAPI's
  """
  def __init__(self, mainAPI=None):
    """Creating a new SubAPI
    Args:
        mainAPI (main.MainAPI, optional): When a MainAPI is available, then it is used. If not, a new MainAPI is created and saved in self.mainAPI. Defaults to None.
    """
    logging.debug('calling SubAPI init')
    logging.debug(mainAPI)
    if mainAPI:
      self.mainAPI = mainAPI
    else:
      self.mainAPI = main.MainAPI()

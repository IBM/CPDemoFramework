"""CSV Processing Functions"""
import logging
import pandas

def items2CSV(add2TableFun, itemsJSON, filePath):
  """creates a csv file from a list of certain WKC API items
  Args:
      add2TableFun (function): function that contains the logic how a API type object should be added to the pandas table.
      itemsJSON (dict): JSON formatted output of the WKC API for a list of certain WKC API type.
      filePath (str): name or filepath for the creation of the csv file
  """
  table = items2Table(add2TableFun, itemsJSON)
  table.to_csv(filePath, index=False)

def items2Table(add2TableFun, itemsJSON):
  """creates a table from a list of certain WKC API items
  Args:
      add2TableFun (function): function that contains the logic how a API type object should be added to the pandas table.
      itemsJSON (dict): JSON formatted output of the WKC API for a list of certain WKC API type.
  Returns:
    pandas.DataFrame: table of certain WKC API items
  """
  table = pandas.DataFrame()
  logging.debug(itemsJSON)
  for itemJSON in itemsJSON:
    table = add2TableFun(table, itemJSON)
  return table

import requests
import json
import collections
import logging


def nested_dict_iter(responseJson, keyToSearch):
   print(keyToSearch)
   for key, value in responseJson.items():
       if (key == keyToSearch):
         if (isinstance(value,dict) or isinstance(value,list)):
           for inner_key, inner_value in nested_dict_iter(value, keyToSearch):
               try:
                  if key is keyToSearch:
                    print(inner_value)
               except Exception:
                   logging.error(Exception)


def key_parser(value,key):
       if (isinstance(value,list)):
           for i in range(len(value)):
               for k,v in value[i].items():
                   if (k == key):
                       return v
       elif (isinstance(value,dict)):
            for k,v in value:
                if k is  key:
                    print(v)
                    return v


def key_value_finder(responsejson,keyToSearch):
   for key,value in responsejson.items():
       if(key == keyToSearch):
           if not (isinstance(value,list) or isinstance(value,dict)):
               return value
           else:
              if(type_find(value)):
                   key_value_finder(value,"outbound")
              else:
                   key_parser(value,"outbound")
           break
       else:
           continue


def type_find(value):
   if(isinstance(value,list)):
       return False
   elif(isinstance(value,dict)):
       return True
   else:
       return None

def key_value_finder_unique(responsejson,keyToSearch):
   for key,value in responsejson.items():
       if  (key == keyToSearch):
           if not (isinstance(value,list) or isinstance(value,dict)):
               print(value)
           elif (type_find(value)):
                   key_value_finder_unique(value, keyToSearch)
           else:
                   key_parser(value, keyToSearch)
       elif (key is not keyToSearch):
           if(type_find(value)):
                   key_value_finder_unique(value,keyToSearch)
           else:
                   key_parser(value,keyToSearch)
   else:
         raise Exception
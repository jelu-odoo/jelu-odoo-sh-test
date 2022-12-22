# from xmlrpc import client
import pandas as pd
import collections

# url = 'https://jelu-odoo-jelu-odoo-sh-test-harvest-right-6728827.dev.odoo.com'
# db = 'jelu-odoo-jelu-odoo-sh-test-harvest-right-6728827'
# username = 'admin'
# password = 'admin'

# common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
# print(common.version())

# uid = common.authenticate(db, username, password, {})
# print(uid)

# models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

# create_lead = models.execute_kw(db, uid, password, 
#                                 'crm.lead', 'create', 
#                                 [
#                                     {
#                                         'name': 'owo',
                                        
#                                     }
#                                 ])

# print(create_lead)

df = pd.read_excel('Leads1.xlsx',sheet_name='Leads1')

lead_mapping = pd.read_csv('harvestright leads master fields mapping.csv', names=[0, 1])

mapping = collections.defaultdict()

for index, row in lead_mapping.iterrows(): 
    
    mapping[row[0]] = row[1]
    
# for k, v in mapping.items(): 
#     print(k, v)
    

    
for index, row in df[0:2].iterrows(): 
    print(row)
    
    
    
#     print(columnName, type(columnData.values), columnData.values)
    
    
    

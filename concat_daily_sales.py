import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', None)
# Uploading sales table
sales=pd.read_excel('/Users/dboldin/Local documents/Jurabek/source tables/sales_to_concat.xlsx',
                    header=None,
                    names=['date', 'client', 'inn', 'clinic',	'promo', 'new_medication',	'group', 'region',	'pcs',	'total',
                            'discount',	'cashback',	'price', 'distributor',	'payment', 'type',	'stock']
                    )
# Formating data. We have to clean string variables such as product names. Trimming them.
sales['date'] = pd.to_datetime(sales['date'], format='%d%m%Y', infer_datetime_format=True, dayfirst=True)
sales['new_medication'] = sales['new_medication'].str.replace('  ', ' ')
sales['new_medication'] = sales['new_medication'].str.strip()
sales['region'] = sales['region'].str.strip()
# Adding supplementary fields
sales['VIP'] = np.where(sales.region=='VIP', True, False)
regions = pd.read_csv('/Users/dboldin/Local documents/Jurabek/source tables/region_mapping.csv',
                        sep=';')
sales = sales.merge(regions, on='region', how='left')
# uploading the current table with all sales data
master_sales = pd.read_excel('/Users/dboldin/Documents/Jurabek/Source/daily_sales.xlsx')
# concat the tables to get the updated info
merged = pd.concat([master_sales, sales])
# Loading it back into the file source for Power BI or else
merged.to_excel('/Users/dboldin/Documents/Jurabek/Source/daily_sales.xlsx', index=False)
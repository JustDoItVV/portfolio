from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import aerospike


spark = SparkSession.builder.master('local[*]').appName('hackaton').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
PATH = '/home/jd/Desktop/hackaton/datasets/'
parquet_file = spark.read.parquet(PATH + 'agg_usage.parquet')
csv_file = spark.read.option('header', 'true').option('inferSchema', 'true').csv(PATH + 'parent_operator.csv')

# data_traffic = spark.read.parquet(PATH + 'data_traffic.parquet')
# voice_traffic = spark.read.parquet(PATH + 'voice_traffic.parquet')
# client_profile = spark.read.parquet(PATH + 'client_profile.parquet')

data_traffic = parquet_file\
    .filter((parquet_file.call_type_key.isin({'G', 'Y', 'X'})) &
            (parquet_file.roaming_type_key.isin({'X', 'R', 'H'})))\
    .groupBy('client_id', 'time_key', 'network_type')\
    .agg(when(col('network_type') == 'L', sum('rounded_data_volume')).alias('data_4g_mb'),
         when(col('network_type') == 'G', sum('rounded_data_volume')).alias('data_3g_mb'),
         sum('rounded_data_volume').alias('data_all_mb'))\
    .groupBy('client_id', 'time_key')\
    .agg(sum('data_4g_mb').alias('data_4g_mb'),
         sum('data_3g_mb').alias('data_3g_mb'),
         sum('data_all_mb').alias('data_all_mb'))\
    .withColumn('time_key',
                regexp_replace(col('time_key'),
                               '.(\d{4})(\d{2})(\d{2})',
                               '$1-$2-$3'))\
    .fillna(0)

parquet_file_enhanced = parquet_file.join(csv_file, csv_file.parent_operator_code == parquet_file.parent_operator_code_b, how='left_outer')

voice_traffic_1 = \
    parquet_file_enhanced\
    .groupBy('client_id',
             'time_key',
             'call_direction_ind',
             'call_type_key',
             'connection_type_key',
             'group_operator_code',
             'location_type_key',
             )\
    .agg(when(col('call_direction_ind') == '1',
              sum('num_of_call'))
         .alias('voice_in_cnt'),
         when(((col('call_type_key') == 'V') &
               (col('call_direction_ind') == '1') &
               (col('connection_type_key') == '3') &
               (col('group_operator_code') == 'BLN')),
              sum('num_of_call'))
         .alias('voice_onnet_in_cnt'),
         when(((col('location_type_key') == '1') &
               (col('call_direction_ind') == '1')),
              sum('num_of_call'))
         .alias('voice_intercity_in_cnt'),
         when(((col('location_type_key') == '3') &
               (col('call_direction_ind') == '1')),
              sum('actual_call_dur_sec'))
         .alias('voice_international_in_sec'),
         when(((col('location_type_key') == '1') &
               (col('call_direction_ind') == '2')),
              sum('actual_call_dur_sec'))
         .alias('voice_intercity_out_sec'),
         when((col('call_direction_ind') == '2'),
              sum('actual_call_dur_sec'))
         .alias('voice_out_sec'),
         when(((col('call_type_key') == 'V') &
               (col('call_direction_ind') == '2') &
               (col('connection_type_key') == '3') &
               (col('group_operator_code') == 'BLN')),
              sum('num_of_call'))
         .alias('voice_onnet_out_cnt'),
         when(((col('location_type_key') == '3') &
               (col('call_direction_ind') == '2')),
              sum('actual_call_dur_sec'))
         .alias('voice_international_out_cnt'),
         when((col('call_direction_ind') == '2'),
              sum('num_of_call'))
         .alias('voice_out_cnt'),
         when(((col('call_type_key') == 'V') &
               (col('call_direction_ind') == '2') &
               (col('connection_type_key') == '3') &
               (col('group_operator_code') == 'BLN')),
              sum('actual_call_dur_sec'))
         .alias('voice_onnet_out_sec'),
         when((col('call_direction_ind') == '1'),
              sum('actual_call_dur_sec'))
         .alias('voice_in_sec'),
         when(((col('call_type_key') == 'V') &
               (col('call_direction_ind') == '1') &
               (col('connection_type_key') == '3') &
               (col('group_operator_code') == 'BLN')),
              sum('actual_call_dur_sec'))
         .alias('voice_onnet_in_sec'),
         when(((col('location_type_key') == '1') &
               (col('call_direction_ind') == '1')),
              sum('actual_call_dur_sec'))
         .alias('voice_intercity_in_sec'),
         when(((col('location_type_key') == '1') &
               (col('call_direction_ind') == '2')),
              sum('num_of_call'))
         .alias('voice_intercity_out_cnt'),
         when(((col('location_type_key') == '3') &
               (col('call_direction_ind') == '1')),
              sum('num_of_call'))
         .alias('voice_international_in_cnt'),
         when(((col('location_type_key') == '3') &
               (col('call_direction_ind') == '2')),
              sum('actual_call_dur_sec'))
         .alias('voice_international_out_sec'))

voice_traffic_2 = \
    parquet_file_enhanced\
    .filter(col('charge_amt_rur') > 0)\
    .groupBy('client_id',
             'time_key',
             'call_direction_ind',
             'call_type_key',
             'connection_type_key',
             'group_operator_code',
             'location_type_key',
             )\
    .agg(when((col('call_direction_ind') == '2'),
              sum('actual_call_dur_sec'))
         .alias('voice_out_nopackage_sec'))

voice_traffic = voice_traffic_1.join(voice_traffic_2,
                                     on=['client_id',
                                         'time_key',
                                         'call_direction_ind',
                                         'call_type_key',
                                         'connection_type_key',
                                         'group_operator_code',
                                         'location_type_key'],
                                     how='left_outer')

voice_traffic = voice_traffic\
    .groupBy('client_id', 'time_key')\
    .agg(sum('voice_in_cnt').alias('voice_in_cnt'),
         sum('voice_onnet_in_cnt').alias('voice_onnet_in_cnt'),
         sum('voice_intercity_in_cnt').alias('voice_intercity_in_cnt'),
         sum('voice_international_in_sec').alias('voice_international_in_sec'),
         sum('voice_intercity_out_sec').alias('voice_intercity_out_sec'),
         sum('voice_out_sec').alias('voice_out_sec'),
         sum('voice_onnet_out_cnt').alias('voice_onnet_out_cnt'),
         sum('voice_international_out_cnt').alias('voice_international_out_cnt'),
         sum('voice_out_cnt').alias('voice_out_cnt'),
         sum('voice_onnet_out_sec').alias('voice_onnet_out_sec'),
         sum('voice_in_sec').alias('voice_in_sec'),
         sum('voice_onnet_in_sec').alias('voice_onnet_in_sec'),
         sum('voice_intercity_in_sec').alias('voice_intercity_in_sec'),
         sum('voice_intercity_out_cnt').alias('voice_intercity_out_cnt'),
         sum('voice_international_in_cnt').alias('voice_international_in_cnt'),
         sum('voice_international_out_sec').alias('voice_international_out_sec'),
         sum('voice_out_nopackage_sec').alias('voice_out_nopackage_sec'),
         )

voice_traffic = voice_traffic\
    .withColumn('time_key',
                regexp_replace(col('time_key'),
                               '.(\d{4})(\d{2})(\d{2})',
                               '$1-$2-$3'))\
    .fillna(0)

client_profile = voice_traffic.join(data_traffic, on=['client_id', 'time_key'], how='left_outer')

client_profile = client_profile\
    .withColumn('time_key',
                substring('time_key', 1, 7))

client_profile = client_profile.groupBy('client_id', 'time_key').sum()

newColumns = ['client_id',
              'time_key',
              'voice_in_cnt',
              'voice_onnet_in_cnt',
              'voice_intercity_in_cnt',
              'voice_international_in_sec',
              'voice_intercity_out_sec',
              'voice_out_sec',
              'voice_onnet_out_cnt',
              'voice_international_out_cnt',
              'voice_out_cnt',
              'voice_onnet_out_sec',
              'voice_in_sec',
              'voice_onnet_in_sec',
              'voice_intercity_in_sec',
              'voice_intercity_out_cnt',
              'voice_international_in_cnt',
              'voice_international_out_sec',
              'voice_out_nopackage_sec',
              'data_4g_mb',
              'data_3g_mb',
              'data_all_mb']
client_profile = client_profile.toDF(*newColumns)

# data_traffic.write.parquet(PATH + 'data_traffic.parquet')
# voice_traffic.write.parquet(PATH + 'voice_traffic.parquet')
# client_profile.write.parquet(PATH + 'client_profile.parquet')







# Configure the client
# config = {
#     'hosts': [ ('127.0.0.1', 3000) ],
#     'policy' : {'key': aerospike.POLICY_KEY_SEND}
# }
#
# client = aerospike.client(config).connect()
#
#
#
#
# # Records are addressable via a tuple of (namespace, set, key)
# try:
#     for i in range(10):
#         # Write the records
#         client.put(('test', 'demo', 'id'+str(people[i]['id'])), people[i])
# except Exception as e:
#     import sys
#     print("error: {0}".format(e), file=sys.stderr)
#
# print('Test data populated.')

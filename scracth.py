import pandas as pd
import numpy as np
from catchment.models import Site
import datetime
# data = pd.DataFrame([[1., 2.2, 3.], [4., 5., 6.]], index=['fp35', 'fp56'])
#
# print(data)
#
# location_measurement = [
#     ("FP", "FP35", "Rainfall"),
#     ("FP", "FP56", "River Level"),
#     ("PL", "PL23", "River Level"),
#     ("PL", "PL23", "Water pH")
# ]
# index_names = ["Catchment", "Site", "Measurement"]
# index = pd.MultiIndex.from_tuples(location_measurement, names=index_names)
# data = [
#     [0., 2., 1.],
#     [30., 29., 34.],
#     [34., 32., 33.],
#     [7.8, 8., 7.9]
# ]
#
# data2 = pd.DataFrame(data,index=index)
# print(data2)
#
# measurement_data = [
#     {
#         'site': 'FP35',
#         'measurement': 'Rainfall',
#         'data': [0., 2., 1.]
#     },
#     {
#         'site': 'FP56',
#         'measurement': 'River level',
#         'data': [30., 29., 34.]
#     }
# ]
#
# print(measurement_data)
#
#
# def attach_sites(data, sites, measurements):
#     output = []
#
#     for i in range(len(data)):
#         output.append({'site':sites[i],
#                        'measurement': measurements[i],
#                        'data': data[i]})
#
#     return output
#
#
# data = np.array([[34., 32., 33.],
#                  [7.8, 8.0, 7.9]])
#
# output = attach_sites(data, ['PL23', 'PL23'], ['River Level', 'pH'])
# print(output)

FP35 = Site('FP35')

print(FP35.name)
print('version of instance', FP35.name)

rainfall_data = pd.Series(
    [0.0, 2.0, 1.0],
    index=[
        datetime.date(2000, 1, 1),
        datetime.date(2000, 1, 2),
        datetime.date(2000, 1, 3)
        ]
    )

waterph_data = pd.Series(
    [7.8, 8.8, 7.9],
    index=[
        datetime.date(2000, 1, 1),
        datetime.date(2000, 1, 2),
        datetime.date(2000, 1, 3)
    ]
)

FP35.add_measurement('Rainfall', rainfall_data, 'mm')
FP35.add_measurement('Water ph', waterph_data)

print(FP35.measurements['Rainfall'].series)

#last_data = FP35.last_measurements
#print(last_data)

# default_site = Site.create_sample_site()
# print(default_site.name)
#
# print(FP35)

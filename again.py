import json
import csv


def flatten_json(data):
    flattened = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '_')
        else:
            flattened[name[:-1]] = x

    flatten(data)
    return flattened


def json_to_csv(json_data, csv_file):
    # Flatten the JSON data
    flattened_data = [flatten_json(item) for item in json_data]

    # Extract all unique keys
    keys = set().union(*(d.keys() for d in flattened_data))

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write the header
        writer.writeheader()

        # Write the data rows
        writer.writerows(flattened_data)

json_data = {
  "defaultProfileConfiguration": {
    "datasetConfiguration": {
      "includedStatistics": [
        "CORRELATION",
        "DUPLICATE_ROWS_COUNT"
      ],
      "parameters": {
        "CORRELATION": {
          "columnNumber": "10"
        }
      }
    },
    "columnConfiguration": {
      "booleanColumn": {
        "includedStatistics": [
          "MOST_COMMON_VALUES",
          "DISTINCT_VALUES_COUNT",
          "UNIQUE_VALUES_COUNT",
          "MISSING_VALUES_COUNT",
          "ENTROPY"
        ],
        "parameters": {
          "MOST_COMMON_VALUES": {
            "sampleSize": "50"
          }
        }
      },
      "stringColumn": {
        "includedStatistics": [
          "MIN",
          "MOST_COMMON_VALUES",
          "DISTINCT_VALUES_COUNT",
          "MAX",
          "MEAN",
          "UNIQUE_VALUES_COUNT",
          "MODE",
          "MISSING_VALUES_COUNT",
          "STANDARD_DEVIATION",
          "ENTROPY",
          "MEDIAN",
          "OUTLIER_DETECTION",
          "VALUE_DISTRIBUTION"
        ],
        "parameters": {
          "MOST_COMMON_VALUES": {
            "sampleSize": "50"
          },
          "OUTLIER_DETECTION": {
            "threshold": "3",
            "sampleSize": "50"
          },
          "VALUE_DISTRIBUTION": {
            "binNumber": "20"
          }
        }
      },
      "numericColumn": {
        "includedStatistics": [
          "MIN",
          "PERCENTILES",
          "ZEROS_COUNT",
          "UNIQUE_VALUES_COUNT",
          "ENTROPY",
          "VALUE_DISTRIBUTION",
          "SKEWNESS",
          "Z_SCORE_DISTRIBUTION",
          "MAX",
          "MISSING_VALUES_COUNT",
          "INTER_QUARTILE_RANGE",
          "MEDIAN_ABSOLUTE_DEVIATION",
          "RANGE",
          "MOST_COMMON_VALUES",
          "DISTINCT_VALUES_COUNT",
          "VARIANCE",
          "MEDIAN",
          "MEAN",
          "MINIMUM_VALUES",
          "MODE",
          "SUM",
          "KURTOSIS",
          "MAXIMUM_VALUES",
          "STANDARD_DEVIATION",
          "OUTLIER_DETECTION"
        ],
        "parameters": {
          "MOST_COMMON_VALUES": {
            "sampleSize": "50"
          },
          "MINIMUM_VALUES": {
            "sampleSize": "5"
          },
          "MAXIMUM_VALUES": {
            "sampleSize": "5"
          },
          "OUTLIER_DETECTION": {
            "threshold": "3",
            "sampleSize": "50"
          },
          "VALUE_DISTRIBUTION": {
            "binNumber": "20"
          },
          "Z_SCORE_DISTRIBUTION": {
            "binNumber": "20"
          }
        }
      }
    }
  },
  "datasetConfigurationOverride": {},
  "sampleSize": 1449891,
  "duplicateRowsCount": 0,
  "columns": [
    {
      "name": "ID",
      "type": "int",
      "correlations": {
        "ID": 1.0
      },
      "columnConfigurationOverride": {},
      "distinctValuesCount": 1373655,
      "uniqueValuesCount": 1299799,
      "entropy": 14.11323648556734,
      "mostCommonValues": [
        {
          "value": 5370286,
          "count": 4
        },
        {
          "value": 2654727,
          "count": 4
        },
        {
          "value": 5489474,
          "count": 4
        },
        {
          "value": 3309039,
          "count": 4
        },
        {
          "value": 7540228,
          "count": 4
        },
        {
          "value": 5368865,
          "count": 4
        },
        {
          "value": 419180,
          "count": 4
        },
        {
          "value": 3902038,
          "count": 4
        },
        {
          "value": 1669219,
          "count": 4
        },
        {
          "value": 1863067,
          "count": 4
        },
        {
          "value": 867822,
          "count": 4
        },
        {
          "value": 361177,
          "count": 4
        },
        {
          "value": 8243541,
          "count": 4
        },
        {
          "value": 4060169,
          "count": 4
        },
        {
          "value": 7431101,
          "count": 4
        },
        {
          "value": 2868666,
          "count": 4
        },
        {
          "value": 5112515,
          "count": 4
        },
        {
          "value": 7458336,
          "count": 4
        },
        {
          "value": 886428,
          "count": 4
        },
        {
          "value": 6237974,
          "count": 4
        },
        {
          "value": 9605475,
          "count": 4
        },
        {
          "value": 8012319,
          "count": 4
        },
        {
          "value": 7904094,
          "count": 4
        },
        {
          "value": 522760,
          "count": 4
        },
        {
          "value": 3039934,
          "count": 4
        },
        {
          "value": 763166,
          "count": 4
        },
        {
          "value": 4298500,
          "count": 4
        },
        {
          "value": 315919,
          "count": 4
        },
        {
          "value": 1251048,
          "count": 4
        },
        {
          "value": 9037718,
          "count": 4
        },
        {
          "value": 1151950,
          "count": 4
        },
        {
          "value": 3899368,
          "count": 4
        },
        {
          "value": 6122069,
          "count": 4
        },
        {
          "value": 2685337,
          "count": 4
        },
        {
          "value": 6056002,
          "count": 4
        },
        {
          "value": 7905191,
          "count": 4
        },
        {
          "value": 6569759,
          "count": 4
        },
        {
          "value": 3349554,
          "count": 4
        },
        {
          "value": 7827265,
          "count": 4
        },
        {
          "value": 3465306,
          "count": 4
        },
        {
          "value": 5747786,
          "count": 4
        },
        {
          "value": 2676093,
          "count": 4
        },
        {
          "value": 6952216,
          "count": 4
        },
        {
          "value": 754048,
          "count": 4
        },
        {
          "value": 8523008,
          "count": 4
        },
        {
          "value": 5009442,
          "count": 4
        },
        {
          "value": 2341885,
          "count": 4
        },
        {
          "value": 2179439,
          "count": 4
        },
        {
          "value": 3728499,
          "count": 4
        },
        {
          "value": 1211792,
          "count": 3
        }
      ],
      "missingValuesCount": 0,
      "kurtosis": -1.2002152216888209,
      "max": 9999997,
      "mean": 4996417.934350237,
      "min": 1,
      "skewness": 0.0027711259842627617,
      "standardDeviation": 2886663.172804553,
      "sum": 7244261395253,
      "zerosCount": 0,
      "variance": 8332824273226.048,
      "range": 9999996,
      "percentile5": 502792.5,
      "percentile25": 2494725.5,
      "percentile75": 7494560.5,
      "percentile95": 9500168.5,
      "median": 4994733.0,
      "interquartileRange": 4999835.0,
      "mode": 5370286,
      "minimumValues": [
        {
          "value": 1,
          "count": 1
        },
        {
          "value": 3,
          "count": 1
        },
        {
          "value": 12,
          "count": 1
        },
        {
          "value": 21,
          "count": 1
        },
        {
          "value": 23,
          "count": 1
        }
      ],
      "maximumValues": [
        {
          "value": 9999997,
          "count": 1
        },
        {
          "value": 9999992,
          "count": 1
        },
        {
          "value": 9999974,
          "count": 1
        },
        {
          "value": 9999973,
          "count": 1
        },
        {
          "value": 9999966,
          "count": 1
        }
      ],
      "valueDistribution": [
        {
          "bucket": [
            1,
            500000
          ],
          "count": 72081
        },
        {
          "bucket": [
            500000,
            999999
          ],
          "count": 72776
        },
        {
          "bucket": [
            999999,
            1499998
          ],
          "count": 72915
        },
        {
          "bucket": [
            1499998,
            1999997
          ],
          "count": 72883
        },
        {
          "bucket": [
            1999997,
            2499997
          ],
          "count": 72633
        },
        {
          "bucket": [
            2499997,
            2999997
          ],
          "count": 72365
        },
        {
          "bucket": [
            2999997,
            3499997
          ],
          "count": 72407
        },
        {
          "bucket": [
            3499997,
            3999997
          ],
          "count": 72979
        },
        {
          "bucket": [
            3999997,
            4499997
          ],
          "count": 72623
        },
        {
          "bucket": [
            4499997,
            4999997
          ],
          "count": 72060
        },
        {
          "bucket": [
            4999997,
            5499997
          ],
          "count": 72925
        },
        {
          "bucket": [
            5499997,
            5999997
          ],
          "count": 72298
        },
        {
          "bucket": [
            5999997,
            6499997
          ],
          "count": 72471
        },
        {
          "bucket": [
            6499997,
            6999997
          ],
          "count": 72078
        },
        {
          "bucket": [
            6999997,
            7499997
          ],
          "count": 72747
        },
        {
          "bucket": [
            7499997,
            7999997
          ],
          "count": 72194
        },
        {
          "bucket": [
            7999997,
            8499997
          ],
          "count": 72134
        },
        {
          "bucket": [
            8499997,
            8999997
          ],
          "count": 72205
        },
        {
          "bucket": [
            8999997,
            9499997
          ],
          "count": 72591
        },
        {
          "bucket": [
            9499997,
            "inf"
          ],
          "count": 72526
        }
      ],
      "zScoreOutliersCount": 0,
      "zScoreOutliersSample": [],
      "zScoreDistribution": [
        {
          "bucket": [
            "-inf",
            -1.5576521627847972
          ],
          "count": 72082
        },
        {
          "bucket": [
            -1.5576521627847972,
            -1.3844418607618485
          ],
          "count": 72775
        },
        {
          "bucket": [
            -1.3844418607618485,
            -1.2112315587389
          ],
          "count": 72916
        },
        {
          "bucket": [
            -1.2112315587389,
            -1.0380212567159512
          ],
          "count": 72884
        },
        {
          "bucket": [
            -1.0380212567159512,
            -0.8648109546930025
          ],
          "count": 72631
        },
        {
          "bucket": [
            -0.8648109546930025,
            -0.6916006526700538
          ],
          "count": 72365
        },
        {
          "bucket": [
            -0.6916006526700538,
            -0.5183903506471051
          ],
          "count": 72408
        },
        {
          "bucket": [
            -0.5183903506471051,
            -0.3451800486241564
          ],
          "count": 72978
        },
        {
          "bucket": [
            -0.3451800486241564,
            -0.1719697466012077
          ],
          "count": 72623
        },
        {
          "bucket": [
            -0.1719697466012077,
            0.001240555421741
          ],
          "count": 72060
        },
        {
          "bucket": [
            0.001240555421741,
            0.1744508574446897
          ],
          "count": 72925
        },
        {
          "bucket": [
            0.1744508574446897,
            0.3476611594676384
          ],
          "count": 72298
        },
        {
          "bucket": [
            0.3476611594676384,
            0.520871461490587
          ],
          "count": 72471
        },
        {
          "bucket": [
            0.520871461490587,
            0.6940817635135358
          ],
          "count": 72078
        },
        {
          "bucket": [
            0.6940817635135358,
            0.8672920655364845
          ],
          "count": 72747
        },
        {
          "bucket": [
            0.8672920655364845,
            1.0405023675594332
          ],
          "count": 72194
        },
        {
          "bucket": [
            1.0405023675594332,
            1.2137126695823819
          ],
          "count": 72134
        },
        {
          "bucket": [
            1.2137126695823819,
            1.3869229716053306
          ],
          "count": 72205
        },
        {
          "bucket": [
            1.3869229716053306,
            1.5601332736282794
          ],
          "count": 72591
        },
        {
          "bucket": [
            1.5601332736282794,
            "inf"
          ],
          "count": 72526
        }
      ],
      "medianAbsoluteDeviation": 2499899.0
    },
    {
      "name": "Name",
      "type": "string",
      "columnConfigurationOverride": {},
      "distinctValuesCount": 777427,
      "uniqueValuesCount": 524279,
      "entropy": 13.210510702149646,
      "mostCommonValues": [
        {
          "value": "\"Wendy Smith",
          "count": 53
        },
        {
          "value": "\"Laura Smith",
          "count": 51
        },
        {
          "value": "Clifford Smith",
          "count": 50
        },
        {
          "value": "\"Patricia Smith",
          "count": 49
        },
        {
          "value": "Nicola Smith",
          "count": 49
        },
        {
          "value": "\"Amber Smith",
          "count": 48
        },
        {
          "value": "Leonard Smith",
          "count": 48
        },
        {
          "value": "\"Clare Smith",
          "count": 48
        },
        {
          "value": "\"Ann Smith",
          "count": 47
        },
        {
          "value": "\"Karl Smith",
          "count": 47
        },
        {
          "value": "Leslie Smith",
          "count": 47
        },
        {
          "value": "\"Tracy Smith",
          "count": 47
        },
        {
          "value": "Shaun Smith",
          "count": 47
        },
        {
          "value": "Heather Smith",
          "count": 47
        },
        {
          "value": "Roy Smith",
          "count": 47
        },
        {
          "value": "Barry Smith",
          "count": 46
        },
        {
          "value": "\"Joshua Smith",
          "count": 46
        },
        {
          "value": "Rebecca Smith",
          "count": 46
        },
        {
          "value": "Suzanne Smith",
          "count": 46
        },
        {
          "value": "\"Shannon Jones",
          "count": 45
        },
        {
          "value": "\"Christine Smith",
          "count": 45
        },
        {
          "value": "\"Gavin Smith",
          "count": 45
        },
        {
          "value": "\"Katherine Smith",
          "count": 45
        },
        {
          "value": "Kim Smith",
          "count": 45
        },
        {
          "value": "Maurice Smith",
          "count": 45
        },
        {
          "value": "Lynne Smith",
          "count": 45
        },
        {
          "value": "Deborah Smith",
          "count": 45
        },
        {
          "value": "Roger Smith",
          "count": 45
        },
        {
          "value": "Stuart Smith",
          "count": 44
        },
        {
          "value": "Tom Smith",
          "count": 44
        },
        {
          "value": "\"Shirley Smith",
          "count": 44
        },
        {
          "value": "Cheryl Jones",
          "count": 44
        },
        {
          "value": "Beverley Smith",
          "count": 44
        },
        {
          "value": "Adam Smith",
          "count": 44
        },
        {
          "value": "Rita Smith",
          "count": 44
        },
        {
          "value": "\"Mathew Smith",
          "count": 44
        },
        {
          "value": "\"Kevin Smith",
          "count": 44
        },
        {
          "value": "Dawn Smith",
          "count": 44
        },
        {
          "value": "\"Mary Smith",
          "count": 44
        },
        {
          "value": "\"Susan Smith",
          "count": 44
        },
        {
          "value": "Pamela Smith",
          "count": 44
        },
        {
          "value": "Danny Smith",
          "count": 44
        },
        {
          "value": "Louise Smith",
          "count": 44
        },
        {
          "value": "\"Emma Smith",
          "count": 44
        },
        {
          "value": "Zoe Jones",
          "count": 44
        },
        {
          "value": "\"Marilyn Smith",
          "count": 43
        },
        {
          "value": "\"Jeremy Smith",
          "count": 43
        },
        {
          "value": "\"Malcolm Smith",
          "count": 43
        },
        {
          "value": "\"Julian Smith",
          "count": 43
        },
        {
          "value": "Melissa Smith",
          "count": 43
        }
      ],
      "missingValuesCount": 0,
      "max": 32,
      "mean": 15.165697283450962,
      "min": 7,
      "standardDeviation": 3.3517142424336446,
      "median": 15.0,
      "mode": 14,
      "valueDistribution": [
        {
          "bucket": [
            7,
            8
          ],
          "count": 318
        },
        {
          "bucket": [
            8,
            9
          ],
          "count": 3633
        },
        {
          "bucket": [
            9,
            10
          ],
          "count": 18176
        },
        {
          "bucket": [
            10,
            11
          ],
          "count": 52832
        },
        {
          "bucket": [
            11,
            12
          ],
          "count": 103610
        },
        {
          "bucket": [
            12,
            13
          ],
          "count": 151459
        },
        {
          "bucket": [
            13,
            14
          ],
          "count": 177096
        },
        {
          "bucket": [
            14,
            15
          ],
          "count": 180183
        },
        {
          "bucket": [
            15,
            16
          ],
          "count": 167029
        },
        {
          "bucket": [
            16,
            17
          ],
          "count": 144204
        },
        {
          "bucket": [
            17,
            18
          ],
          "count": 118351
        },
        {
          "bucket": [
            18,
            19
          ],
          "count": 94081
        },
        {
          "bucket": [
            19,
            20
          ],
          "count": 73027
        },
        {
          "bucket": [
            20,
            21
          ],
          "count": 55946
        },
        {
          "bucket": [
            21,
            22
          ],
          "count": 40908
        },
        {
          "bucket": [
            22,
            24
          ],
          "count": 47342
        },
        {
          "bucket": [
            24,
            26
          ],
          "count": 16731
        },
        {
          "bucket": [
            26,
            28
          ],
          "count": 4212
        },
        {
          "bucket": [
            28,
            30
          ],
          "count": 690
        },
        {
          "bucket": [
            30,
            "inf"
          ],
          "count": 63
        }
      ],
      "zScoreOutliersCount": 4965,
      "zScoreOutliersSample": [
        {
          "value": 32,
          "zScore": 5.022594857109844
        },
        {
          "value": 31,
          "zScore": 4.724240066793975
        },
        {
          "value": 30,
          "zScore": 4.425885276478106
        },
        {
          "value": 29,
          "zScore": 4.127530486162238
        },
        {
          "value": 28,
          "zScore": 3.8291756958463696
        },
        {
          "value": 27,
          "zScore": 3.530820905530501
        },
        {
          "value": 26,
          "zScore": 3.2324661152146326
        }
      ]
    },
    {
      "name": "Email",
      "type": "string",
      "columnConfigurationOverride": {},
      "distinctValuesCount": 393748,
      "uniqueValuesCount": 248048,
      "entropy": 12.558576160413399,
      "mostCommonValues": [
        {
          "value": "msmith@example.net",
          "count": 94
        },
        {
          "value": "usmith@example.org",
          "count": 87
        },
        {
          "value": "rsmith@example.org",
          "count": 85
        },
        {
          "value": "wsmith@example.net",
          "count": 82
        },
        {
          "value": "asmith@example.com",
          "count": 82
        },
        {
          "value": "ismith@example.com",
          "count": 81
        },
        {
          "value": "osmith@example.com",
          "count": 80
        },
        {
          "value": "psmith@example.com",
          "count": 78
        },
        {
          "value": "tsmith@example.org",
          "count": 77
        },
        {
          "value": "bsmith@example.org",
          "count": 77
        },
        {
          "value": "csmith@example.org",
          "count": 77
        },
        {
          "value": "osmith@example.net",
          "count": 76
        },
        {
          "value": "asmith@example.org",
          "count": 76
        },
        {
          "value": "qsmith@example.net",
          "count": 76
        },
        {
          "value": "ysmith@example.net",
          "count": 75
        },
        {
          "value": "nsmith@example.net",
          "count": 75
        },
        {
          "value": "ismith@example.net",
          "count": 74
        },
        {
          "value": "zsmith@example.com",
          "count": 74
        },
        {
          "value": "xsmith@example.net",
          "count": 74
        },
        {
          "value": "wsmith@example.com",
          "count": 73
        },
        {
          "value": "ysmith@example.com",
          "count": 73
        },
        {
          "value": "osmith@example.org",
          "count": 73
        },
        {
          "value": "jsmith@example.net",
          "count": 73
        },
        {
          "value": "dsmith@example.org",
          "count": 73
        },
        {
          "value": "rsmith@example.net",
          "count": 72
        },
        {
          "value": "tsmith@example.net",
          "count": 72
        },
        {
          "value": "qsmith@example.com",
          "count": 72
        },
        {
          "value": "jsmith@example.com",
          "count": 72
        },
        {
          "value": "zjones@example.org",
          "count": 72
        },
        {
          "value": "hjones@example.org",
          "count": 71
        },
        {
          "value": "usmith@example.com",
          "count": 71
        },
        {
          "value": "jsmith@example.org",
          "count": 71
        },
        {
          "value": "usmith@example.net",
          "count": 70
        },
        {
          "value": "dsmith@example.com",
          "count": 70
        },
        {
          "value": "tsmith@example.com",
          "count": 69
        },
        {
          "value": "lsmith@example.org",
          "count": 69
        },
        {
          "value": "ssmith@example.org",
          "count": 69
        },
        {
          "value": "rsmith@example.com",
          "count": 69
        },
        {
          "value": "ysmith@example.org",
          "count": 69
        },
        {
          "value": "zsmith@example.net",
          "count": 68
        },
        {
          "value": "ismith@example.org",
          "count": 68
        },
        {
          "value": "kjones@example.net",
          "count": 68
        },
        {
          "value": "csmith@example.com",
          "count": 68
        },
        {
          "value": "ssmith@example.com",
          "count": 68
        },
        {
          "value": "hsmith@example.org",
          "count": 67
        },
        {
          "value": "msmith@example.org",
          "count": 67
        },
        {
          "value": "qsmith@example.org",
          "count": 66
        },
        {
          "value": "gsmith@example.net",
          "count": 66
        },
        {
          "value": "ejones@example.org",
          "count": 66
        },
        {
          "value": "esmith@example.org",
          "count": 66
        }
      ],
      "missingValuesCount": 725329,
      "max": 33,
      "mean": 21.527123972827724,
      "min": 16,
      "standardDeviation": 2.819024071828075,
      "median": 21.0,
      "mode": 19,
      "valueDistribution": [
        {
          "bucket": [
            16,
            17
          ],
          "count": 3599
        },
        {
          "bucket": [
            17,
            18
          ],
          "count": 30841
        },
        {
          "bucket": [
            18,
            19
          ],
          "count": 76541
        },
        {
          "bucket": [
            19,
            20
          ],
          "count": 100692
        },
        {
          "bucket": [
            20,
            21
          ],
          "count": 85820
        },
        {
          "bucket": [
            21,
            22
          ],
          "count": 84903
        },
        {
          "bucket": [
            22,
            23
          ],
          "count": 75268
        },
        {
          "bucket": [
            23,
            24
          ],
          "count": 78699
        },
        {
          "bucket": [
            24,
            25
          ],
          "count": 67446
        },
        {
          "bucket": [
            25,
            26
          ],
          "count": 53199
        },
        {
          "bucket": [
            26,
            27
          ],
          "count": 34134
        },
        {
          "bucket": [
            27,
            28
          ],
          "count": 19380
        },
        {
          "bucket": [
            28,
            29
          ],
          "count": 8848
        },
        {
          "bucket": [
            29,
            30
          ],
          "count": 3736
        },
        {
          "bucket": [
            30,
            31
          ],
          "count": 1090
        },
        {
          "bucket": [
            31,
            32
          ],
          "count": 298
        },
        {
          "bucket": [
            32,
            33
          ],
          "count": 60
        },
        {
          "bucket": [
            33,
            "inf"
          ],
          "count": 8
        }
      ],
      "zScoreOutliersCount": 1456,
      "zScoreOutliersSample": [
        {
          "value": 33,
          "zScore": 4.069804207004295
        },
        {
          "value": 32,
          "zScore": 3.7150715142282724
        },
        {
          "value": 31,
          "zScore": 3.3603388214522503
        },
        {
          "value": 30,
          "zScore": 3.0056061286762277
        }
      ]
    },
    {
      "name": "Date of Birth",
      "type": "string",
      "columnConfigurationOverride": {},
      "distinctValuesCount": 84736,
      "uniqueValuesCount": 0,
      "entropy": 11.317739175014486,
      "mostCommonValues": [
        {
          "value": "12-06-1953",
          "count": 36
        },
        {
          "value": "16-04-1919",
          "count": 36
        },
        {
          "value": "30-01-1910",
          "count": 36
        },
        {
          "value": "20/12/1931",
          "count": 35
        },
        {
          "value": "01-02-1964",
          "count": 35
        },
        {
          "value": "30-05-2014",
          "count": 35
        },
        {
          "value": "30-09-1955",
          "count": 34
        },
        {
          "value": "19/08/1924",
          "count": 34
        },
        {
          "value": "06-08-1910",
          "count": 34
        },
        {
          "value": "09/04/2017",
          "count": 34
        },
        {
          "value": "01/06/1930",
          "count": 34
        },
        {
          "value": "10-04-1965",
          "count": 34
        },
        {
          "value": "22/07/1954",
          "count": 34
        },
        {
          "value": "26-11-2022",
          "count": 34
        },
        {
          "value": "25-05-1934",
          "count": 34
        },
        {
          "value": "31/03/2014",
          "count": 33
        },
        {
          "value": "09-06-1963",
          "count": 33
        },
        {
          "value": "31/03/2017",
          "count": 33
        },
        {
          "value": "01/09/1926",
          "count": 33
        },
        {
          "value": "23/07/1953",
          "count": 33
        },
        {
          "value": "09/10/1995",
          "count": 33
        },
        {
          "value": "14-07-1978",
          "count": 33
        },
        {
          "value": "21/07/1911",
          "count": 33
        },
        {
          "value": "25-02-2008",
          "count": 33
        },
        {
          "value": "04-09-1983",
          "count": 33
        },
        {
          "value": "14/08/1955",
          "count": 33
        },
        {
          "value": "09-11-1954",
          "count": 33
        },
        {
          "value": "03/12/1998",
          "count": 33
        },
        {
          "value": "15-04-2009",
          "count": 33
        },
        {
          "value": "25/07/1983",
          "count": 33
        },
        {
          "value": "05-07-1916",
          "count": 33
        },
        {
          "value": "13/12/2016",
          "count": 33
        },
        {
          "value": "13-09-1991",
          "count": 33
        },
        {
          "value": "23-11-1928",
          "count": 33
        },
        {
          "value": "13/05/1994",
          "count": 33
        },
        {
          "value": "11-02-1988",
          "count": 33
        },
        {
          "value": "21-04-1912",
          "count": 32
        },
        {
          "value": "29-06-2010",
          "count": 32
        },
        {
          "value": "07-09-1957",
          "count": 32
        },
        {
          "value": "02/10/1930",
          "count": 32
        },
        {
          "value": "16-06-1914",
          "count": 32
        },
        {
          "value": "30/07/1936",
          "count": 32
        },
        {
          "value": "04/06/1947",
          "count": 32
        },
        {
          "value": "14-04-1928",
          "count": 32
        },
        {
          "value": "11-03-1920",
          "count": 32
        },
        {
          "value": "01/12/1986",
          "count": 32
        },
        {
          "value": "20/09/1968",
          "count": 32
        },
        {
          "value": "07/02/1991",
          "count": 32
        },
        {
          "value": "01-12-1948",
          "count": 32
        },
        {
          "value": "22-11-1948",
          "count": 32
        }
      ],
      "missingValuesCount": 0,
      "max": 10,
      "mean": 10.0,
      "min": 10,
      "standardDeviation": 0.0,
      "median": 10.0,
      "mode": 10,
      "valueDistribution": [
        {
          "bucket": [
            10.0,
            10.0
          ],
          "count": 1449891
        }
      ],
      "zScoreOutliersCount": 0,
      "zScoreOutliersSample": []
    },
    {
      "name": "Address",
      "type": "string",
      "columnConfigurationOverride": {},
      "distinctValuesCount": 725370,
      "uniqueValuesCount": 725370,
      "entropy": 13.49443714847919,
      "mostCommonValues": [
        {
          "value": "9 Brett wells, Brendaport, TS60 0DE",
          "count": 1
        },
        {
          "value": "Flat 86, Donna ports, East Declantown, B42 4ZA",
          "count": 1
        },
        {
          "value": "Flat 7, Richard springs, Oliverborough, KY75 5EN",
          "count": 1
        },
        {
          "value": "Flat 0, Sean lakes, McCarthymouth, M75 9XA",
          "count": 1
        },
        {
          "value": "897 Ross stravenue, Damienstad, L5C 3XT",
          "count": 1
        },
        {
          "value": "914 Jones courts, North Katie, SM8 2NU",
          "count": 1
        },
        {
          "value": "Studio 37b, Rebecca lane, Mariemouth, NR1E 4BJ",
          "count": 1
        },
        {
          "value": "Studio 5, Michael freeway, Leahland, G2T 5PB",
          "count": 1
        },
        {
          "value": "Flat 9, Simpson well, Wrightmouth, HP1 8BJ",
          "count": 1
        },
        {
          "value": "Flat 6, Stanley inlet, Tinamouth, OL5B 8LQ",
          "count": 1
        },
        {
          "value": "333 Butcher mission, West Brandon, HD3H 4JT",
          "count": 1
        },
        {
          "value": "Flat 31D, Brady square, Lake Dawnberg, S68 9BX",
          "count": 1
        },
        {
          "value": "Studio 0, Woodward expressway, Joanneshire, E8 5YG",
          "count": 1
        },
        {
          "value": "Flat 7, Edwards camp, North Margaret, B72 6AW",
          "count": 1
        },
        {
          "value": "585 Dylan pike, Deborahmouth, W6C 0SY",
          "count": 1
        },
        {
          "value": "40 Lewis village, South Dylan, M3 0LQ",
          "count": 1
        },
        {
          "value": "Studio 0, Jarvis crossing, Lake Neil, N1 5PG",
          "count": 1
        },
        {
          "value": "Studio 8, Smith walk, West Jessicatown, HX90 1UP",
          "count": 1
        },
        {
          "value": "Studio 41I, Little shoals, East Rhys, BL4 8FA",
          "count": 1
        },
        {
          "value": "65 Charlotte via, Lake Tracyborough, B7 7RP",
          "count": 1
        },
        {
          "value": "28 Jodie forest, Lake Amberview, FK74 6LH",
          "count": 1
        },
        {
          "value": "7 O'Connor orchard, South Catherine, HG83 8PB",
          "count": 1
        },
        {
          "value": "Studio 73D, Dennis groves, Thompsonbury, M3C 1LG",
          "count": 1
        },
        {
          "value": "350 Luke passage, Woodchester, KY96 1BP",
          "count": 1
        },
        {
          "value": "Studio 75, Thorpe lodge, Arthurhaven, M5F 0XH",
          "count": 1
        },
        {
          "value": "Flat 64, Taylor run, South Eleanorville, NW7 8JA",
          "count": 1
        },
        {
          "value": "Flat 34i, George crossing, South Gerard, G25 4YH",
          "count": 1
        },
        {
          "value": "74 Wilson courts, Lyonsfurt, HS7 3JZ",
          "count": 1
        },
        {
          "value": "Studio 18, Leslie square, South Yvonne, G1 5EP",
          "count": 1
        },
        {
          "value": "0 Singh throughway, East Abbie, M00 1HN",
          "count": 1
        },
        {
          "value": "78 Elaine plaza, Leannetown, S01 1RL",
          "count": 1
        },
        {
          "value": "1 Lloyd land, Cartershire, G80 4HD",
          "count": 1
        },
        {
          "value": "Flat 72, Alan common, Henryside, BT32 1YB",
          "count": 1
        },
        {
          "value": "31 Hanson valley, Alexanderberg, ST2P 8AY",
          "count": 1
        },
        {
          "value": "Flat 6, Fisher forest, Allanbury, GU4 4AU",
          "count": 1
        },
        {
          "value": "505 Gerard groves, Lloydborough, N62 0DN",
          "count": 1
        },
        {
          "value": "02 Paige plaza, Lamberttown, E2F 3RJ",
          "count": 1
        },
        {
          "value": "0 Mandy corners, Port Staceychester, TS0 9BJ",
          "count": 1
        },
        {
          "value": "319 Wilkinson wall, Douglastown, DL6 7XP",
          "count": 1
        },
        {
          "value": "Studio 90, Olivia divide, Dobsonfurt, ME3 5WR",
          "count": 1
        },
        {
          "value": "23 Turner common, Port Charlesland, IV7 4XW",
          "count": 1
        },
        {
          "value": "29 Slater neck, Tracyton, S3 8TX",
          "count": 1
        },
        {
          "value": "Studio 07F, Conor burg, Vincentfurt, G41 5XY",
          "count": 1
        },
        {
          "value": "Flat 00l, Paula freeway, Francisville, G0E 2HN",
          "count": 1
        },
        {
          "value": "Studio 91, Hudson lake, Begumland, SR65 6SW",
          "count": 1
        },
        {
          "value": "Flat 2, Samuel lock, South Ashleighshire, ME9V 9NL",
          "count": 1
        },
        {
          "value": "Studio 56, Patel canyon, North Wendyhaven, PE8 6RD",
          "count": 1
        },
        {
          "value": "Flat 2, Wilkinson run, Duncanhaven, WA1 9TF",
          "count": 1
        },
        {
          "value": "Flat 0, Helen forks, West Craigbury, G0 8DP",
          "count": 1
        },
        {
          "value": "9 Davies harbor, New Owenville, TW9N 1HF",
          "count": 1
        }
      ],
      "missingValuesCount": 724521,
      "max": 65,
      "mean": 41.99551401353792,
      "min": 27,
      "standardDeviation": 5.073414345780278,
      "median": 42.0,
      "mode": 43,
      "valueDistribution": [
        {
          "bucket": [
            27,
            28
          ],
          "count": 7
        },
        {
          "bucket": [
            28,
            29
          ],
          "count": 58
        },
        {
          "bucket": [
            29,
            31
          ],
          "count": 1232
        },
        {
          "bucket": [
            31,
            33
          ],
          "count": 9732
        },
        {
          "bucket": [
            33,
            35
          ],
          "count": 35076
        },
        {
          "bucket": [
            35,
            37
          ],
          "count": 67778
        },
        {
          "bucket": [
            37,
            39
          ],
          "count": 85477
        },
        {
          "bucket": [
            39,
            41
          ],
          "count": 91901
        },
        {
          "bucket": [
            41,
            43
          ],
          "count": 100102
        },
        {
          "bucket": [
            43,
            45
          ],
          "count": 102797
        },
        {
          "bucket": [
            45,
            47
          ],
          "count": 88986
        },
        {
          "bucket": [
            47,
            49
          ],
          "count": 64427
        },
        {
          "bucket": [
            49,
            51
          ],
          "count": 40893
        },
        {
          "bucket": [
            51,
            53
          ],
          "count": 22299
        },
        {
          "bucket": [
            53,
            55
          ],
          "count": 9878
        },
        {
          "bucket": [
            55,
            57
          ],
          "count": 3548
        },
        {
          "bucket": [
            57,
            59
          ],
          "count": 922
        },
        {
          "bucket": [
            59,
            61
          ],
          "count": 221
        },
        {
          "bucket": [
            61,
            63
          ],
          "count": 33
        },
        {
          "bucket": [
            63,
            "inf"
          ],
          "count": 3
        }
      ],
      "zScoreOutliersCount": 579,
      "zScoreOutliersSample": [
        {
          "value": 65,
          "zScore": 4.534320364666381
        },
        {
          "value": 63,
          "zScore": 4.140108525520331
        },
        {
          "value": 62,
          "zScore": 3.9430026059473056
        },
        {
          "value": 61,
          "zScore": 3.74589668637428
        },
        {
          "value": 60,
          "zScore": 3.548790766801255
        },
        {
          "value": 59,
          "zScore": 3.3516848472282295
        },
        {
          "value": 58,
          "zScore": 3.1545789276552045
        }
      ]
    }
  ],
  "jobName": "dirty-data-demo-dataset-profile-job",
  "jobRunId": "db_59a71d244ff350bfb06c159b3304cd0c79d73dd76a4ca553bba59609d0c34938",
  "location": "s3://databrew-dataprofile/dirty-data-demo-dataset_59a71d244ff350bfb06c159b3304cd0c79d73dd76a4ca553bba59609d0c34938.json",
  "startedOn": "2024-03-27T12:48:38.100164",
  "writtenOn": "2024-03-27T12:50:16.213216",
  "version": "1.0"
}

# Output CSV file
csv_file = 'output.csv'

# Convert JSON to CSV
json_to_csv(json_data, csv_file)

print(f"JSON data has been successfully converted to CSV. Output saved to {csv_file}.")
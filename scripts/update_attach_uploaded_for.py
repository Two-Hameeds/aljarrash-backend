import requests

API_URL = "https://jellyfish-app-ebfd5.ondigitalocean.app/api"

ids_globals = {
    35: 41,
    36: 42,
    38: 44,
    41: 47,
    46: 48,
    47: 49,
    48: 50,
    49: 51,
    50: 52,
    51: 53,
    53: 55,
    54: 56,
    55: 57,
    56: 58,
    57: 59,
    58: 60,
    59: 61,
    60: 62,
    61: 63,
    62: 64,
    63: 65,
    64: 66,
    65: 67,
    66: 68,
    67: 69,
    68: 70,
    69: 71,
    71: 73,
    72: 74,
    73: 75,
    74: 76,
    75: 77,
    76: 78,
    77: 79,
    78: 80,
    79: 81,
    80: 82,
    81: 83,
    82: 84,
    83: 85,
    84: 86,
    85: 87,
    86: 88,
    87: 89,
    130: 92,
    131: 93,
    132: 94,
    133: 95,
    134: 96,
    135: 97,
    136: 98,
    137: 99,
    138: 100,
    139: 101,
    140: 102,
    141: 103,
    142: 104,
    143: 105,
    144: 106,
    145: 107,
    146: 108,
    147: 109,
    148: 110,
    149: 111,
    150: 112,
    151: 113,
    152: 114,
    153: 115,
    154: 116,
    155: 117,
    156: 118,
    157: 119,
    158: 120,
    159: 121,
    160: 122,
    161: 123,
    162: 124,
    163: 125,
    164: 126,
    165: 127,
    166: 128,
    167: 129,
    168: 130,
    169: 131,
    170: 132,
    171: 133,
    172: 134,
    173: 135,
    174: 136,
    175: 137,
    176: 138,
    177: 139,
    178: 140,
    179: 141,
    180: 142,
    181: 143,
    182: 144,
    183: 145,
    185: 147,
    186: 148,
    187: 149,
    188: 150,
    189: 151,
    190: 152,
    191: 153,
    192: 154,
    193: 155,
    194: 156,
    195: 157,
    196: 158,
    184: 146,
    197: 159,
    198: 160,
    199: 161,
    200: 162,
    201: 163,
    202: 164,
    203: 165,
    204: 166,
    205: 167,
    206: 168,
    207: 169,
    208: 170,
    209: 171,
    210: 172,
    211: 173,
    212: 174,
    213: 175,
    214: 176,
    215: 177,
    216: 178,
    217: 179,
    218: 180,
    219: 181,
    220: 182,
    221: 183,
    222: 184,
    223: 185,
    224: 186,
    225: 187,
    226: 188,
    227: 189,
    228: 190,
    229: 191,
    230: 192,
    231: 193,
    232: 194,
    233: 195,
    234: 196,
    235: 197,
    236: 198,
    237: 199,
    238: 200,
    239: 201,
    240: 202,
    241: 203,
    242: 204,
    243: 205,
}


def get_project_ids():
    response = requests.get(f"{API_URL}/design")
    count = 0
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            if not project["id"] == project["global_id"]:
                count = count + 1
                print(f"{project['id']}: {project['global_id']}", end=", ")
        print(f"{count=}")
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
        
        
def get_attachments():
    response = requests.get(f"{API_URL}/attachments/")
    count = 0
    if(response.status_code == 200):
        attachments = response.json()
        for attachment in attachments:
            if(attachment["uploaded_for"] in ids_globals.keys()):
                count = count + 1
                print(f"{attachment['id']}: {attachment['uploaded_for']}")
        print(f"{count=}")
    else:
        print(f"Failed to retrieve attachments. Status code: {response.status_code}")


if __name__ == "__main__":
    # get_project_ids()
    get_attachments()

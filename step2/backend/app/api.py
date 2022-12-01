from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware






phddata = [
  {
    "year": 2000,
    "RUG": 263,
    "UvA": 296,
    "RU": 227,
    "VU": 158,
    "TUD": 169,
    "TUE": 190,
    "WUR": 200,
    "EUR": 117,
    "UU": 99,
    "LEI": 14,
    "UM": 89,
    "UT": 109,
    "UTi": 68
  },
  {
    "year": 2002,
    "RUG": 259,
    "UvA": 378,
    "RU": 216,
    "VU": 146,
    "TUD": 177,
    "TUE": 234,
    "WUR": 233,
    "EUR": 117,
    "UU": 183,
    "LEI": 10,
    "UM": 105,
    "UT": 132,
    "UTi": 65
  },
  {
    "year": 2003,
    "RUG": 274,
    "UvA": 354,
    "RU": 224,
    "VU": 200,
    "TUD": 181,
    "TUE": 218,
    "WUR": 185,
    "EUR": 142,
    "UU": 203,
    "LEI": 12,
    "UM": 138,
    "UT": 160,
    "UTi": 63
  },
  {
    "year": 2004,
    "RUG": 319,
    "UvA": 378,
    "RU": 219,
    "VU": 226,
    "TUD": 199,
    "TUE": 254,
    "WUR": 179,
    "EUR": 154,
    "UU": 184,
    "LEI": 23,
    "UM": 126,
    "UT": 138,
    "UTi": 61
  },
  {
    "year": 2005,
    "RUG": 335,
    "UvA": 362,
    "RU": 229,
    "VU": 245,
    "TUD": 215,
    "TUE": 282,
    "WUR": 201,
    "EUR": 213,
    "UU": 189,
    "LEI": 222,
    "UM": 155,
    "UT": 176,
    "UTi": 73
  },
  {
    "year": 2006,
    "RUG": 389,
    "UvA": 369,
    "RU": 264,
    "VU": 268,
    "TUD": 209,
    "TUE": 257,
    "WUR": 233,
    "EUR": 249,
    "UU": 385,
    "LEI": 280,
    "UM": 144,
    "UT": 186,
    "UTi": 97
  },
  {
    "year": 2007,
    "RUG": 333,
    "UvA": 436,
    "RU": 303,
    "VU": 294,
    "TUD": 225,
    "TUE": 283,
    "WUR": 258,
    "EUR": 237,
    "UU": 423,
    "LEI": 266,
    "UM": 191,
    "UT": 170,
    "UTi": 88
  },
  {
    "year": 2008,
    "RUG": 355,
    "UvA": 423,
    "RU": 276,
    "VU": 442,
    "TUD": 225,
    "TUE": 295,
    "WUR": 218,
    "EUR": 260,
    "UU": 304,
    "LEI": 316,
    "UM": 177,
    "UT": 196,
    "UTi": 88
  },
  {
    "year": 2009,
    "RUG": 391,
    "UvA": 467,
    "RU": 274,
    "VU": 465,
    "TUD": 261,
    "TUE": 281,
    "WUR": 201,
    "EUR": 283,
    "UU": 359,
    "LEI": 315,
    "UM": 203,
    "UT": 220,
    "UTi": 90
  },
  {
    "year": 2010,
    "RUG": 417,
    "UvA": 495,
    "RU": 282,
    "VU": 504,
    "TUD": 333,
    "TUE": 282,
    "WUR": 209,
    "EUR": 282,
    "UU": 333,
    "LEI": 332,
    "UM": 178,
    "UT": 215,
    "UTi": 111
  },
  {
    "year": 2011,
    "RUG": 423,
    "UvA": 524,
    "RU": 310,
    "VU": 510,
    "TUD": 317,
    "TUE": 309,
    "WUR": 201,
    "EUR": 294,
    "UU": 309,
    "LEI": 333,
    "UM": 195,
    "UT": 209,
    "UTi": 130
  },
  {
    "year": 2012,
    "RUG": 476,
    "UvA": 580,
    "RU": 343,
    "VU": 533,
    "TUD": 300,
    "TUE": 339,
    "WUR": 236,
    "EUR": 308,
    "UU": 356,
    "LEI": 393,
    "UM": 234,
    "UT": 210,
    "UTi": 132
  },
  {
    "year": 2013,
    "RUG": 439,
    "UvA": 693,
    "RU": 387,
    "VU": 626,
    "TUD": 352,
    "TUE": 325,
    "WUR": 276,
    "EUR": 297,
    "UU": 356,
    "LEI": 394,
    "UM": 251,
    "UT": 228,
    "UTi": 132
  },
  {
    "year": 2014,
    "RUG": 447,
    "UvA": 672,
    "RU": 359,
    "VU": 610,
    "TUD": 373,
    "TUE": 343,
    "WUR": 288,
    "EUR": 315,
    "UU": 348,
    "LEI": 418,
    "UM": 291,
    "UT": 257,
    "UTi": 155
  },
  {
    "year": 2015,
    "RUG": 505,
    "UvA": 671,
    "RU": 366,
    "VU": 661,
    "TUD": 353,
    "TUE": 355,
    "WUR": 305,
    "EUR": 328,
    "UU": 340,
    "LEI": 410,
    "UM": 364,
    "UT": 245,
    "UTi": 166
  },
  {
    "year": 2016,
    "RUG": 539,
    "UvA": 745,
    "RU": 415,
    "VU": 628,
    "TUD": 394,
    "TUE": 329,
    "WUR": 296,
    "EUR": 368,
    "UU": 327,
    "LEI": 402,
    "UM": 349,
    "UT": 288,
    "UTi": 124
  },
  {
    "year": 2017,
    "RUG": 508,
    "UvA": 749,
    "RU": 435,
    "VU": 587,
    "TUD": 357,
    "TUE": 313,
    "WUR": 298,
    "EUR": 310,
    "UU": 323,
    "LEI": 427,
    "UM": 341,
    "UT": 214,
    "UTi": 119
  },
  {
    "year": 2018,
    "RUG": 513,
    "UvA": 765,
    "RU": 389,
    "VU": 577,
    "TUD": 368,
    "TUE": 389,
    "WUR": 286,
    "EUR": 322,
    "UU": 310,
    "LEI": 444,
    "UM": 363,
    "UT": 262,
    "UTi": 130
  },
  {
    "year": 2019,
    "RUG": 551,
    "UvA": 765,
    "RU": 433,
    "VU": 553,
    "TUD": 400,
    "TUE": 395,
    "WUR": 294,
    "EUR": 327,
    "UU": 328,
    "LEI": 433,
    "UM": 341,
    "UT": 259,
    "UTi": 108
  },
  {
    "year": 2020,
    "RUG": 578,
    "UvA": 733,
    "RU": 369,
    "VU": 608,
    "TUD": 364,
    "TUE": 325,
    "WUR": 282,
    "EUR": 314,
    "UU": 282,
    "LEI": 446,
    "UM": 319,
    "UT": 203,
    "UTi": 102
  },
  {
    "year": 2021,
    "RUG": 142,
    "UvA": 179,
    "RU": 97,
    "VU": 158,
    "TUD": 125,
    "TUE": 73,
    "WUR": 64,
    "EUR": 59,
    "UU": 36,
    "LEI": 101,
    "UM": 96,
    "UT": 43,
    "UTi": 20
  }
]



app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)



@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Data Visualizer"}


@app.get("/phddata", tags=["phddata"],status_code = 200)
async def get_phddata() -> dict:
    return { "data": phddata }



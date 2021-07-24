data = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "stroke": "#555555",
        "stroke-width": 5,
        "stroke-opacity": 0.8
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            103.0078125,
            67.47492238478702
          ],
          [
            21.796875,
            17.97873309555617
          ],
          [
            101.25,
            37.43997405227057
          ],
          [
            114.2578125,
            65.80277639340238
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -99.16801602348116,
              19.41085844601428              
            ],
            [
              -103.35937499999999,
              7.710991655433217
            ],
            [
              -47.8125,
              27.994401411046148
            ],
            [
              -52.3828125,
              54.57206165565852
            ],
            [
              -71.3671875,
              68.65655498475735
            ],
            [
              -114.60937499999999,
              42.8115217450979
            ]
          ]
        ]
      }
    }
  ]
}

import geoplot
import geoplot.crs as gcrs

geoplot.polyplot(data, projection=gcrs.AlbersEqualArea(), edgecolor='darkgrey', facecolor='lightgrey', linewidth=.3,
    figsize=(12, 8))










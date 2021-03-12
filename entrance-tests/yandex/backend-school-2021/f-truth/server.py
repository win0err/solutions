from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify([
        {
            "magnetic": [
                47,
                10,
                43,
                61
            ],
            "electric": [
                62,
                45,
                15,
                44,
                20
            ],
            "gravitational": [
                5,
                41,
                63,
                -9,
                9,
                12
            ]
        },
        {
            "electric": [
                1,
                82,
                56,
                48
            ],
            "magnetic": [
                -2,
                58,
                96,
                14,
                94
            ],
            "gravitational": [
                -8,
                98,
                -5
            ]
        },
        {
            "electric": [
                68,
                81,
                40,
                -2,
                -8
            ],
            "magnetic": [
                74,
                -12,
                67,
                54
            ],
            "gravitational": [
                85,
                -6
            ]
        }
    ])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

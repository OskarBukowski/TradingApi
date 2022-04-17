import json
import sys
sys.path.append('/home/obukowski/Desktop/TradingApi/src/')

from src.HttpServerOperator import app

class TestHttpServerOperator:

    @staticmethod
    def test_get_exchanges():
        response = app.test_client().get('http://192.168.0.178:5000/exchanges')
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data['exchanges'] == ["zonda","wazirx","bitkub","huobi","gemini","bitso"]





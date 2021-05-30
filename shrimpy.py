import shrimpy

public_key = 'bea8edb348af226...'
secret_key = 'df84c39fb49026dcad9d99...'

client = shrimpy.ShrimpyApiClient(public_key, secret_key)

supported_exchanges = client.get_supported_exchanges()

exchange_assets = client.get_exchange_assets('bittrex')

trading_pairs = client.get_trading_pairs('bittrex')

ticker = client.get_ticker('bittrex')

orderbooks = client.get_orderbooks(
    'bittrex',  # exchange
    'XLM',      # base_symbol
    'BTC',      # quote_symbol
    10          # limit
)

candles = client.get_candles(
    'bittrex',  # exchange
    'XLM',      # base_trading_symbol
    'BTC',      # quote_trading_symbol
    '15m'       # interval
)
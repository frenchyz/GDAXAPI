
import gdax;
public_client = gdax.PublicClient();
stats = public_client.get_product_24hr_stats('BTC-USD');
print("Open: {0} High: {1} Low: {2} Volume: {3}".format(stats['open'], stats['high'], stats['low'], stats['volume']))
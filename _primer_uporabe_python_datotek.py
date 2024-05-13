# Primer ob uporabi folder-jev, ki NIMAJO presledkov v imenu
from Napoved_Spletnih_Strani.website_prediction1 import WebScraper

# -----------------------------------------------------------------------------------------------
# Primer ob uporabi folder-jev, ki IMAJO presldke v imenu
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Napoved Spletnih Strani"))
sys.path.append(module_path)

from website_prediction1 import WebScraper

# -----------------------------------------------------------------------------------------------
# Deluje v obeh primerih
webscraper = WebScraper()
webscraper.run()

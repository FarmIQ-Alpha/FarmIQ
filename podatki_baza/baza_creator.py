from database import *

print(database_get('delete from podkategorija_kmečki_pridelki_leto where podkategorija_id in (SELECT podkategorija_id FROM podkategorija_kmečki_pridelki WHERE kategorija_id=2'))



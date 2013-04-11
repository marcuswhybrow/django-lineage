from django.conf import settings

ANCESTOR_PHRASE = getattr(settings, 'LINEAGE_ANCESTOR_PHRASE', 'active')

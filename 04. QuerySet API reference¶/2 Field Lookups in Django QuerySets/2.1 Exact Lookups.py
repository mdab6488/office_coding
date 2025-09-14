# Field lookups are how you specify the meat of an SQL WHERE clause in Django. They're used with filter(), exclude(), and get() methods.

"""
Lookup	Description	Example
exact	Exact match (default)	Member.objects.filter(firstname__exact='Emil')
iexact	Case-insensitive exact match	Member.objects.filter(firstname__iexact='emil')
"""
# Exact match (default behavior)
members = Member.objects.filter(firstname='Emil')  # Equivalent to __exact

# Case-insensitive exact match
members = Member.objects.filter(firstname__iexact='emil')  # Matches 'Emil', 'emil', 'EMIL'
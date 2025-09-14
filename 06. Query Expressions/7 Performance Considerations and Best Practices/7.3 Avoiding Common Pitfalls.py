# Be aware of common pitfalls and limitations when working with expressions 

# F() expressions persist after save - remember to refresh
company = Company.objects.get(pk=1)
company.num_employees = F('num_employees') + 10
company.save()  # F() expression is saved with instance
company.refresh_from_db()  # Necessary to see updated value

# Database support varies for different operations
# String operations with F() may have limited database support

# Be cautious with null values in expressions
# Use Coalesce to handle nulls appropriately
Product.objects.annotate(
    effective_price=Coalesce(F('discounted_price'), F('price'))
)

# Table: Performance Comparison of Different Approaches

# Approach	Database Queries	Race Condition Risk	Performance
# Python-based operation	Multiple (fetch + save)	High	Low
# F() expression update	Single	Low	High
# Bulk update with expressions	Single	Low	Very High

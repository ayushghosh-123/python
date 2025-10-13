from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            print('Access denied: Admins only')
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print('Access granted to the tea inventory')

# Example usage
access_tea_inventory('admin')      # ✅ Access granted
access_tea_inventory('customer')   # ❌ Access denied

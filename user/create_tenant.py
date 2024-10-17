from user.models import Tenant, Domain

def create_tenant(name, schema_name, is_public = False):
    
    if is_public:
        tenant = Tenant(schema_name='public', name='Public')
        tenant.save()
        domain = Domain(domain='localhost', tenant=tenant, is_primary=True)
        domain.save()

    new_tenant = Tenant(schema_name=schema_name, name=name)
    new_tenant.save()

    new_domain_name = schema_name + '.localhost'
    new_domain = Domain(domain=new_domain_name, tenant=new_tenant, is_primary=True)
    new_domain.save()


    

    

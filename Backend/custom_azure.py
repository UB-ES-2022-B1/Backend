from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'houshstorage'  # Must be replaced by your <storage_account_name>
    account_key = 'QYKpAl2PqpJ1agt93Emf75t7jXZopWYSrVcC828eeG2M/wnEnAT/GsERE0q956unML1lzyvxDsU6+AStUtAvcg=='  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'houshstorage'  # Must be replaced by your storage_account_name
    account_key = 'QYKpAl2PqpJ1agt93Emf75t7jXZopWYSrVcC828eeG2M/wnEnAT/GsERE0q956unML1lzyvxDsU6+AStUtAvcg=='  # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

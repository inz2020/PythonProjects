from  buildrzapi.viewsets import ParcelleViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('parcelle',ParcelleViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book, name='book'),
    path('infectioncontrolcleaning/',views.infectioncontrolcleaning,name='infectioncontrolcleaning'),
    path('Builderscleaning/',views.Builderscleaning, name='Builderscleaning'),
    path('constructioncleaning/',views.constructioncleaning, name='constructioncleaning'),
    path('rubbishremoval/',views.rubbishremoval, name='rubbishremoval'),
    path('carpetcleaning/',views.carpetcleaning, name='carpetcleaning'),
    path('upholsterycleaning/',views.upholsterycleaning, name='upholsterycleaning'),
    path('mattresscleaning/',views.mattresscleaning, name='mattresscleaning'),
    path('commercialkitchencleaning/',views.commercialkitchencleaning, name='commercialkitchencleaning'),
    path('commercialkitchencanopycleaning/',views.commercialkitchencanopycleaning, name='commercialkitchencanopycleaning'),
    path('ovencleaning/',views.ovencleaning, name='ovencleaning'),
    path('endleasecleaning/',views.endleasecleaning, name='endleasecleaning'),
    path('guttercleaning/',views.guttercleaning, name='guttercleaning'),
    path('highpressurecleaning/',views.highpressurecleaning, name='highpressurecleaning'),
    path('strippingsealingfloor/',views.strippingsealingfloor, name='strippingsealingfloor'),
    path('tilegroutcleaning/',views.tilegroutcleaning, name='tilegroutcleaning'),
    path('wallcleaning/',views.wallcleaning, name='wallcleaning'),
    path('windowcleaning/',views.windowcleaning, name='windowcleaning'),
    path('highrisewindowscleaning/',views.highrisewindowscleaning, name='highrisewindowscleaning'),
    path('highhustingcleaning/',views.highhustingcleaning, name='highhustingcleaning'),
    path('ventscleaning/',views.ventscleaning, name='ventscleaning'),
    path('factorycleaning/',views.factorycleaning, name='factorycleaning'),
    path('warehousecleaning/',views.warehousecleaning, name='warehousecleaning'),
    path('poolcleaning/',views.poolcleaning, name='poolcleaning'),
    path('gardenmowing/',views.gardenmowing, name='gardenmowing'),
    path('oneOffcleaning/',views.oneOffcleaning, name='oneOffcleaning'),
    path('regularofficecleaning/',views.regularofficecleaning, name='regularofficecleaning'),
    
]




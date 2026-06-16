from django.urls import path

from . import views

urlpatterns = [
    # ── HTML template views ────────────────────────────────────────────────────
    path('members/', views.members, name='members'),
    path('members/<int:pk>/', views.member_detail_view, name='member_detail_view'),
    path('members/<int:pk>/delete/', views.member_delete_view, name='member_delete'),
    path('members/<int:pk>/update/', views.member_update_view, name='member_update'),

    # ── DRF API views (return JSON) ────────────────────────────────────────────
    path('api/members/', views.member_list, name='member_list'),
    path('api/members/data/', views.members_data, name='members_data'),
    path('api/members/<int:pk>/', views.member_detail, name='member_detail'),
]

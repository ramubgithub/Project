"""cyber_security_alert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from cyber_alert import views as alert_view
from admins import views as admin_view

urlpatterns = [

    path(r'^admin/', admin.site.urls),

    path('', alert_view.admin_login, name="admin_login"),
    path('admin_register', alert_view.admin_register, name="admin_registe"),
    path('giver_transaction', alert_view.giver_transaction, name="giver_transaction"),
    path('analyze_page', alert_view.analyze_page, name="analyze_page"),
    path('viewer/(?P<chart_type>\w+)', alert_view.viewer, name="viewer"),
    path('update', alert_view.update, name="update"),
    path('logout_page', alert_view.logout_page, name="logout_page"),
    path('mydetails', alert_view.mydetails, name="mydetails"),
    path('show', alert_view.show, name="show"),
    path('receivealert', alert_view.receivealert, name="receivealert"),

    path('admins/admin_page', admin_view.admin_page, name="admin_page"),
    path('admins/analyze', admin_view.analyze, name="analyze"),
    path('admins/adlogout', admin_view.adlogout, name="adlogout"),
    path('admins/charts/(?P<chart_type>\w+)', admin_view.charts,name="charts"),
    path('admins/riskuser',admin_view.riskuser, name="riskuser"),
    path('admins/riskalert/(?P<tuser>\d+)',admin_view.riskalert, name="riskalert"),
]

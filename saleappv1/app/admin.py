from flask_admin import expose, BaseView

from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.modules import Category, Product

class ContactView(BaseView):
    @expose('/')
    def index(seft):
        return seft.render('admin/contact.html')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view((ContactView(name='Liên Hệ')))
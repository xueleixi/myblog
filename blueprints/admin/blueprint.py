from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

admin_page = Blueprint('admin', __name__,
                       template_folder='templates')


# 优先级比通配符高
@admin_page.route('/home')
def home():
    return __file__


@admin_page.route('/', defaults={'page': 'index'})
@admin_page.route('/<page>')
def show(page):
    try:
        return render_template('/admin/%s.html' % page)
    except TemplateNotFound:
        abort(404)


@admin_page.errorhandler(404)
def page_not_found(e):
    return render_template('/admin/404.html')

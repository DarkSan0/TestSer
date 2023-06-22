from flask import  render_template, request, redirect, url_for, session, flash
from ..client import *
from ..log import *
from ..secure import *

def home_admin ():
    return Redirecionador_PLOG("principal.html", redirect(url_for(login)))

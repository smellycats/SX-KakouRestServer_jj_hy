# -*- coding: utf-8 -*-
import arrow

from app import db, app
from app.models import *


def test_kkdd():
    kkdd = VKkxx.query.all()
    for i in kkdd:
        print i.kkdm, i.kkmc.encode('utf-8')
        print(type(i.kkdm))

def test_kakou():
    c = VGcxx.query.filter_by(clxxbh=102786386).first()
    print(c.jgsk, c.qjtp)


if __name__ == '__main__':
    test_kkdd()
    #test_kakou()


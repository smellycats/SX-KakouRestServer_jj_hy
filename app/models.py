# -*- coding: utf-8 -*-
import arrow

from . import db


class Users(db.Model):
    """用户"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))
    scope = db.Column(db.String(128), default='')
    date_created = db.Column(
        db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    date_modified = db.Column(
        db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, username, password, scope='', banned=0,
                 date_created=None, date_modified=None):
        self.username = username
        self.password = password
        self.scope = scope
        now = arrow.now('PRC').datetime.replace(tzinfo=None)
        if date_created is None:
            self.date_created = now
        else:
            self.date_created = date_created
        if date_modified is None:
            self.date_modified = now
        else:
            self.date_modified = date_modified
        self.banned = banned

    def __repr__(self):
        return '<Users %r>' % self.id


class Scope(db.Model):
    """权限范围"""
    __tablename__ = 'scope'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Scope %r>' % self.id


class Kkdd(db.Model):
    """卡口地点"""
    __tablename__ = 'kkdd'
    id = db.Column(db.Integer, primary_key=True)
    kkdd_id = db.Column(db.String(256))
    kkdd_name = db.Column(db.String(256))
    fxbh_list = db.Column(db.String(256))
    ps = db.Column(db.String(256))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, kkdd_id, kkdd_name, fxbh_list, ps, banned=0):
	self.kkdd_id = kkdd_id
	self.kkdd_name = kkdd_name
	self.fxbh_list = fxbh_list
	self.ps = ps
	self.banned = banned

    def __repr__(self):
        return '<Kkdd %r>' % self.id


class VGcxx(db.Model):
    """过车表"""
    __tablename__ = 'v_gcxx'
    __bind_key__ = 'kakou'
    clxxbh = db.Column(db.Integer, primary_key=True)
    kkbh = db.Column(db.String(32))
    kkmc = db.Column(db.String(64))
    wd = db.Column(db.String(30))
    jd = db.Column(db.String(30))
    jgsk = db.Column(db.DateTime)
    cdbh = db.Column(db.Integer)
    hphm = db.Column(db.String(20))
    hpys = db.Column(db.String(10))
    xsfxdm = db.Column(db.Integer)
    xsfx = db.Column(db.String(64))
    cllx = db.Column(db.String(3))
    csys = db.Column(db.String(1))
    hpzl = db.Column(db.String(2))
    clsd = db.Column(db.Integer)
    hptp = db.Column(db.String(367))
    qjtp = db.Column(db.String(367))

    def __init__(self, kkbh, kkmc, wd, jd, jgsk, cdbh, hpys, xsfxdm,
		 xsfx, cllx, csys, hpzl, clsd, hptp, qjtp):
        self.kkbh = kkbh
        self.kkmc = kkmc
        self.wd = wd
        self.jd = jd
        self.jgsk = jgsk
        self.cdbh = cdbh
        self.hpys = hpys
        self.xsfxdm = xsfxdm
        self.xsfx = xsfx
        self.cllx = cllx
        self.csys = csys
        self.hpzl = hpzl
        self.clsd = clsd
        self.hptp = hptp
        self.qjtp = qjtp

    def __repr__(self):
        return '<VGcxx %r>' % self.clxxbh


class VKkxx(db.Model):
    """卡点表"""
    __tablename__ = 'v_kkxx'
    __bind_key__ = 'kakou'
    kkid = db.Column(db.Integer, primary_key=True)
    kkdm = db.Column(db.String(32))
    kkmc = db.Column(db.String(64))
    wd = db.Column(db.String(30))
    jd = db.Column(db.String(30))

    def __init__(self, kkdm, kkmc, wd, jd):
        self.kkdm = kkdm
        self.kkmc = kkmc
        self.wd = wd
        self.jd = jd

    def __repr__(self):
        return '<VKkxx %r>' % self.kkid


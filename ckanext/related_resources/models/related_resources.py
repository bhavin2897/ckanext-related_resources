# encoding: utf-8

from six import text_type
from sqlalchemy import orm, types, Column, Table, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.expression import false
from ckan.model import meta, Package, domain_object


__all__ = ['RelatedResources', 'related_resources_table']

related_resources_table = Table('related_resources', meta.metadata,
                Column('id', types.UnicodeText, primary_key = True, nullable = False),
                Column('package_id', types.UnicodeText, ForeignKey('package.id'), nullable = False),
                Column('relation_id',types.UnicodeText),
                Column('relationType',types.UnicodeText),
                Column('relationIdType', types.UnicodeText)
        )



class RelatedResources(domain_object.DomainObject):
    def __init__(self, related_object):
        self.package_id = related_object.get('package_id')
        self.relation_id = related_object.get('relation_id')
        self.relationType = related_object.get('relationType')
        self.relationIdType = related_object.get('relationIdType')



meta.mapper(
    RelatedResources,
    related_resources_table,
    properties={
        u"package": orm.relation(
            Package, backref=orm.backref(u"related_resources", cascade=u"all, delete, delete-orphan")
        )
    },
)


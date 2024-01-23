# encoding: utf-8

import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import orm

from ckan.model import meta, Package, domain_object
from sqlalchemy import types as _types
from ckan.model import Session
from ckan.model import meta
from .base import Base

_all__ = [u'RelatedResources', u'related_resources_table']


class RelatedResources(Base):
    __tablename__ = 'related_resources'

    """
    Related Resources table stores the related resources for each dataset based on their "hasPart" or "isPart" of 
    ontology metadata.
    
    Initially this was created for Chemotion-Repository, but later adopted for relationship extension as well.  
    """

    id = Column(_types.Integer, primary_key=True, autoincrement=True)
    package_id = Column(_types.String, ForeignKey(Package.id), nullable=False)
    # package = relationship(Package)
    relation_id = Column(_types.JSON)
    relation_type = Column(_types.JSON)
    relation_id_type = Column(_types.JSON)
    alternate_name = Column(_types.String)

    @classmethod
    def create(cls, package_id, relation_id, relation_type, relation_id_type, alternate_name):
        """
        Create a new RelatedResource entry and store it in the database.

        :param alternate_name: Alternate names / Synonyms from MassBank
        :param package_id: The ID of the package
        :param relation_id: The relation ID
        :param relation_type: The type of relation
        :param relation_id_type: The ID type of the relation

        :return: The created RelatedResources instance
        """

        existing_entry = Session.query(cls).filter(cls.package_id == package_id).first()
        if existing_entry:
            # Return the existing entry if found
            return None
        else:
            new_related_resource = cls(
                package_id=package_id,
                relation_id=relation_id,
                relation_type=relation_type,
                relation_id_type=relation_id_type,
                alternate_name=alternate_name
            )
            Session.add(new_related_resource)
            Session.commit()

        return None

    @classmethod
    def get_mol_data_by_package_id(cls, package_id):
        """
                Retrieve related resources based on the given package ID.

                :param package_id: The ID of the package to search for
                :param session: The SQLAlchemy session for database interaction
                :return: A list of RelatedResources instances or IDs associated with the given package ID
                """
        return Session.query(cls.molecules_id).filter(cls.package_id == package_id).all()

    @classmethod
    def get_relation_values_by_package_id(cls, package_id):
        """

        :param package_id:
        :return:
        """
        relation_values = Session.query(
            cls.relation_id,
            cls.relation_type).filter(cls.package_id == package_id).all()

        return relation_values

    @classmethod
    def get_alternate_names_by_package_id(cls, package_id):
        """

        :param package_id: Given Package ID
        :return: Alternate names for the given package ID
        """
        alternate_names = Session.query(
            cls.alternate_name).filter(cls.package_id == package_id).all()

        return alternate_names


package = relationship(Package, secondary=RelatedResources, back_populates="related_resources", cascade="all, delete")

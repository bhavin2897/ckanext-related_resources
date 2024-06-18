import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
#from ckanext.related_resources.controllers.related_link import RelatedController
from flask import Blueprint


class RelatedResourcesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'related_resources')

    def get_blueprint(self):
        blueprint = Blueprint(self.name, self.__module__)

        blueprint.template_folder = u'templates'
        blueprint.add_url_rule(
            u'/localhost:5000/fancy_type/<package_name>',
            u'save_relationships',
            RelatedController.save_relationships,
            methods=['POST']
        )
        return blueprint

    # ITemplateHelpers
    def get_helpers(self):
        return {'related_resources': RelatedController.save_relationships, }

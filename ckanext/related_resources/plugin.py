import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.related_resources.models.related_resources import RelatedResources

class RelatedResourcesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'related_resources')



    def save_relationships(package_name):

        package = toolkit.get_action('package_show')({}, {'name_or_id': package_name})
        related_object = {}
        related_object['package_id'] = package['name']

        record = RelatedResources(related_object)
        record.save()

        return 0


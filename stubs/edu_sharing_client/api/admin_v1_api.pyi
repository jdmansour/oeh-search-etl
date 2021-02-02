from edu_sharing_client.api_client import ApiClient as ApiClient
from typing import Any, Optional

class ADMINV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def add_application(self, url: Any, **kwargs: Any): ...
    def add_application_with_http_info(self, url: Any, **kwargs: Any): ...
    def add_application_0(self, xml: Any, **kwargs: Any): ...
    def add_application_0_with_http_info(self, xml: Any, **kwargs: Any): ...
    def add_toolpermission(self, name: Any, **kwargs: Any): ...
    def add_toolpermission_with_http_info(self, name: Any, **kwargs: Any): ...
    def apply_template(self, template: Any, group: Any, **kwargs: Any): ...
    def apply_template_with_http_info(self, template: Any, group: Any, **kwargs: Any): ...
    def cancel_job(self, job: Any, **kwargs: Any): ...
    def cancel_job_with_http_info(self, job: Any, **kwargs: Any): ...
    def change_logging(self, name: Any, loglevel: Any, **kwargs: Any): ...
    def change_logging_with_http_info(self, name: Any, loglevel: Any, **kwargs: Any): ...
    def delete_person(self, username: Any, **kwargs: Any): ...
    def delete_person_with_http_info(self, username: Any, **kwargs: Any): ...
    def export_by_lucene(self, **kwargs: Any): ...
    def export_by_lucene_with_http_info(self, **kwargs: Any): ...
    def export_lom(self, filter_query: Any, target_dir: Any, sub_object_handler: Any, **kwargs: Any): ...
    def export_lom_with_http_info(self, filter_query: Any, target_dir: Any, sub_object_handler: Any, **kwargs: Any): ...
    def get_all_toolpermissions(self, authority: Any, **kwargs: Any): ...
    def get_all_toolpermissions_with_http_info(self, authority: Any, **kwargs: Any): ...
    def get_application_xml(self, xml: Any, **kwargs: Any): ...
    def get_application_xml_with_http_info(self, xml: Any, **kwargs: Any): ...
    def get_applications(self, **kwargs: Any): ...
    def get_applications_with_http_info(self, **kwargs: Any): ...
    def get_cache_info(self, id: Any, **kwargs: Any): ...
    def get_cache_info_with_http_info(self, id: Any, **kwargs: Any): ...
    def get_catalina_out(self, **kwargs: Any): ...
    def get_catalina_out_with_http_info(self, **kwargs: Any): ...
    def get_cluster(self, **kwargs: Any): ...
    def get_cluster_with_http_info(self, **kwargs: Any): ...
    def get_clusters(self, **kwargs: Any): ...
    def get_clusters_with_http_info(self, **kwargs: Any): ...
    def get_config(self, **kwargs: Any): ...
    def get_config_with_http_info(self, **kwargs: Any): ...
    def get_config_file(self, filename: Any, **kwargs: Any): ...
    def get_config_file_with_http_info(self, filename: Any, **kwargs: Any): ...
    def get_global_groups(self, **kwargs: Any): ...
    def get_global_groups_with_http_info(self, **kwargs: Any): ...
    def get_jobs(self, **kwargs: Any): ...
    def get_jobs_with_http_info(self, **kwargs: Any): ...
    def get_oai_classes(self, **kwargs: Any): ...
    def get_oai_classes_with_http_info(self, **kwargs: Any): ...
    def get_property_to_mds(self, properties: Any, **kwargs: Any): ...
    def get_property_to_mds_with_http_info(self, properties: Any, **kwargs: Any): ...
    def get_statistics(self, **kwargs: Any): ...
    def get_statistics_with_http_info(self, **kwargs: Any): ...
    def import_collections(self, xml: Any, **kwargs: Any): ...
    def import_collections_with_http_info(self, xml: Any, **kwargs: Any): ...
    def import_excel(self, excel: Any, parent: Any, **kwargs: Any): ...
    def import_excel_with_http_info(self, excel: Any, parent: Any, **kwargs: Any): ...
    def import_oai(self, base_url: Any, set: Any, metadata_prefix: Any, class_name: Any, **kwargs: Any): ...
    def import_oai_with_http_info(self, base_url: Any, set: Any, metadata_prefix: Any, class_name: Any, **kwargs: Any): ...
    def import_oai_xml(self, **kwargs: Any): ...
    def import_oai_xml_with_http_info(self, **kwargs: Any): ...
    def refresh_app_info(self, **kwargs: Any): ...
    def refresh_app_info_with_http_info(self, **kwargs: Any): ...
    def refresh_cache(self, folder: Any, sticky: Any, **kwargs: Any): ...
    def refresh_cache_with_http_info(self, folder: Any, sticky: Any, **kwargs: Any): ...
    def refresh_edu_group_cache(self, **kwargs: Any): ...
    def refresh_edu_group_cache_with_http_info(self, **kwargs: Any): ...
    def remove_application(self, id: Any, **kwargs: Any): ...
    def remove_application_with_http_info(self, id: Any, **kwargs: Any): ...
    def remove_cache_entry(self, **kwargs: Any): ...
    def remove_cache_entry_with_http_info(self, **kwargs: Any): ...
    def remove_oai_imports(self, base_url: Any, set: Any, metadata_prefix: Any, **kwargs: Any): ...
    def remove_oai_imports_with_http_info(self, base_url: Any, set: Any, metadata_prefix: Any, **kwargs: Any): ...
    def search_by_lucene(self, **kwargs: Any): ...
    def search_by_lucene_with_http_info(self, **kwargs: Any): ...
    def server_update_list(self, **kwargs: Any): ...
    def server_update_list_with_http_info(self, **kwargs: Any): ...
    def server_update_list_0(self, id: Any, execute: Any, **kwargs: Any): ...
    def server_update_list_0_with_http_info(self, id: Any, execute: Any, **kwargs: Any): ...
    def set_config(self, **kwargs: Any): ...
    def set_config_with_http_info(self, **kwargs: Any): ...
    def set_toolpermissions(self, authority: Any, **kwargs: Any): ...
    def set_toolpermissions_with_http_info(self, authority: Any, **kwargs: Any): ...
    def start_job(self, body: Any, job_class: Any, **kwargs: Any): ...
    def start_job_with_http_info(self, body: Any, job_class: Any, **kwargs: Any): ...
    def test_mail(self, receiver: Any, template: Any, **kwargs: Any): ...
    def test_mail_with_http_info(self, receiver: Any, template: Any, **kwargs: Any): ...
    def update_application_xml(self, xml: Any, **kwargs: Any): ...
    def update_application_xml_with_http_info(self, xml: Any, **kwargs: Any): ...
    def update_config_file(self, filename: Any, **kwargs: Any): ...
    def update_config_file_with_http_info(self, filename: Any, **kwargs: Any): ...
    def upload_temp(self, file: Any, name: Any, **kwargs: Any): ...
    def upload_temp_with_http_info(self, file: Any, name: Any, **kwargs: Any): ...

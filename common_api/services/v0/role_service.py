from typing import Dict, Optional
from common_api.services.v0.logger_service import Logger

logger = Logger()

def get_license_in_state(request) -> str:
    license_uuid = getattr(request.state, 'licence_uuid', None)
    return license_uuid


def get_api_roles(request) -> dict:
    licenses = getattr(request.state, 'licenses', None)
    licence_uuid = get_license_in_state(request)

    if not licenses or not licence_uuid:
        return {}

    api_roles = None
    for license in licenses:
        if str(license.get('uuid')) == str(licence_uuid):
            api_roles = license
            break

    return api_roles.get("api_roles", {}) if api_roles else {}


def get_app_roles(request) -> dict:
    licenses = getattr(request.state, 'licenses', None)
    licence_uuid = get_license_in_state(request)

    logger.info('Token : get_app_roles')
    if not licenses or not licence_uuid:
        return {}

    app_roles = None
    for license in licenses:
        if str(license.get('uuid')) == str(licence_uuid):
            app_roles = license
            break

    return app_roles.get("app_roles", {}) if app_roles else {}


def get_license_by_uuid(request) -> Optional[Dict]:
    licenses = getattr(request.state, 'licenses', None)
    licence_uuid = get_license_in_state(request)

    if not licenses or not licence_uuid:
        return None

    for license in licenses:
        if str(license.get('uuid')) == str(licence_uuid):
            return license

    return None

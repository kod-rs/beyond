import datetime
import enum
import functools

import packaging.version

from hat.doit.common import *  # NOQA


now = datetime.datetime.now()


VersionType = enum.Enum('VersionType', ['SEMVER', 'PIP'])


@functools.lru_cache
def get_version(version_type=VersionType.SEMVER):
    with open('VERSION', encoding='utf-8') as f:
        version = f.read().strip()
    if version.endswith('dev'):
        version += now.strftime("%Y%m%d%H%M")
    if version_type == VersionType.SEMVER:
        return version
    if version_type == VersionType.PIP:
        return packaging.version.Version(version).public
    raise ValueError()

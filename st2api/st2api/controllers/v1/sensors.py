# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import six

from st2common import log as logging
from st2common.models.api.base import jsexpose
from st2common.persistence.sensor import SensorType
from st2common.models.api.sensor import SensorTypeAPI
from st2api.controllers import resource
from st2common.rbac.types import PermissionType
from st2common.rbac.decorators import request_user_has_permission
from st2common.rbac.decorators import request_user_has_resource_permission

http_client = six.moves.http_client

LOG = logging.getLogger(__name__)


class SensorTypeController(resource.ContentPackResourceController):
    model = SensorTypeAPI
    access = SensorType
    supported_filters = {
        'name': 'name',
        'pack': 'pack'
    }

    options = {
        'sort': ['pack', 'name']
    }

    include_reference = True

    @request_user_has_permission(permission_type=PermissionType.SENSOR_TYPE_VIEW)
    @jsexpose()
    def get_all(self, **kwargs):
        return super(SensorTypeController, self)._get_all(**kwargs)

    @request_user_has_resource_permission(permission_type=PermissionType.SENSOR_TYPE_VIEW)
    @jsexpose(arg_types=[str])
    def get_one(self, ref_or_id):
        return super(SensorTypeController, self)._get_one(ref_or_id)

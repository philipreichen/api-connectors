#!/usr/bin/env python
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class SchemaApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def find(self, **kwargs):
        """Get model schemata for data objects returned by this API.

        Args:
            model, str: Optional model filter. If omitted, will return all models. (optional)

            

        Returns: object
        """

        allParams = ['model']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method find" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/schema'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        if ('model' in params):
            queryParams['model'] = self.apiClient.toPathValue(params['model'])
        if formParams:
            headerParams['Content-type'] = 'application/x-www-form-urlencoded'

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'object')
        return responseObject
        

        

    def websocketHelp(self, **kwargs):
        """Returns help text &amp; subject list for websocket usage.

        Args:
            

        Returns: object
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method websocketHelp" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/schema/websocketHelp'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        if formParams:
            headerParams['Content-type'] = 'application/x-www-form-urlencoded'

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'object')
        return responseObject
        

        

    





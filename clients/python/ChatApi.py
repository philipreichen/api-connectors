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


class ChatApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def get(self, **kwargs):
        """Get chat messages.

        Args:
            start, float: Starting point for results. (optional)

            reverse, bool: If true, will sort results newest first. (optional)

            count, float: Number of results to fetch. (optional)

            

        Returns: Array[Chat]
        """

        allParams = ['start', 'reverse', 'count']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/chat'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        if ('start' in params):
            queryParams['start'] = self.apiClient.toPathValue(params['start'])
        if ('reverse' in params):
            queryParams['reverse'] = self.apiClient.toPathValue(params['reverse'])
        if formParams:
            headerParams['Content-type'] = 'application/x-www-form-urlencoded'

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Chat]')
        return responseObject
        

        

    def send(self, message, **kwargs):
        """Send a chat message.

        Args:
            message, str:  (required)

            

        Returns: Chat
        """

        allParams = ['message']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method send" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/chat'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        if ('message' in params):
            formParams['message'] = params['message']
        if formParams:
            headerParams['Content-type'] = 'application/x-www-form-urlencoded'

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Chat')
        return responseObject
        

        

    





<?php
/**
 *  Copyright 2011 Wordnik, Inc.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

/**
 *
 * NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
 */
class OrderBookApi {

  function __construct($apiClient) {
    $this->apiClient = $apiClient;
  }

  /**
   * getOrderBook
   * Get current orderbook.
   * 
   * @param string $symbol Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. (required)
   * @param float $depth Orderbook depth. (optional)
   * @return Array[OrderBook]
   */

   public function getOrderBook($symbol, $depth=null) {

      //parse inputs
      $resourcePath = "/orderBook";
      $resourcePath = str_replace("{format}", "json", $resourcePath);
      $method = "GET";
      $queryParams = array();
      $headerParams = array();
      $headerParams['Accept'] = 'application/json';
      $headerParams['Content-Type'] = 'application/json';

      if($symbol != null) {
        $queryParams['symbol'] = $this->apiClient->toQueryValue($symbol);
      }
      if($depth != null) {
        $queryParams['depth'] = $this->apiClient->toQueryValue($depth);
      }
      // Generate form params
      if (! isset($body)) {
        $body = array();
      }
      if (empty($body)) {
        $body = null;
      }

      // Make the API Call
      $response = $this->apiClient->callAPI($resourcePath, $method,
                                            $queryParams, $body,
                                            $headerParams);


      if(! $response){
          return null;
      }

      $responseObject = $this->apiClient->deserialize($response,
                                                      'Array[OrderBook]');
      return $responseObject;

      }
  

}


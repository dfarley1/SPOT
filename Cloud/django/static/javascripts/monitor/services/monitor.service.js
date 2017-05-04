(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.services')
    .factory('Monitor', Monitor);

  Monitor.$inject = ['$cookies', '$http'];

  // Returns factory
  function Monitor($cookies, $http) {
    var Monitor = {
      create_spot: create_spot
    }; 

    return Monitor;

    // Define factory functionality
    function create_spot(spot_name) {
      return $http.post('/monitor', {
        spot_name: spot_name
      }).then(create_spotSuccessFn, create_spotErrorFn);

      // Define Success and failure methods
      function create_spotSuccessFn(data, status, headers, config) {
        console.log('Successful POST to /monitor!');
      }
      function create_spotErrorFn(data, status, headers, config) {
        console.error('FAILED to POST to /monitor!');
      }
    }
  }
})();

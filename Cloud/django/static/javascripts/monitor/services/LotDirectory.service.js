(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.services')
    .factory('LotDirectory', LotDirectory);

  LotDirectory.$inject = ['$cookies', '$http'];

  // Returns factory
  function LotDirectory($cookies, $http) {
    var LotDirectory = {
      getDirectory: getDirectory
    }; 

    return LotDirectory;

    // Define factory functionality
    function getDirectory(lot_name) {
      return $http.post('/api/v1/monitor/create_lot/', {
        lot_name: lot_name
      }).then(create_lotSuccessFn, create_lotErrorFn);

      // Define Success and failure methods
      function create_lotSuccessFn(data, status, headers, config) {
        console.log('Successful POST to /monitor!');
        window.location = "/monitor"
      }
      function create_lotErrorFn(data, status, headers, config) {
        console.error('FAILED to POST to /monitor!');
      }
    }
  }
})();

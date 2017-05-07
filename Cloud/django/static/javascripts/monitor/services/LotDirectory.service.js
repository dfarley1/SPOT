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
    function getDirectory(test_receive) {
      return $http.get('/api/v1/monitor/list_lots/',
      ).then(getDirectorySuccessFn, getDirectoryErrorFn);

      // Define Success and failure methods
      function getDirectorySuccessFn(data, status, headers, config) {
        test_receive = data;
        console.log(test_receive);
        console.log('Successfuly load directory');
      }
      function getDirectoryErrorFn(data, status, headers, config) {
        console.error('FAILED to GET directory');
      }
    }
  }
})();

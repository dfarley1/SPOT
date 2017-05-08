(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.services')
    .factory('LotDirectory', LotDirectory);

  LotDirectory.$inject = ['$cookies', '$http'];

  // Returns factory
  function LotDirectory($cookies, $http) {
    // Define functions
    var LotDirectory = {
      getDirectory: getDirectory
    }; 

    return LotDirectory;

    // Define factory functionality
    function getDirectory() {
      //$http.get('/api/v1/monitor/list_lots/',
      //).then(getDirectorySuccessFn, getDirectoryErrorFn);

      // Define Success and failure methods
      //function getDirectorySuccessFn(data, status, headers, config) {
      //  console.log(data.data);
      //  console.log('Successfuly load directory');
      //  dir = data.data;
      //}
      //function getDirectoryErrorFn(data, status, headers, config) {
      //  console.error('FAILED to GET directory');
      //}
      //console.log('ran it');
      return ['t1', 't2'];
    }
  }
})();

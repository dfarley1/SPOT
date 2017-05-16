(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('LotDirectoryController', LotDirectoryController);

  LotDirectoryController.$inject = ['$location', '$scope', '$http',  'LotDirectory'];

  function LotDirectoryController($location, $scope, $http ,LotDirectory) {
    // Initialization
    var LotVM = this;
    LotVM.lot_directory = [{name:'Loading Lots...'},];

    LoadLotDirectory();

    



    // API
    function LoadLotDirectory() {
      $http.get('/api/v1/monitor/list_lots/',
      ).then(getDirectorySuccessFn, getDirectoryErrorFn);
   
      //Define Success and failure methods
      function getDirectorySuccessFn(data, status, headers, config) {
        console.log(data.data);
        LotVM.lot_directory = data.data;
      }

      function getDirectoryErrorFn(data, status, headers, config) {
        console.error('FAILED to GET directory');
      }
    }



  }
})();

(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('LotDirectoryController', LotDirectoryController);

  LotDirectoryController.$inject = ['$location', '$scope', '$http',  'LotDirectory'];

  function LotDirectoryController($location, $scope, $http ,LotDirectory) {
    // Initialization
    var LotVM = this;
    var dir;
    $http.get('/api/v1/monitor/list_lots/',
    ).then(getDirectorySuccessFn, getDirectoryErrorFn);
      
    // LotVM.lot_directory = ['test1', 'test2', 'test3'];
    // getDir();

    function getDir() {
      LotVM.lot_directory = LotDirectory.getDirectory();
      // console.log(LotVM.lot_directory);
      // return LotVM.lot_directory;
    }


    //Define Success and failure methods
    function getDirectorySuccessFn(data, status, headers, config) {
      // console.log(data.data);
      //  console.log('Successfuly load directory');
      dir = data.data;
      console.log(dir);
      LotVM.lot_directory = dir;
    }
    
    function getDirectoryErrorFn(data, status, headers, config) {
      console.error('FAILED to GET directory');
    }
  }
})();

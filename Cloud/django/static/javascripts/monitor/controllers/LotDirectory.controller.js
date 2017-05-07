(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('LotDirectoryController', LotDirectoryController);

  LotDirectoryController.$inject = ['$location', '$scope', 'LotDirectory'];

  function LotDirectoryController($location, $scope, LotDirectory) {
    // Initialization
    var LotVM = this;

    LotVM.lot_directory = ['test1', 'test2', 'test3'];
    LotVM.getDirectory = getDirectory;
  
    function getDirectory() {
      LotDirectory.getDirectory(LotVM.lot_name);
    }
  }
})();

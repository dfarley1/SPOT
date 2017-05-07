(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('MonitorController', MonitorController);

  MonitorController.$inject = ['$location', '$scope', 'Monitor'];

  function MonitorController($location, $scope, Monitor) {
    var vm = this;
    vm.create_lot = create_lot;
  
    function create_lot() {
      Monitor.create_lot(vm.lot_name);
    }
  }
})();

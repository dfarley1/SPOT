(function () {
  'use strict';

  angular
    .module('sdpspot.monitor.controllers')
    .controller('MonitorController', MonitorController);

  MonitorController.$inject = ['$location', '$scope', 'Monitor'];

  function MonitorController($location, $scope, Monitor) {
    var vm = this;
    vm.create_spot = create_spot;
  
    function create_spot() {
      Monitor.create_spot(vm.spot_name);
    }
  }
})();

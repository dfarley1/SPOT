(function () {
  'use strict';

  angular
    .module('sdpspot.monitor', [
      'sdpspot.monitor.controllers',
      'sdpspot.monitor.services'
    ]);

  angular
    .module('sdpspot.monitor.controllers', []);

  angular
    .module('sdpspot.monitor.services', ['ngCookies']);
})();

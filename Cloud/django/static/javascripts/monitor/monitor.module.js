(function () {
  'use strict';

  angular
    .module('sdpspot.monitor', [
      'sdpspot.monitor.controllers',
      'sdpspot.monitor.services',
      'rwdImageMaps'
    ]);

  angular
    .module('sdpspot.monitor.controllers', ['rwdImageMaps']);

  angular
    .module('sdpspot.monitor.services', ['ngCookies']);
})();

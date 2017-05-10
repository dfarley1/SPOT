(function () {
  'use strict';

  angular
    .module('sdpspot.authentication', [
      'sdpspot.authentication.controllers',
      'sdpspot.authentication.services'
    ]);

  angular
    .module('sdpspot.authentication.controllers', ['ngDialog']);

  angular
    .module('sdpspot.authentication.services', ['ngCookies']);
})();
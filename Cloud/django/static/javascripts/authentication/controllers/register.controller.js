/**
* Register controller
* @namespace sdpspot.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('sdpspot.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf sdpspot.authentication.controllers.RegisterController
    */
    function register() {
      Authentication.register(vm.email, vm.password, vm.username);
    }
  }
})();
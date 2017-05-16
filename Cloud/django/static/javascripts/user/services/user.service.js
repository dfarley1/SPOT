 (function () {
    'use strict';

    angular
        .module('sdpspot.user.services')
        .factory('User', User);

    User.$inject = ['$cookies', '$http'];

    function User($cookies, $http) {
        var User = {
        }; 
        return User;
    }
})();